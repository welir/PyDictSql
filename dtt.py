import ast
import datetime


class DictToTable:
    dict_array = {}
    date_formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%m/%d/%Y', '%Y-%m-%d', '%d.%m.%Y']

    def __init__(self, array_dict):
        self.dict_array = array_dict

    def is_valid_date(self, date_text, format_date):
        try:
            if date_text is None or type(date_text) not in [str]:
                return False
            if datetime.datetime.strptime(date_text, format_date) is not None:
                return True
            else:
                return False
        except ValueError:
            return False

    def validate_date(self, date_text):
        try:
            for f in self.date_formats:
                if self.is_valid_date(date_text, f):
                    return True
        except ValueError:
            return False

    def get_data_type(self, val):
        # try:
        # Evaluates numbers to an appropriate type, and strings an error
        # if self.validate_date(val):
        #     t = datetime.datetime.now()
        # else:
        #     t = ast.literal_eval(val)

        # except ValueError:
        #     pass
        # except SyntaxError:
        #     return 'varchar'

        if type(val) == dict:
            return 'dict'

        if type(val) in [int, float]:
            if (type(val) in [int]):
                # Use smallest possible int type
                if (-32768 < val < 32767):
                    return 'smallint'
                elif (-2147483648 < val < 2147483647):
                    return 'int'
                else:
                    return 'bigint'
            if type(val) is float:
                return 'decimal'

        else:
            if isinstance(val, datetime.datetime):
                return 'datetime2(7)'

            return 'varchar'

    def dict_to_ddl(self, dict_array):
        headers = []

        for key, value in dict_array.items():
            if self.get_data_type(value) == 'varchar':
                headers.append([key, self.get_data_type(value), 512, value])
            else:
                headers.append([key, self.get_data_type(value), -1, value])

        return headers

    def create_ddl_string(self, table_name):
        headers = self.dict_to_ddl(self.dict_array)

        if headers is None:
            return ''

        statement = 'create table {0} ('.format(table_name)

        for h in headers:
            if h[1] == 'varchar':
                statement = (statement + '\n{} varchar({}),').format(h[0].upper(), str(h[2]))

            else:
                if (h[1] == 'dict'):

                    d = DictToTable(h[3])
                    print("")
                    print(d.create_ddl_string(h[0]))
                    print("")
                else:
                    statement = (statement + '\n' + '{} {}' + ',').format(h[0].upper(), h[1])

        statement = statement[:-1] + ');'

        return statement
