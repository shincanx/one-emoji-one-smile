"""One Emoji, One Smile — entry program.

Writes exactly one emoji, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
bounty's RULES.txt requires. Deterministic: no randomness, no network,
no input files.

The emoji: a face holding back tears — a smile that is almost
overwhelmed by feeling. Warmer than a plain smile because it carries
real emotion: someone so moved they are about to cry, and still
smiling. The field is full of hugging faces, heart hands and
sunflowers; this one is the same warmth with a catch in its throat.
"""

import os

EMOJI = "🥹"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(f"wrote {path} ({len(EMOJI)} character)")


if __name__ == "__main__":
    main()
