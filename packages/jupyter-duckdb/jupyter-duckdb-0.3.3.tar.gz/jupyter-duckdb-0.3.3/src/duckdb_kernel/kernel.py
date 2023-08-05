import json
import os
import re
import time
import traceback
from typing import Optional, Dict, List, Tuple

import duckdb
from ipykernel.kernelbase import Kernel
import checkmarkandcross


class DuckDBKernel(Kernel):
    implementation = 'DuckDB'
    implementation_version = '0.6.1'
    banner = 'DuckDB Kernel'
    language_info = {
        'name': 'duckdb',
        'mimetype': 'application/sql',
        'file_extension': '.sql',
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._db: Optional[duckdb.DuckDBPyConnection] = None
        self._tests: Optional[Dict] = None

    # output related functions
    def print(self, text: str, name: str = 'stdout'):
        self.send_response(self.iopub_socket, 'stream', {
            'name': name,
            'text': text
        })

    def print_exception(self, e: Exception):
        if isinstance(e, AssertionError):
            text = str(e)
        elif isinstance(e, (duckdb.OperationalError, duckdb.ProgrammingError)):
            text = str(e)
        else:
            text = traceback.format_exc()

        self.print(text, 'stderr')

    def print_data(self, *data: str, mime: str = 'text/html'):
        for v in data:
            self.send_response(self.iopub_socket, 'display_data', {
                'data': {
                    mime: v
                },
                # `metadata` is required. Otherwise, Jupyter Lab does not display any output.
                # This is not the case when using Jupyter Notebook btw.
                'metadata': {}
            })

    # database related functions
    def _load_database(self, database: str, read_only: bool):
        if self._db is None:
            self._db = duckdb.connect(database, read_only)
            return True
        else:
            return False

    def _unload_database(self):
        if self._db is not None:
            self._db.close()
            self._db = None
            return True
        else:
            return False

    def _execute_stmt(self, query: str, silent: bool) -> Tuple[List[str], List[List]]:
        if self._db is None:
            raise AssertionError('load a database first')

        with self._db.cursor() as cursor:
            # execute query and store start and end timestamp
            st = time.time()
            cursor.execute(query)
            et = time.time()

            if not silent:
                if query.strip().startswith('EXPLAIN'):
                    rows = cursor.fetchall()
                    for ekey, evalue in rows:
                        self.print_data(f'<b>{ekey}</b><br><pre>{evalue}</pre>')

                else:
                    # table header
                    table_header = ''.join(map(lambda e: f'<th>{e[0]}</th>', cursor.description))

                    # table data
                    rows = cursor.fetchall()

                    table_data = ''.join(map(
                        lambda row: '<tr>' + ''.join(map(lambda e: f'<td>{e}</td>', row)) + '</tr>',
                        rows
                    ))

                    # send to client
                    self.print_data(f'''
                        <table class="duckdb-query-result">
                            {table_header}
                            {table_data}
                        </table>
                    ''')

                    self.print_data(f'{len(rows)} row{"" if len(rows) == 1 else "s"} in {et - st:.3f}s')

            return [e[0] for e in cursor.description], rows

    # magic command related functions
    def _load_magic(self, silent: bool, target: str, create: bool, source: Optional[str], tests: Optional[str]):
        # unload current database if necessary
        if self._unload_database():
            if not silent:
                self.print('unloaded database\n')

        # print kernel version
        if not silent:
            self.print(f'{self.implementation} {self.implementation_version}\n')

        # load new database
        if target.startswith(("'", '"')):
            target = target[1:-1]

        if create and os.path.exists(target):
            os.remove(target)

        if self._load_database(target, read_only=False):
            if not silent:
                self.print(f'loaded database {target}\n')

        # copy data from source database
        if source is not None:
            if source.startswith(("'", '"')):
                source = source[1:-1]

            if source.endswith('.sql'):
                with open(source, 'r') as file:
                    content = file.read()

                    # statements = re.split(r';\r?\n', content)
                    # for statement in statements:
                    #     self._db.execute(statement)

                    self._db.execute(content)

                    if not silent:
                        self.print(f'executed {source}')

            else:
                with duckdb.connect(source, read_only=True) as source_db:
                    source_db.execute('SHOW TABLES')
                    for table, in source_db.fetchall():
                        transfer_df = source_db.query(f'SELECT * FROM {table}').to_df()
                        self._db.execute(f'CREATE TABLE {table} AS SELECT * FROM transfer_df')

                        if not silent:
                            self.print(f'transferred table {table}\n')

        # load tests
        if tests is None:
            self._tests = {}
        else:
            with open(tests, 'r') as tests_file:
                self._tests = json.load(tests_file)
                self.print(f'loaded tests from {tests}')

    def _test_magic(self, name: str, description: List[str], result: List[List], silent: bool):
        # Testing makes no sense if there is no output.
        if silent:
            return

        # extract data for test
        data = self._tests[name]

        # prepare comparison functions
        def my_equals(row1, row2):
            return len(row1) == len(row2) and all((x == y for x, y in zip(row1, row2)))

        def my_in(row, rows):
            for r in rows:
                if my_equals(r, row):
                    return True

            return False

        # ordered test
        if data['ordered']:
            rows = data['equals']
            missing = len(rows) - len(result)

            if missing > 0:
                return self.print_data(checkmarkandcross.image_html(
                    False, title=f'{missing} row{"" if missing == 1 else "s"} missing'
                ))

            if missing < 0:
                return self.print_data(checkmarkandcross.image_html(
                    False, title=f'{-missing} row{"" if -missing == 1 else "s"} more than required'
                ))

            for data_row, result_row in zip(data['equals'], result):
                if not my_equals(data_row, result_row):
                    return self.print_data(checkmarkandcross.image_html(False, title='found row without match'))

            return self.print_data(checkmarkandcross.image_html(True, title='success'))

        # unordered test
        else:
            rows = data['equals']

            missing = 0
            for element in rows:
                if not my_in(element, result):
                    missing += 1

            if missing > 0:
                return self.print_data(checkmarkandcross.image_html(
                    False, title=f'{missing} row{"" if missing == 1 else "s"} missing'
                ))

            over = 0
            for element in result:
                if not my_in(element, rows):
                    over += 1

            if over > 0:
                return self.print_data(checkmarkandcross.image_html(
                    False, title=f'{over} row{"" if over == 1 else "s"} more than required'
                ))

            return self.print_data(checkmarkandcross.image_html(True, title='success'))

    def _handle_magic(self, code: str, silent: bool):
        code_lower = code.lower()

        if code_lower.startswith('%load'):
            # parse line
            match = re.match(
                r'''^%LOAD +([^ ]+?|'.+?'|".+?")( +WITH +([^ ]+?|'.+?'|".+?"))?$''',
                code.strip(), re.IGNORECASE
            )
            if match is None:
                raise AssertionError('usage: %LOAD target.db [WITH tests.json]')

            # call
            self._load_magic(silent, match.group(1), False, None, match.group(3))

        elif code_lower.startswith('%create'):
            # parse line
            match = re.match(
                r'''^%CREATE +([^ ]+?|'.+?'|".+?")( +FROM +([^ ]+?|'.+?'|".+?"))?( +WITH +([^ ]+?|'.+?'|".+?"))?$''',
                code.strip(), re.IGNORECASE
            )
            if match is None:
                raise AssertionError('usage: %CREATE target.db [FROM (source.db | source.sql)] [WITH tests.json]')

            # call
            self._load_magic(silent, match.group(1), True, match.group(3), match.group(5))

        elif code_lower.startswith('%test'):
            # parse line
            match = re.match(
                r'''^%TEST +([^ ]+?|'.+?'|".+?")$''',
                code, re.IGNORECASE | re.MULTILINE
            )

            if match is None:
                raise AssertionError('usage: %TEST name')
            if match.group(1) not in self._tests:
                raise AssertionError(f'test {match.group(1)} unknown')

            # execute statement
            description, rows = self._execute_stmt(code[match.end():], silent)

            # execute tests
            self._test_magic(match.group(1), description, rows, silent)

        else:
            raise AssertionError('unknown magic command')

    # jupyter related functions
    def do_execute(self, code: str, silent: bool,
                   store_history: bool = True, user_expressions: dict = None, allow_stdin: bool = False,
                   **kwargs):
        try:
            # handle magic commands
            if code.startswith('%'):
                self._handle_magic(code, silent)

            # execute statement otherwise
            else:
                self._execute_stmt(code, silent)

            return {
                'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {}
            }

        except Exception as e:
            self.print_exception(e)

            return {
                'status': 'error',
                'ename': str(type(e)),
                'evalue': str(e),
                'traceback': traceback.format_exc()
            }

    def do_shutdown(self, restart):
        self._unload_database()
        return super().do_shutdown(restart)
