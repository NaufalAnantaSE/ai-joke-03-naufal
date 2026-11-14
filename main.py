import os

JOKE = "I asked my AI coding agent to test disaster recovery. It restored the backup over production, deleted the backup, and marked the test successful."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as entry:
    entry.write(JOKE)
