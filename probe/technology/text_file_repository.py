import datetime
from probe.domain.taskerize import TypeResult
from probe.domain.taskerize import TaskResult


class TextFileRepository:

    def __init__(self, filename):
        self.filename = filename

    def add(self, result):
        s = self._result_to_string(result)
        with open(self.filename, 'a') as f:
            f.write(s)

    def get_first(self):
        result = None
        with open(self.filename, 'r') as f:
            line = f.readline()
            result = self._string_to_result(line)
        return result

    def get_last(self):
        result = None
        with open(self.filename, 'r') as f:
            line = f.readlines()[-1]
            result = self._string_to_result(line)
        return result

    def get_all(self):
        lines = self.file.readlines()
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print(lines)

    def _result_to_string(self, result):
        out = ','.join([datetime.datetime.strftime(result.timestamp, '%d-%m-%Y %H:%M:%S'), result.action, str(result.item), result.type.name, str(result.value), str(result.time)])
        out += '\n'
        return out

    def _string_to_result(self, line):
        items = line.rstrip('\n').split(',')

        items[0] = datetime.datetime.strptime(items[0], '%d-%m-%Y %H:%M:%S')
        items[3] = TypeResult[items[3]]  # TypeResult conversion
        if items[4] == 'None':
            items[4] = None
        if items[5] == 'None':
            items[5] = None
        else:
            items[5] = float(items[5])  # Time conversion (seconds)

        return TaskResult(*items)
