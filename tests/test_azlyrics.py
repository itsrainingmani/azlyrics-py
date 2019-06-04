from azlyrics import __version__
import pytest
import azlyrics.lyrics as api


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
        assert api._clean_names(inp[0], inp[1]) == exp

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
            (
                ("kinggizzardthelizardwizard", "workthistime"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/workthistime.html")
            ),
            (
                ("kinggizzardthelizardwizard", "headonpill"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/headonpill.html")
            ),
            (
                ("kinggizzardthelizardwizard", "danger"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/danger.html")
            ),
            (
                ("kinggizzardthelizardwizard", "herandislowjam2"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/herandislowjam2.html")
            ),
            (
                ("kinggizzardthelizardwizard", "timefate"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/timefate.html")
            ),
        ],
    )
    def test_create_url(self, inp, exp):
        assert api._create_url(inp[0], inp[1]) == exp

    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (
                ("Metallica", "One"),
                ("https://www.azlyrics.com/lyrics/metallica/one.html")
            ),
            (
                ("The Killers", "The Man"),
                ("https://www.azlyrics.com/lyrics/killers/theman.html")
            ),
            (
                ("King Gizzard & the LizArd wizArd", "woRk-This-Time"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/workthistime.html")
            ),
            (
                ("King Gizzard &the LizArd wizArd", "Head on / Pill"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/headonpill.html")
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Danger $$$"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/danger.html")
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Her And I (Slow Jam 2)"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/herandislowjam2.html")
            ),
            (
                ("King Gizzard & The Lizard Wizard", "TIme = Fate"),
                ("https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/timefate.html")
            ),
        ],
    )
    def test_create_url_uncleaned(self, inp, exp):
        assert api._create_url(inp[0], inp[1]) == exp
