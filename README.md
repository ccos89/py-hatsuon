# py-hatsuon
 A port of DJTB/hatsuon to Python

## Purpose

A fairly faithful port of [Hatsuon](https://github.com/DJTB/hatsuon) from Javascript to Python.  When given a reading and a pitch number for a Japanese word, Hatsuon will return data about the pitch accent characteristics of that word and an array of numbers which can be used to easily create an SVG graph of the pitch accent.


## Usage

```
hatsuon('しょうちゅう', 3)
```
will return:

```
{'Reading': 'しょうちゅう', 'Morae': 4, 'Pitch Number': 3, 'Pitch Pattern': 'Nakadaka', 'Pitch Array': [0, 1, 1, 0, 0]}
```

I did this port for looping use in a larger project so right now there is no CLI usage.

There is always an extra digit at the end of the pitch array to indicate the position of a following particle.

## Acknowledgement/License

Credit for original creation of Hatsuon goes to Duncan Bay.  Hatsuon is licensed under the MIT License.

This software is licensed under the MIT License, so feel free to use it however you want.