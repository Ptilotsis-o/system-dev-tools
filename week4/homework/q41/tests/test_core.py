from strutil.core import reverse, is_palindrome

def test_reverse():
    assert reverse("abc") == "cba"
    assert reverse("") == ""

def test_is_palindrome():
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
