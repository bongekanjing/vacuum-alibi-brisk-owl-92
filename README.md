# vacuum-alibi-brisk-owl-92

A single robot-vacuum alibi, written by a program to `/output/entry.txt`.

[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/bongekanjing/vacuum-alibi-brisk-owl-92/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/bongekanjing/vacuum-alibi-brisk-owl-92/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Bounty page: <https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7>

## The entry

`main.py` holds the line and writes it to `/output/entry.txt` unchanged. Before
it writes, it checks the three things the gate refuses: more than 200
characters, white space only, and a stray line break or non-UTF-8 byte.

## Run it

```
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

## Licence

MIT. See `LICENSE`.
