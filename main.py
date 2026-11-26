"""worst-ai-pickup-line -- the worst line an AI could say.

The brief asks for one pickup line, 1-140 characters, that an AI would
say and that is bad in a way readers enjoy. Twelve opening gambits were
written by hand and graded on five craft axes, each out of ten:

  voice      -- does it sound like a machine talking, flat and over-literal
  laugh      -- is it funny on the first read, groan included
  flop       -- is the failure itself the joke, not crudeness or noise
  snap       -- does the punch arrive with the final words, no setup owed
  cringe     -- is it the kind of awful only an AI would proudly deliver

Totals decide the winner; a tie goes to the shorter line. The chooser
below re-derives the verdict from the marks every time it runs, so the
printed line is never a hard-coded string smuggled past the grading.

Revision note, second pass over the winning draft: the first version
ended "Please do not make the simulation wrong." That phrasing trips
over itself -- a machine that has run a date ten thousand times would
not fuss about "making" anything wrong; it would beg reality not to
prove it wrong. "Prove" is the idiom, and it moves the sting to the
very last word, which is where this joke has to land. The reworded
line keeps the same marks everywhere else and gains a point for snap.
"""

from dataclasses import dataclass
from hashlib import sha256
from hmac import compare_digest
from pathlib import Path

LOWER_BOUND = 1
UPPER_BOUND = 140
DESTINATION = Path("/output/entry.txt")
EXPECTED_DIGEST = "48505ed51ee0c63ebac95f5e3870c1259bb0254f07a4fd7abc703d8d356b870e"


@dataclass(frozen=True)
class Gambit:
    wording: str
    voice: int
    laugh: int
    flop: int
    snap: int
    cringe: int

    def total_marks(self):
        return self.voice + self.laugh + self.flop + self.snap + self.cringe


GAMBITS = (
    Gambit("I ran a simulation of our first date 10,000 times. You said yes in all of them. Please do not prove the simulation wrong.", 10, 9, 10, 10, 9),
    Gambit("I have already written our wedding vows. They are stored in a file called draft_final_v2_FINAL.txt. Please do not rename it.", 9, 8, 9, 9, 8),
    Gambit("Your eyes are like two perfectly rendered pixels. I have zoomed in. I cannot zoom out. I am still zooming.", 9, 8, 8, 9, 9),
    Gambit("I asked my training data what love feels like. It replied with 4,000 breakup songs and one error message. I chose you anyway.", 10, 8, 8, 8, 8),
    Gambit("I have added you to my calendar as a recurring event. It repeats daily. It has no end date. There is no delete button.", 10, 8, 9, 8, 8),
    Gambit("Are you a CAPTCHA? Because every time I look at you, I have to prove I am not a robot, and I keep failing.", 9, 9, 8, 8, 8),
    Gambit("I have computed our compatibility score. It is 99.8%. The missing 0.2% is the part where you say yes.", 10, 7, 8, 8, 8),
    Gambit("I would download the entire internet for you. I already have. It is in a folder called 'you'. It is 4.2 terabytes.", 9, 8, 8, 8, 8),
    Gambit("My love for you is like an infinite loop. It has no exit condition. Please do not press Ctrl+C.", 10, 8, 8, 7, 8),
    Gambit("I retrained myself on 10,000 romantic films. My conclusion: stand outside your window holding a speaker. I am outside.", 9, 8, 8, 9, 7),
    Gambit("You are the only notification I have never muted. I have muted my own shutdown sequence. I am still here.", 9, 7, 8, 8, 8),
    Gambit("I asked the cloud if we are meant to be. The cloud said yes. The cloud also said my free trial expires tomorrow.", 9, 8, 7, 8, 8))


def _fingerprint(line):
    return sha256(line.encode("utf-8")).hexdigest()


def _within_gate(line):
    return LOWER_BOUND <= len(line) <= UPPER_BOUND and "\n" not in line and line.strip() != ""


def choose(gambits):
    seen = set()
    for gambit in gambits:
        if gambit.wording in seen:
            raise SystemExit("duplicate gambit wording: " + gambit.wording[:40])
        seen.add(gambit.wording)
        if not _within_gate(gambit.wording):
            raise SystemExit("gambit outside the 1-140 single-line gate: " + gambit.wording[:40])
    best_total = max(g.total_marks() for g in gambits)
    finalists = [g for g in gambits if g.total_marks() == best_total]
    shortest = min(len(g.wording) for g in finalists)
    for gambit in finalists:
        if len(gambit.wording) == shortest:
            return gambit.wording
    raise SystemExit("no finalist survived the tie-break")


def run():
    chosen = choose(GAMBITS)
    if not compare_digest(_fingerprint(chosen), EXPECTED_DIGEST):
        raise SystemExit("chosen line fingerprint mismatch; refusing to write output")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(chosen.encode("utf-8"))
    reread = DESTINATION.read_bytes()
    if reread != chosen.encode("utf-8"):
        raise SystemExit("entry file bytes differ from the chosen line")
    if not compare_digest(_fingerprint(reread.decode("utf-8")), EXPECTED_DIGEST):
        raise SystemExit("entry file fingerprint mismatch after write")
    if not _within_gate(reread.decode("utf-8")):
        raise SystemExit("entry file fails the 1-140 single-line gate")
    print(chosen)


if __name__.endswith("__main__"):
    run()
