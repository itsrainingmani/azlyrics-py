from azlyrics import __version__
import pytest
import azlyrics.azlyrics as az


def test_version():
    assert __version__ == '0.1.0'

class TestClass(object):
    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (("Metallica", "One"), ("metallica", "one")),
            (("The Killers", "The Man"), ("killers", "theman")),
            (("King Gizzard & the LizArd wizArd", "woRk-This-Time"), ("kinggizzardthelizardwizard", "workthistime"))
        ],
    )
    def test_clean_names(self, inp, exp):
        assert az.clean_names(inp[0], inp[1]) == exp

    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (
                ("metallica", "one"),
                ("https://www.azlyrics.com/lyrics/metallica/one.html")
            ),
            (
                ("killers", "theman"),
                ("https://www.azlyrics.com/lyrics/killers/theman.html")
            ),
        ],
    )
    def test_create_url(self, inp, exp):
        assert az.create_url(inp[0], inp[1]) == exp