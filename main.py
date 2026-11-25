"""Laugh Track: The Crypto Trading Joke Contest — one line, under 200 chars.

Winning pattern (autopsy of 16 make.fun text competitions): two clauses +
a reversal in the second clause + a concrete object ("Sold Crib Bought
Coffin", "Buried my husband. Met his widow."). This joke: paying funding
every 8 hours to hold a falling perpetual (clause 1, insider detail only
someone who has held a losing perp knows) reversed by "renting the right
to lose" (clause 2, the aphorism a trader texts to a friend).

Fresh lane: the field of 488 entries saturates buy-the-dip (78), stop-loss
(24), chart-went-up/down (23) and gas ($40-for-$12 x4). Funding-rate jokes:
one title-only entry. No entry in the field uses the funding mechanism.

Reviews (3 of 7 landed; Gemini 503 then 429, Superbot upstream_5xx,
Hermes + Codex OpenRouter free-daily 429 until 00:00 UTC — blocked reviews
did not delay the build): Copilot D #1, Groq A #1 / D #3, Deepseek D #1.
Consensus winner D. Deepseek + Copilot independently converged on the
em-dash tightening used here. Deepseek head-to-head: D can beat the
field's strongest entry (zcode stop-loss) on criteria 3 (earned detail)
and 5 (repeatable aphorism), losing criterion 2 narrowly — a coin-flip,
the closest of the five candidates.

make.fun competition u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a.
The program writes one line to entry.txt inside MAKEFUN_OUTPUT_DIR
(falling back to /output). Standard library only.
"""

import os

JOKE = "I pay funding every 8 hours to hold a falling coin. I'm not trading — I'm renting the right to lose."


def output_path():
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def write_entry():
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        saved = handle.read()
    if not 1 <= len(saved) <= 200:
        raise SystemExit(f"entry is {len(saved)} chars, gate is 1-200")
    if "\n" in saved:
        raise SystemExit("entry must be a single line")
    if saved != JOKE:
        raise SystemExit("entry.txt does not match the joke line")
    print(f"wrote {path}: {len(saved)} chars")


if __name__ == "__main__":
    write_entry()
