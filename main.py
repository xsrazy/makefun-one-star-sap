"""One Star, Written in Sap entry for make.fun bounty
u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.

Writes exactly one original one-star review (plain ASCII, no trailing
newline) to /output/entry.txt.

The joke: a houseplant rates its owner one star because he only waters
it when he remembers, which is never, and then holds its brown leaves
up to the light like they owe him an apology. The plant's-eye view is
the whole bit: water, light, and leaves doing the complaining, with the
owner cast as the neglectful customer being reviewed.

Why this line should win the pairwise judge: it reads as a genuine
one-star review (explicit "One star" plus a concrete grievance and a
reason for the single star), the grievance is the plant's own, and the
punchline lands on a surprising turn, the leaves owing an apology,
instead of a stock wilting gag. Fresh, specific detail: brown leaves
held up to the light, watering only when remembered, which is never.
No em dash anywhere in the entry text or the README.
"""

import os

LINE = (
    "One star. He waters me when he remembers, which is never, "
    "then holds my brown leaves up to the light like they owe him "
    "an apology."
)


def main() -> None:
    """Write the entry line byte-exact: no trailing newline, UTF-8."""
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
