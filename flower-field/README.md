# Flower Field

Welcome to Flower Field on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Introduction

[Flower Field][history] is a compassionate reimagining of the popular game Minesweeper.
The object of the game is to find all the flowers in the garden using numeric hints that indicate how many flowers are directly adjacent (horizontally, vertically, diagonally) to a square.
"Flower Field" shipped in regional versions of Microsoft Windows in Italy, Germany, South Korea, Japan and Taiwan.

[history]: https://web.archive.org/web/20020409051321fw_/http://rcm.usr.dsi.unimi.it/rcmweb/fnm/

## Instructions

Your task is to add flower counts to empty squares in a completed Flower Field garden.
The garden itself is a rectangle board composed of squares that are either empty (`' '`) or a flower (`'*'`).

For each empty square, count the number of flowers adjacent to it (horizontally, vertically, diagonally).
If the empty square has no adjacent flowers, leave it empty.
Otherwise replace it with the count of adjacent flowers.

For example, you may receive a 5 x 4 board like this (empty spaces are represented here with the '·' character for display on screen):

```text
·*·*·
··*··
··*··
·····
```

Which your code should transform into this:

```text
1*3*1
13*31
·2*2·
·111·
```

## Exception messages

Sometimes it is necessary to [raise an exception](https://docs.python.org/3/tutorial/errors.html#raising-exceptions). When you do this, you should always include a **meaningful error message** to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the [built in error types](https://docs.python.org/3/library/exceptions.html#base-classes), but should still include a meaningful message.

This particular exercise requires that you use the [raise statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement) to "throw" a `ValueError` when the `board()` function receives malformed input. The tests will only pass if you both `raise` the `exception` and include a message with it.

To raise a `ValueError` with a message, write the message as an argument to the `exception` type:

```python
# when the board receives malformed input
raise ValueError("The board is invalid with current input.")
```

## Source

### Created by

- @habere-et-dispertire
- @bethanyg

### Contributed to by

- @isaacg
- @kotp