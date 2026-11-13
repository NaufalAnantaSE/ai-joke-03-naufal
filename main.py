import os

JOKE = "My coding agent opened a PR to fix the outage, then marked it resolved when the outage stopped reproducing locally."

os.makedirs("/output", exist_ok=True)
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry:
    entry.write(JOKE)
