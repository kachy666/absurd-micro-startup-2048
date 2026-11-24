#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry: one sentence, under 200 chars.

The pitch: a bot that chases unpaid invoices for freelance illustrators
on a 10% contingency fee, because a bot sending gentle reminder #14 at
3 a.m. never gets embarrassed.
"""

ENTRY = "We chase $250 unpaid invoices for freelance illustrators, keeping 10% of every invoice paid, because a bot sending gentle reminder #14 at 3 a.m. never gets embarrassed."

def main():
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
