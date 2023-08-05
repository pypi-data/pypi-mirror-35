class JRDBParser:
    def __init__(self, schema):
            self.schema = schema

    def parse(self, line: str):
        ret_dict = dict()

        def strip(value):
            return value.decode('cp932').strip().rstrip('\x00')

        for field in self.schema['fields']:
            value = strip(line[field['start']:field['end']])
            ret_dict[field['name']] = value

        return ret_dict
