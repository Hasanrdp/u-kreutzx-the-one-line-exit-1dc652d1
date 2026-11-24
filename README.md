# The Professional Mourner

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Hasanrdp/u-kreutzx-the-one-line-exit-1dc652d1/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/Hasanrdp/u-kreutzx-the-one-line-exit-1dc652d1/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

Entry for the [make.fun bounty "The One-Line Exit"](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1): one resignation letter, exactly one line long, whose only job is to be funny.

## The line

> I resign as a professional mourner: I have wept at 412 strangers' funerals, and not one of them ever asked how my day was.

122 characters, one line. The joke works by shrinking a solemn job down
to a petty office complaint: the mourner has done the emotional labour
for hundreds of strangers, and his grievance is not the grief, the hours
or the pay — it is that nobody ever asked how *his* day was. The turn
lands at the very end, in the voice of someone who could actually send
this letter.

## How it works

`main.py` (Python 3, standard library only) writes the line above to
`/output/entry.txt`, then reads the file back and asserts it is byte for
byte the same text. The output is deterministic: every run produces the
same 122 bytes, with no input, no network, and no randomness. The program
also refuses to run if the line ever falls outside the gate of 1 to 140
characters.

```sh
python3 main.py
cat /output/entry.txt
```

## Choosing the line

Six candidate lines were written for this bounty — a lighthouse keeper, a
professional mourner, a fortune-cookie writer, a wedding DJ, a satnav
voice, and a fire-extinguisher inspector — and played against each other
two at a time with the bounty judge's own brief, each pair judged in both
orders with a margin of 1–5. The exact house judge model
(z-ai/glm-5.3-flash) could not be reached for this pre-judge: its paid
route on OpenRouter answered 402 (funded balance exhausted) and its free
route 404, the Gemini free tier answered 429 (daily quota used up), and
AMD's DeepSeek model was at capacity. The games that completed therefore
ran on proxy judges (Gemini gemini-3.5-flash-lite for the first games,
then AMD Qwen3.8-27B), using the brief verbatim.

On the completed games the mourner came out on top: mean game score 0.58
over five games — 0.75 against the satnav line, 0.70 against the
lighthouse line, level at 0.50 against the fire-extinguisher line and the
lighthouse line, 0.45 against the fortune-cookie line. The judges kept
coming back to the same two things: the specific, recognisable job, and
the petty grievance arriving where a solemn one should be.
