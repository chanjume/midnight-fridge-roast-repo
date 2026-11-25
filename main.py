#!/usr/bin/env python3
"""Midnight Fridge Roast: write one roast line to /output/entry.txt.

Craft: one concrete time (12:03 a.m.), one named person (Dave), one quoted
refusal, and a single surprise turn — the fridge as a bouncer, with the
leftovers themselves filing a restraining order. The petty midnight rule
is the target, not generic smart-home grumbling.
"""
import os

ENTRY = 'At 12:03 a.m. my fridge turned bouncer: "Not tonight, Dave — the leftovers filed a restraining order."'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
