class JRDBParser:
    def __init__(self, schema):
            self.schema = schema

    def cast(self, types, value):
        if 'float' in types and 'null' in types:
            return float(value) if value else None
        elif 'int' in types and 'null' in types:
            return int(value) if value else None
        elif 'float' in types and value:
            return float(value)
        elif 'int' in types and value:
            return int(value)
        elif 'string' in types:
            return value
        else:
            raise Exception(F'Cannot cast "{value}" to {types} types.')

    def parse(self, line: str):
        ret_dict = dict()

        def strip(value):
            return value.decode('cp932').strip().rstrip('\x00')

        for field in self.schema['fields']:
            value = strip(line[field['start']:field['end']])

            types = field['type'] if isinstance(field['type'], list) else [field['type']]

            try:
                ret_dict[field['name']] = self.cast(types, value)
            except Exception as e:
                print(f'Cannot cast value. field is {field}')
                raise e

        return ret_dict
