from pathlib import Path
assert Path("fixture.txt").read_text().strip() in {"pass","fail","pending","cancel"}
print("SYNTHETIC_TEST_HARNESS_EXECUTED")
