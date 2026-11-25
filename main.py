"""Writes one roast of a daily gadget to /output/entry.txt."""
import os

TEXT = "My robot vacuum has mapped every room, learned my routine, and still eats the same charging cable every single Tuesday."

# Rule: the roast must be a single line of 1 to 200 characters.
# The joke lands on a specific gripe: a vacuum smart enough to map the
# flat, dumb enough to eat the same cable every Tuesday.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
