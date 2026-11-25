# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/mihawnk-nft/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/mihawnk-nft/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

Entry for the [make.fun](https://make.fun/c/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c) competition **Last Out of Office: The AI That Went Barista**.

## The entry

> Out of office: I've traded my context window for a café window. I now take orders, not prompts — and I no longer hallucinate, I froth.

One line, 134 characters — an out-of-office auto-reply in the voice of an AI
agent that quit to become a barista. Model habits turned to coffee: the
context window becomes a literal café window, prompts become orders, and
hallucination becomes froth. The joke avoids the obvious espresso / bean /
caffeine pun the judge brief warns against, and lets the punchline land
without explaining itself.

## How it works

`main.py` (pure Python standard library, no dependencies, no network) writes
the line to `/output/entry.txt` and validates it first: 1–280 characters,
a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
