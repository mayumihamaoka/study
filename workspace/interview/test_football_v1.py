# test_football_v1.py
import pytest
# import football_v1 as fb

# ...

def test_parse_next_line(mock_csv_data):
    all_lines = [line for line in fb.parse_next_line(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 7
