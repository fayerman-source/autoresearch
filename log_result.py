#!/usr/bin/env python3
"""
Append a run summary to results.tsv from a captured training log.

Usage:
    python log_result.py --log run.log --status keep --description "baseline"
"""

import argparse
import os
import re
import subprocess
import sys


def extract(pattern, text, cast):
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        return None
    return cast(match.group(1))


def get_commit():
    return subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True,
    ).strip()


def main():
    parser = argparse.ArgumentParser(description="Append a run result to results.tsv")
    parser.add_argument("--log", default="run.log", help="Path to the run log")
    parser.add_argument("--results", default="results.tsv", help="Path to the TSV ledger")
    parser.add_argument("--status", required=True, choices=["keep", "discard", "crash"])
    parser.add_argument("--description", required=True, help="Short description of the experiment")
    args = parser.parse_args()

    with open(args.log, "r", encoding="utf-8") as f:
        text = f.read()

    val_bpb = extract(r"^val_bpb:\s+([0-9.]+)$", text, float)
    peak_vram_mb = extract(r"^peak_vram_mb:\s+([0-9.]+)$", text, float)

    if args.status == "crash":
        val_bpb = 0.0
        memory_gb = 0.0
    else:
        if val_bpb is None or peak_vram_mb is None:
            raise SystemExit("missing val_bpb or peak_vram_mb in log; use --status crash if the run failed")
        memory_gb = peak_vram_mb / 1024

    if not os.path.exists(args.results):
        with open(args.results, "w", encoding="utf-8") as f:
            f.write("commit\tval_bpb\tmemory_gb\tstatus\tdescription\n")

    row = f"{get_commit()}\t{val_bpb:.6f}\t{memory_gb:.1f}\t{args.status}\t{args.description}\n"
    with open(args.results, "a", encoding="utf-8") as f:
        f.write(row)

    sys.stdout.write(row)


if __name__ == "__main__":
    main()
