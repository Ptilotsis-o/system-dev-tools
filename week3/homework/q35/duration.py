import re

def parse_duration(s):
    m = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?", s)
    if not m:
        raise ValueError("unsupported")
    h = int(m.group(1) or 0)
    mi = int(m.group(2) or 0)
    return h * 60 + mi
