import subprocess
import sys

def run_cli(*args):
    cmd = [sys.executable, "-m", "calc.cli", *args]
    return subprocess.run(cmd, capture_output=True, text=True)

def test_add():
    r = run_cli("--op", "add", "--a", "2", "--b", "3")
    assert r.stdout.strip() == "5.0"

def test_sub():
    r = run_cli("--op", "sub", "--a", "5", "--b", "2")
    assert r.stdout.strip() == "3.0"
