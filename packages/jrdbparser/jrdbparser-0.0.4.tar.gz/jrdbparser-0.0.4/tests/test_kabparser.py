from jrdbparser import JRDBParser, schema
from jrdbparser import JRDBAvroWriter
from io import BytesIO
import json


def test_1():
    kab_parser = JRDBParser(schema.kab)
    with open('tests/data/kab_input.txt', 'rb') as f:
        lines = f.readlines()

    actual = kab_parser.parse(lines[0])

    with open('tests/data/kab_expected.json', 'r') as f:
        expected = json.load(f)

    assert expected == actual


def test_2():
    kab_parser = JRDBParser(schema.kab)
    with open('tests/data/kab_input.txt', 'rb') as f:
        lines = f.readlines()

    kab_data = kab_parser.parse(lines[0])

    buf = BytesIO()
    writer = JRDBAvroWriter(buf, schema.kab)
    writer.write(kab_data)
    writer.flush()
