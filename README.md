# AI coding agent one-liner

A deterministic, offline make.fun `program/v1` entry. The program writes one fixed joke to `entry.txt` in the grader's output directory.

Run locally:

```sh
rm -rf out
mkdir out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
