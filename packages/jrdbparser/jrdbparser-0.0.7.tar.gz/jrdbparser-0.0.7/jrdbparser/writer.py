import fastavro


class JRDBAvroWriter:
    def __init__(self, schema):
        self.schema = fastavro.parse_schema(schema)

    def write(self, fo, records: list):
        fastavro.write.writer(fo, self.schema, records)
