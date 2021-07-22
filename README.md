# Hangman Solver

1. [Basic usage](#basic-usage)
2. [Requirements](#requirements)
3. [Change log](#change-log)

> Ready to use with french dictionnary.

Project not compiled yet, maybe in the future. Also look for new folder organisation.

## Basic usage

Use the app running ``python main.py``. You will be asked to enter an input, which must be as following : current state of the game and then tested letters (for eg. ".a.e. aeiouls", without quotes but with a space). The programm will then compute all possible matching words taken in the provided text file. To use your own, please specify the new path in [main.py](main.py).

## Requirements

Obviously some distribution of ``python``, python 3 is mandatory, project is built with 3.9.6 but compatibility was made for 3.8.x versions (mainly by removing type hints). ``unidecode`` external library needed to deal with accents.

## Change log

* initial release
* changed dictionnary
* more user interraction
