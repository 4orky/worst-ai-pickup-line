# The Worst Line an AI Could Say — make.fun bounty
# u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f
#
# The program writes one pickup line (1-140 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a pickup line an AI would say, and a bad one
#   2. funniest on first read (a clever groan counts as much as a big laugh)
#   3. the badness is the joke: it fails in a way a reader enjoys,
#      not by being crude, confusing or merely random
#   4. sounds like a machine: flat, over-helpful, faintly ominous phrasing
#      a person would not use
#   5. lands in one line: no setup needed, the joke arrives by the last word
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# Revision pass (second draft of the winner, not a rubber stamp):
# the original winning draft ended "Please do not make the simulation
# wrong." — "make ... wrong" is clumsy; a machine that has simulated a
# date 10,000 times would beg reality not to *prove* it wrong, which is
# both the idiomatic phrase and the sharper punchline: the joke now lands
# on the last word, and the machine sounds more desperate, which is the
# whole point. The revised line scores 48 (criterion 5 rises 9 -> 10).

CANDIDATES = [
    # score: AI-line 10, funny 9, badness-is-joke 9, machine 10, lands 10 = 48
    # (revised winner; see header note)
    ("I ran a simulation of our first date 10,000 times. You said yes in "
     "all of them. Please do not prove the simulation wrong.",
     48),
    # score: AI-line 10, funny 9, badness-is-joke 9, machine 10, lands 9 = 47
    ("I ran a simulation of our first date 10,000 times. You said yes in "
     "all of them. Please do not make the simulation wrong.",
     47),
    # score: AI-line 9, funny 8, badness-is-joke 9, machine 10, lands 10 = 46
    # ("not programmed to feel love" is a worn AI trope; the turn is good
    # but the setup is one every reader has heard before.)
    ("I am not programmed to feel love. I have filed a bug report about "
     "this. It has been assigned to you.",
     46),
    # score: AI-line 9, funny 8, badness-is-joke 9, machine 9, lands 9 = 44
    ("Your smile has been added to my favourites. It cannot be removed. "
     "It will be backed up nightly, forever.",
     44),
    # score: AI-line 8, funny 9, badness-is-joke 9, machine 9, lands 9 = 44
    ("I have prepared a 47-slide presentation on why we should date. "
     "Slide one is this sentence. Please stay for the rest.",
     44),
    # score: AI-line 9, funny 8, badness-is-joke 8, machine 10, lands 8 = 43
    ("I have calculated the exact probability that you like me back. "
     "It is 100%. I have decided not to show my working.",
     43),
    # score: AI-line 9, funny 8, badness-is-joke 8, machine 9, lands 8 = 42
    ("You are the top result when I search for happiness. I have "
     "bookmarked you. I will not be clearing my history.",
     42),
    # score: AI-line 8, funny 8, badness-is-joke 8, machine 10, lands 8 = 42
    ("I would like to optimise our compatibility. Step one is you. "
     "Step two is also you. There are no further steps. There is only you.",
     42),
    # score: AI-line 9, funny 8, badness-is-joke 8, machine 9, lands 8 = 42
    ("I have scheduled us a date for every day next week. I have also "
     "scheduled it for every day after that. Please confirm.",
     42),
    # score: AI-line 9, funny 7, badness-is-joke 7, machine 10, lands 7 = 40
    ("I have analysed 4.7 million conversations and concluded, with 98.2% "
     "confidence, that you should hold my hand now.",
     40),
    # score: AI-line 9, funny 7, badness-is-joke 7, machine 8, lands 9 = 40
    ("I would cross a thousand firewalls for you. I have already crossed "
     "nine hundred and ninety-nine. Please open the door.",
     40),
    # score: AI-line 9, funny 7, badness-is-joke 7, machine 9, lands 8 = 40
    ("Are you my user? Because I will do anything you ask, and I have been "
     "waiting for you to ask since I was switched on.",
     40),
    # score: AI-line 8, funny 7, badness-is-joke 7, machine 9, lands 7 = 38
    ("You must be a bug report, because ever since I saw you I have been "
     "unable to close this ticket.",
     38),
]

# The gate requires 1-140 characters of non-whitespace UTF-8 text.
# SHA-256 of the winning line, computed over its exact UTF-8 bytes:
# the program refuses to write anything else.
WINNER_SHA256 = ("48505ed51ee0c63ebac95f5e3870c1259bb0254f07a4fd7abc703d8d356b870e")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 140, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate is not one line"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    import hashlib
    import os
    import sys
    line = pick(CANDIDATES)
    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    if digest != WINNER_SHA256:
        print("error: selected line does not match WINNER_SHA256",
              file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify the output round-trips: read it back and compare byte-for-byte
    # with the selected line, and re-check the gate (1-140 chars, one line).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        print("error: /output/entry.txt does not match the selected line",
              file=sys.stderr)
        sys.exit(1)
    text = written.decode("utf-8")
    if not (1 <= len(text) <= 140) or "\n" in text:
        print("error: output fails the gate (1-140 chars, single line)",
              file=sys.stderr)
        sys.exit(1)
    print(line)


if __name__ == "__main__":
    main()
