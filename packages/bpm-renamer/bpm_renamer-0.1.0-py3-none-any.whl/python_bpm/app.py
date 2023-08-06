from python_bpm.bpm_detection import get_bpm
import sys
import os
import os.path


def run():
    full_path = os.path.realpath(sys.argv[1])
    base = os.path.basename(full_path)
    dirn = os.path.dirname(full_path)
    bpm = get_bpm(full_path)

    new_base = f"{bpm:.0f}BPM - {base}"
    new_full = os.path.join(dirn, new_base)

    os.rename(full_path, new_full)
