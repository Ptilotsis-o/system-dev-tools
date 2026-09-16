from duration import parse_duration

def test_1h30m():
    assert parse_duration("1h30m") == 90

def test_2h():
    assert parse_duration("2h") == 120
