from az import __version__
import pytest
import az.lyrics as api


def test_version():
    assert __version__ == '0.1.0'

class TestClass(object):
    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (("Metallica", "One"), ("metallica", "one")),
            (("The Killers", "The Man"), ("killers", "theman")),
            (("King Gizzard & the LizArd wizArd", "woRk-This-Time"), ("kinggizzardthelizardwizard", "workthistime")),
            (("King Gizzard &the LizArd wizArd", "Head on / Pill"), ("kinggizzardthelizardwizard", "headonpill")),
            (("King Gizzard & the LizArd wizArd", "Danger $$$"), ("kinggizzardthelizardwizard", "danger")),
            (("King Gizzard & the LizArd wizArd", "Her And I (Slow Jam 2)"), ("kinggizzardthelizardwizard", "herandislowjam2")),
            (("King Gizzard & The Lizard Wizard", "TIme = Fate"), ("kinggizzardthelizardwizard", "timefate")),
        ],
    )
    def test_clean_names(self, inp, exp):
        assert api.clean_names(inp[0], inp[1]) == exp

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
        assert api.create_url(inp[0], inp[1]) == exp

    # @pytest.mark.parametrize(
    #     ("inp", "exp"),
    #     [
    #         (
    #             ("metallica", "one"),
    #             ("https://www.azlyrics.com/lyrics/metallica/one.html")
    #         ),
    #         (
    #             ("killers", "theman"),
    #             ("https://www.azlyrics.com/lyrics/killers/theman.html")
    #         ),
    #     ],
    # )
    # def test_create_url_uncleaned(self, inp, exp):
    #     assert api.create_url(inp[0], inp[1]) == exp