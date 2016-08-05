# QuickQuiz-Text

QuickQuiz is a simple to use text based flash card program. It's job is to get you studying your flash cards as fast as possible with as little hassle as possible. It runs from the command prompt and takes one or more simple text files as input.


## Why?

Why yet another flash card program? Because I just want to take bloody my notes and start studying. No fussing about with accounts, no awkward data entry screens, no confusing UIs! Just get on with it! And I want to do this where my notes are... on my computer!

There may be an app out there that gets it right. But if there is, I haven't found it. Most flash card apps are awkward and cumbersome to use. From complicated UIs to slow data entry screens, they just get in the way. Some apps do allow you to enter cards through excel files or word documents but they usually have some other major problem. Others have reasonably good data entry screens but then they hamstring you by requiring you to create an account on some website. Some only work online or on your phone.

So tired of all that mess, I created my own.


## Installing / Running

Step 1: Install Python 3
Step 2: Download QuickQuiz.egg
Step 3: Create a text file with your notes (see below)
Step 4: Run from the command line or terminal (see Run Command below)

## Run Command

python3 QuickQuiz.egg datafile1.txt [ datafile2.txt ... ]


## Data file format

The format of the text file is simple. A blank line indicates the split between flash cards and the first line of the card is the title.


Example:

```Card 1 Title
This is the description that will be displayed for the first card.

Card 2 Title
This is the content of the second card.
This is the second line of the second card.

Card 3 Title
And so on and so on.
```
