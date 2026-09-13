import sys

import pytest

from greetlab.cli import main


def test_normal_name(capsys):
    sys.argv = ["sdt-greet", "--name", "Alice"]
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_blank_name_exits(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
