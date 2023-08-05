import fastavro


class JRDBAvroWriter:
    def __init__(self, out, schema):
        for field in schema['fields']:
            del field['start']
            del field['end']

        self.writer = fastavro.write.Writer(
            out, schema)

    def write(self, line: dict):
        self.writer.write(line)

    def flush(self):
        self.writer.flush()
