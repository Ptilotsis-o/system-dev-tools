import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

import pytest
from greetlab.cli import main

def test_blank_name_exits(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2
