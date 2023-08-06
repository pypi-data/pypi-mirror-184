#!/usr/bin/env python3

import os
import pathlib
import argparse


def main(fdir_root):
    """Returns the yolo weights pt file that has the latest modification date."""
    fpaths = [str(path) for path in pathlib.Path(fdir_root).rglob('*') if path.suffix.lower() == ".pt"]
    # fpaths = [f for f in fpaths if f.endswith("last.pt")]
    latest_file = max(fpaths, key=os.path.getctime)  # find most recent one (relevant if multiple files)
    print("Badabing!")
    return latest_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Return path to the latest .pt file.")
    parser.add_argument("fpath", type=str, action="store")
    args = parser.parse_args()
    print(main(args.fpath))
