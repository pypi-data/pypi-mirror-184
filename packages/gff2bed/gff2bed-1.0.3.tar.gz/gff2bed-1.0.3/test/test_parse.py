import pytest
import gff2bed
from gff2bed.gff2bed import parse_gff_attributes

def test_parse_attr():
    assert parse_gff_attributes('ID=01') == {'ID': '01'}
    assert parse_gff_attributes('ID=01;DUMMY', graceful=True) == {'ID': '01'}

def test_parse(gff_file, gff_data):
    assert tuple(gff2bed.parse(gff_file)) == gff_data
