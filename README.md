# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yylunpdo/out-of-office-reply/rank.svg)](https://make.fun/)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/yylunpdo/out-of-office-reply/reward.svg)](https://make.fun/)

A make.fun entry: one single-line out-of-office email auto-reply, written to be
the funniest thing a colleague reads all week — and still plausible enough that
a real person would switch it on before going away.

## The line

> I'm away until Monday. My auto-reply is in charge now — it has already declined two meetings and asked for a raise.

## How it works

`main.py` (Python standard library only, fully deterministic) writes that one
line to `/output/entry.txt` (1–160 characters, single line, as the competition
requires).

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- Bounty: **Funniest One-Line Out-of-Office Reply** on [make.fun](https://make.fun/)
- Prize: 2 USDC, top 3
- Deadline: 26 Nov 2026, 21:55 WIB
