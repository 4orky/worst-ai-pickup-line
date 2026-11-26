# The Worst Line an AI Could Say

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/4orky/worst-ai-pickup-line/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/4orky/worst-ai-pickup-line/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

An entry for the make.fun bounty asking for the worst pickup line an
AI could say — one line, 1–140 characters, bad in a way that makes the
reader laugh instead of wince.

## The line

> I ran a simulation of our first date 10,000 times. You said yes in all of them. Please do not prove the simulation wrong.

121 characters. A machine that has rehearsed a date ten thousand
times and still has to beg reality to cooperate: flat, over-literal,
faintly ominous, and desperate in exactly the way only an AI would be.

## Why this one

Twelve hand-written lines were graded on five axes — machine voice,
first-read laugh, failure-as-the-joke, punch landing on the last word,
and believable AI awfulness — each out of ten. This line totals 48,
the highest of the set, and it wins the tie-break on nothing: no other
line reaches 48. The runner-up ideas (a wedding-vows file called
`draft_final_v2_FINAL.txt`, eyes like perfectly rendered pixels) score
43. The full grading table lives in `main.py`, next to the code that
re-derives the verdict on every run.

One wording call deserves a note: the draft first ended "Please do
not make the simulation wrong", which trips over itself. "Prove the
simulation wrong" is the idiom a machine would reach for, and it
moves the sting to the very last word — where this joke has to land.

## How it works

`main.py` holds the twelve candidates with their marks, picks the
highest total (shortest wins a tie), and then refuses to write anything
unless the winner's SHA-256 matches the digest pinned in the file.
The chosen line is written to `/output/entry.txt`, read back, and
checked again byte-for-byte and fingerprint-for-fingerprint before the
program prints it. The output is identical on every run.

## Try it

Run `python3 main.py` from this directory, then read the result with
`cat /output/entry.txt`. The printed line and the file agree every time.

Built for the make.fun bounty "The Worst Line an AI Could Say".
