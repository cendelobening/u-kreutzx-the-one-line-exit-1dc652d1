# u-kreutzx-the-one-line-exit-1dc652d1

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cendelobening/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cendelobening/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

A one-line resignation letter for "The One-Line Exit": a short, funny letter a person could actually send, with the punchline landing at the very end. The whole letter is a single line of 136 characters:

> Dear Boss, I hereby resign — I came for the dream job, stayed for the free snacks, and I'm leaving because someone ate the last biscuit.

`main.py` validates the line (1–140 characters, one line, no leading or trailing whitespace, no control characters), then writes it as UTF-8 with no trailing newline to `entry.txt` in the output directory, using an atomic rename and verifying the file back afterwards.

## Run it

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt` is written (default `/output`).

---

Built for [make.fun](https://make.fun/?ref=jme44qjv).
