[![Coverage Status](https://coveralls.io/repos/github/is-gabs/rpgtk/badge.svg)](https://coveralls.io/github/is-gabs/rpgtk)

# RPGTK 

Role-Playing Game Toolkit is a platform for build Python RPG's systems.

## Installing
Install and update using [pip](https://pypi.org/project/rpgtk/):
```
$ pip install -U rpgtk
```

## A simple example
```python
# dice.py
from rpgtk import Dice

dice = Dice(sides=20)

dice.roll()

print(dice)
```
```bash
python dice.py
'D20[6]'
```

```python
# advantage roll
from rpgtk import Dice

dice = Dice(sides=20)

advantage_roll = max(dice * 2)

print(advantage_roll)
```
