from string_lists import is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("not a palindrome") == False
    assert is_palindrome("UFO Tofu") == True
    assert is_palindrome("Sir, I demand, I am a maid named Iris.") == True
    assert is_palindrome("Cannot be a palindrome...") == False
    assert is_palindrome("") == True
