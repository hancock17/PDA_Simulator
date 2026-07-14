PDA Simulator — a^n b^n

A small, dependency-free Python project that simulates a pushdown automaton (PDA) for recognizing strings in the language:
L = {a^n b^n | n >= 0}
For example, aabb is accepted, while aab, abb, and aba are rejected. The empty string is accepted because it represents the case where n = 0.

Requirements

Python 3.9 or later
No external dependencies

Usage

Test a single string:
python pda.py aabb

Run 
the built-in examples:
python pda.py
Run the automated tests:
python -m unittest -v

How It Works

The automaton pushes one marker onto the stack for every a.
It pops one marker from the stack for every b.
Once a b has been read, no further a characters are allowed.
The string is accepted only if the stack is empty at the end.

Project Structure

pda.py       PDA implementation and command-line interface
test_pda.py  Automated tests

License

This project is intended for educational use. Consider adding an MIT License before publishing it on GitHub.
