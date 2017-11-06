from probe.domain.taskerize import TypeResult
from probe.domain.taskerize import TaskResult


class TextFileRepository:

    def __init__(self, filename):
        self.filename = filename

    def add(self, result):
        s = self._result_to_string(result)
        with open(self.filename, 'w') as f:
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
        out = ','.join([result.action, str(result.item), result.type.name, str(result.value), str(result.time)])
        return out

    def _string_to_result(self, line):
        items = line.split(',')

        items[2] = TypeResult[items[2]]  # TypeResult conversion
        if items[3] == 'None':
            items[3] = None
        if items[4] == 'None':
            items[4] = None
        else:
            items[4] = float(items[4])  # Time conversion (seconds)

        return TaskResult(*items)
