import fastavro


class JRDBAvroWriter:
    def __init__(self, schema):
        for field in schema['fields']:
            del field['start']
            del field['end']

        self.schema = schema

    def write(self, fo, records: list):
        fastavro.write.writer(fo, self.schema, records)
