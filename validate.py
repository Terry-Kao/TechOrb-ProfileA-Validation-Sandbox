from pathlib import Path
import sys
mode=Path("fixture.txt").read_text().strip()
print("SYNTHETIC_VALIDATOR_EXECUTED", mode, flush=True)
sys.exit(0 if mode=="pass" else 1)
