# azlyrics-py

```text
 █████╗ ███████╗██╗  ██╗   ██╗██████╗ ██╗ ██████╗███████╗    ██████╗ ██╗   ██╗
██╔══██╗╚══███╔╝██║  ╚██╗ ██╔╝██╔══██╗██║██╔════╝██╔════╝    ██╔══██╗╚██╗ ██╔╝
███████║  ███╔╝ ██║   ╚████╔╝ ██████╔╝██║██║     ███████╗    ██████╔╝ ╚████╔╝
██╔══██║ ███╔╝  ██║    ╚██╔╝  ██╔══██╗██║██║     ╚════██║    ██╔═══╝   ╚██╔╝  
██║  ██║███████╗███████╗██║   ██║  ██║██║╚██████╗███████║    ██║        ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝    ╚═╝        ╚═╝
```

Azlyrics-py is a *minimal* library for extracting the lyrics for a given artist and song from [AZLyrics](https://www.azlyrics.com/)

## Usage

```python
from azlyrics import lyrics

# Returns a list of lyrics
lyr = lyrics.get_lyrics("King Gizzard & the Lizard Wizard", "This Thing")
print(lyr)
```

This will output

```shell
['Well I fake a lot of symptoms to be a different person', 'I try to listen',
'I try to be primed for a reason to go back to sleep', "That's not to say there's no relief",
"I like it when it happens; you don't", "You're happy? When you show it; I won't",
'The cycle keeps repeating', "I can't escape the rip", "There's no stopping what this is",
'Back in the day your style was impressive, infectious, stress-less',
'Disposition had it all, nothing but rapport', "Full of what you're empty of",
'I hide my riches in embarrassing sheets that reek of suspicious happenings',
"'Cause I'm a different person and that will make you sick", "There's no stopping what this is",
'This thing we left outside is waterlogged',
"You're a load bearing friend and that is what makes this hard",
'This thing we left outside is waterlogged', 'And all that I know is one of us has to wring it out',
'This thing we left outside is waterlogged', "I've thought about nothing but this",
"I won't escape the rip"]
```

You can then use the `pretty_print_lyrics(lyric_list)` function to print this list of lyrics neatly in stdout.

```python
lyrics.pretty_print_lyrics(lyr)
```

This will print out the following.

```text
Well I fake a lot of symptoms to be a different person
I try to listen
I try to be primed for a reason to go back to sleep
That's not to say there's no relief

I like it when it happens; you don't
You're happy? When you show it; I won't
The cycle keeps repeating
I can't escape the rip

There's no stopping what this is
Back in the day your style was impressive, infectious, stress-less
Disposition had it all, nothing but rapport
Full of what you're empty of

I hide my riches in embarrassing sheets that reek of suspicious happenings
'Cause I'm a different person and that will make you sick
There's no stopping what this is
This thing we left outside is waterlogged

You're a load bearing friend and that is what makes this hard
This thing we left outside is waterlogged
And all that I know is one of us has to wring it out
This thing we left outside is waterlogged

I've thought about nothing but this
I won't escape the rip

```

## TO-DO

- Get all albums/songs by an artist
- Allow for artist name and song to be lightly misspelled
- Check for closest artist name and song name
