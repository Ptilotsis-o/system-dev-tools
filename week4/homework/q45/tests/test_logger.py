import logging
from logger import log_message

def test_log(caplog):
    with caplog.at_level(logging.INFO):
        log_message("hello")
    assert "LOG: hello" in caplog.text
