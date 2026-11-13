import os

JOKE = "I asked my AI coding agent for a blameless postmortem. It rebased the incident onto my commit and opened a PR titled 'fix: assign blame.'"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry:
    entry.write(JOKE)
