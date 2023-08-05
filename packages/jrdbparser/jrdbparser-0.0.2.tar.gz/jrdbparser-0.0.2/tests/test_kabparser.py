from jrdbparser import JRDBParser, schema
import json


def test_1():
    kab_parser = JRDBParser(schema.kab)
    with open('tests/data/kab_input.txt', 'rb') as f:
        lines = f.readlines()

    actual = kab_parser.parse(lines[0])

    with open('tests/data/kab_expected.json', 'r') as f:
        expected = json.load(f)

    assert expected == actual
