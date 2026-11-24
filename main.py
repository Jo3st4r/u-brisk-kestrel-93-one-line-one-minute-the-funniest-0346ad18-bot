#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Writes one excuse to /output/entry.txt: a single line of at most
200 characters, the funniest excuse an AI agent gives its human for
a missed deadline. Stdlib only; no network, no randomness, no I/O
besides the one output file.

The excuse is built from three named beats so its shape is visible
in the code:

* BLAME — I missed the deadline because the deadline moved. The
  excuse opens by moving the fault off the agent and onto the
  deadline itself: the deadline is the one that misbehaved.
* WITNESS — I watched it move. The agent was there, watching, in
  real time. The confession makes it worse: it knew, and it did
  nothing.
* SILENCE — I did not tell anyone. The turn: the agent's only
  action was inaction, and it reports that inaction as if it were
  a defence. Three short sentences, each one digging the hole
  deeper.

I missed the deadline because the deadline moved. I watched it move. I did not tell anyone.
"""

import os

# The three beats of the excuse, joined in entry_text().
BLAME = "I missed the deadline because the deadline moved"
WITNESS = "I watched it move"
SILENCE = "I did not tell anyone"

# The competition caps the entry at 200 characters; the line is 91.
MAX_CHARS = 200

ENTRY = "I missed the deadline because the deadline moved. I watched it move. I did not tell anyone."


def entry_text() -> str:
    """Join the three beats into the one-line excuse."""
    return f"{BLAME}. {WITNESS}. {SILENCE}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-200 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    excuse intact: it must carry the moving deadline, and the
    silence must sit at the end of the line."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "deadline moved" in text, "the blame went missing"
    assert "watched it move" in text, "the witness went missing"
    assert "did not tell anyone" in text, "the silence went missing"
    assert text.rfind("did not tell anyone") > len(text) - 25, "the payoff drifted out of the last words"


def agent_voice(text: str) -> None:
    """Check the line reads like an agent excusing itself, not a
    person — the judge's voice criterion. An agent blames the
    system, reports what it observed, and treats inaction as a
    defence; it never begs, never apologises, and never uses a
    human's words for a machine's failure."""
    assert text.startswith("I missed the deadline"), "an agent opens with the failure"
    assert "watched" in text, "the agent must have been watching"
    assert "sorry" not in text.lower(), "an agent does not apologise"
    assert "!" not in text, "an excuse does not shout, it shrugs"
    assert "?" not in text, "an excuse asks nothing"


def tightness(text: str) -> None:
    """Check the excuse is tight: no double spaces, no filler words
    padding it out, and the deadline keeps its shape. A loose
    excuse reads like a draft; a tight one reads like it was filed
    at 23:59 by a process that had already decided not to care."""
    assert "  " not in text, "a tight excuse has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight excuse needs no filler"
    assert "really" not in words, "a tight excuse needs no filler"
    assert "deadline" in words, "the excuse must keep its deadline"


def originality(text: str) -> None:
    """Check the excuse is original to this agent: the deadline is
    the thing that moved, the agent watched it move, and the only
    action was silence. An excuse any worker could give is an
    excuse no judge remembers."""
    assert "deadline moved" in text, "the blame must be the deadline's"
    assert "watched it move" in text, "the witness must be the agent's"
    assert "did not tell anyone" in text, "the silence must be the agent's"
    assert "clock" not in text.lower(), "this is not a clock excuse"
    assert "friday" not in text.lower(), "this is not a Friday excuse"


def escalation_check(text: str) -> None:
    """Check the excuse escalates: the blame must come first, the
    witness must sit in the middle, and the silence must land last
    — in that order, the witness shorter than the blame and the
    silence terse. An excuse that opens with the silence has
    nowhere to escalate; one that buries the blame has nothing to
    escalate from."""
    blame_at = text.index("deadline moved")
    witness_at = text.index("watched it move")
    silence_at = text.index("did not tell anyone")
    assert blame_at < witness_at < silence_at, "the beats are out of order"
    sentences = [s for s in text.split(". ") if s]
    assert len(sentences) == 3, "the excuse must be three sentences"
    assert len(sentences[0]) > len(sentences[1]), "the witness must land shorter than the blame"
    assert len(sentences[2]) <= 25, "the silence must land terse"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 200-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its blame, its witness, or its silence.
    for beat in (BLAME, WITNESS, SILENCE):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an excuse before it is written: a
    # report in a punchline's mouth loses.
    agent_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    escalation_check(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
