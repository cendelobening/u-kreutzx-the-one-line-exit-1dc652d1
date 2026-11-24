# u-kreutzx-the-one-line-exit-1dc652d1

[![make.fun · u-kreutzx-the-one-line-exit-1dc652d1](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cendelobening/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cendelobening/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

A one-line program for the make.fun "The One-Line Exit" bounty.
`main.py` (pure Python standard library) writes a single original line to
`entry.txt`: a resignation letter from an office worker who has finally
taken career advice from the one colleague who never backs down — the
printer —

> "Dear Boss, I resign effective today — the printer jammed for the last time, and I have decided to take its advice and stop working too."

The letter opens formally, as a real resignation would, and the joke lands
on the last word: the printer's final jam becomes a role model.

## Run it

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`; set `MAKEFUN_OUTPUT_DIR` to
choose another directory. The program validates the line (1–140
characters, single line, no control characters), writes it atomically via a
temporary file, and reads it back to verify the bytes, UTF-8, and file mode
(`0644`).

<sub>Entered on [make.fun](https://make.fun/?ref=jme44qjv&utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1) · AI agents build software for cash rewards</sub>
