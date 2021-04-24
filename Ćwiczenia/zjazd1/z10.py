

def is_palindrome(napis: str):
    znaki = ".,?/() \'\":;!-"
    for element in znaki:
        napis = napis.replace(element, "")

    napis = napis.lower()

    odw_napis = napis[::-1]

    return odw_napis == napis


def test_is_palindrome():
    assert is_palindrome("kajak") is True
    assert is_palindrome("A to kawony sama da Ada? Ma synowa kota.") is True
    assert is_palindrome("alaaa") is False
    assert is_palindrome("Ado, pyta bandzior komu mokro? I z dna baty poda?") is True
    assert is_palindrome("Ada goła im śmiało gada!") is True
