from azlyrics import __version__
import pytest
import azlyrics.lyrics as api


def test_version():
    assert __version__ == "0.1.0"


class TestClass(object):
    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (("Metallica", "One"), ("metallica", "one")),
            (("The Killers", "The Man"), ("killers", "theman")),
            (
                ("King Gizzard & the LizArd wizArd", "woRk-This-Time"),
                ("kinggizzardthelizardwizard", "workthistime"),
            ),
            (
                ("King Gizzard &the LizArd wizArd", "Head on / Pill"),
                ("kinggizzardthelizardwizard", "headonpill"),
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Danger $$$"),
                ("kinggizzardthelizardwizard", "danger"),
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Her And I (Slow Jam 2)"),
                ("kinggizzardthelizardwizard", "herandislowjam2"),
            ),
            (
                ("King Gizzard & The Lizard Wizard", "TIme = Fate"),
                ("kinggizzardthelizardwizard", "timefate"),
            ),
        ],
    )
    def test_clean_names(self, inp, exp):
        assert api._clean_names(inp[0], inp[1]) == exp

    @pytest.mark.parametrize(
        ("inp", "exp"),
        [
            (
                ("metallica", "one"),
                ("https://www.azlyrics.com/lyrics/metallica/one.html"),
            ),
            (
                ("killers", "theman"),
                ("https://www.azlyrics.com/lyrics/killers/theman.html"),
            ),
            (
                ("kinggizzardthelizardwizard", "workthistime"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/workthistime.html"
                ),
            ),
            (
                ("kinggizzardthelizardwizard", "headonpill"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/headonpill.html"
                ),
            ),
            (
                ("kinggizzardthelizardwizard", "danger"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/danger.html"
                ),
            ),
            (
                ("kinggizzardthelizardwizard", "herandislowjam2"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/herandislowjam2.html"
                ),
            ),
            (
                ("kinggizzardthelizardwizard", "timefate"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/timefate.html"
                ),
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
                ("https://www.azlyrics.com/lyrics/metallica/one.html"),
            ),
            (
                ("The Killers", "The Man"),
                ("https://www.azlyrics.com/lyrics/killers/theman.html"),
            ),
            (
                ("King Gizzard & the LizArd wizArd", "woRk-This-Time"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/workthistime.html"
                ),
            ),
            (
                ("King Gizzard &the LizArd wizArd", "Head on / Pill"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/headonpill.html"
                ),
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Danger $$$"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/danger.html"
                ),
            ),
            (
                ("King Gizzard & the LizArd wizArd", "Her And I (Slow Jam 2)"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/herandislowjam2.html"
                ),
            ),
            (
                ("King Gizzard & The Lizard Wizard", "TIme = Fate"),
                (
                    "https://www.azlyrics.com/lyrics/kinggizzardthelizardwizard/timefate.html"
                ),
            ),
        ],
    )
    def test_create_url_uncleaned(self, inp, exp):
        assert api._create_url(inp[0], inp[1]) == exp

    @pytest.mark.parametrize(
        ("inp"), [(("hello kitty", 0)), ((0, "hello kitty")), ((0, 0))]
    )
    def test_artist_wrong_type(self, inp):
        with pytest.raises(TypeError):
            api.get_lyrics(inp[0], inp[1])

    def test_get_page(self):
        test_url = api.AZ_LYRICS.format("bluj", "b;ak")
        r = api._get_page(test_url)
        assert r == "Lyrics not found"

    def test_get_lyrics_incorrect_song(self):
        lyr = api.get_lyrics(
            "King Gizzard & The lizard wizard", "Enter sandman")
        assert len(lyr) == 0

    def test_get_lyrics_incorrect_artist(self):
        lyr = api.get_lyrics("King Gizzard & lizard wizard", "Danger $$$")
        assert len(lyr) == 0

    @pytest.mark.parametrize(
        ("inp"),
        [
            (("Metallica", "One")),
            (("The Killers", "The Man")),
            (("King Gizzard & the LizArd wizArd", "woRk-This-Time")),
            (("King Gizzard &the LizArd wizArd", "Head on / Pill")),
            (("King Gizzard & the LizArd wizArd", "Danger $$$")),
            (("King Gizzard & the LizArd wizArd", "Her And I (Slow Jam 2)")),
            (("King Gizzard & The Lizard Wizard", "TIme = Fate")),
        ],
    )
    def test_get_lyrics(self, inp):
        lyr = api.get_lyrics(inp[0], inp[1])
        assert len(lyr) > 1

    @pytest.mark.parametrize(
        ("inp"), [(0), ("you take my breath aaway"), (tuple([0, 1, 2, 3]))]
    )
    def test_pretty_print_incorrect_type(self, inp):
        with pytest.raises(TypeError):
            api.pretty_print_lyrics(inp)
