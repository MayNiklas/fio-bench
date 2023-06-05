import os
import sys
import time

if __package__ is None and not hasattr(sys, "frozen"):
    import os.path

    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import fio_bench


def main():
    """
    When you run `python -m fio_bench`, this function will be called.
    """

    for z in ["4M", "1M", "4k"]:
        for i in ["read", "write", "readwrite"]:
            fio_bench.Command(i, bs=z).run()
            time.sleep(20)


if __name__ == "__main__":
    main()
