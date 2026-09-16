def parse_duration(s):
    if s.endswith("h"):
        return int(s[:-1]) * 60
    raise ValueError("unsupported")
