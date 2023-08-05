class JRDBParser:
    def __init__(self, schema):
            self.schema = schema

    def parse(self, line: str):
        ret_dict = dict()

        def strip(value):
            return value.decode('cp932').strip().rstrip('\x00')

        for field in self.schema['fields']:
            value = strip(line[field['start']:field['end']])

            types = field['type'] if isinstance(field['type'], list) else [field['type']]

            if 'int' in types and 'null' in types:
                ret_dict[field['name']] = int(value) if value else None
            elif 'int' in types:
                ret_dict[field['name']] = int(value)
            else:
                ret_dict[field['name']] = value

        return ret_dict
