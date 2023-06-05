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

    # this is just a example!
    # you can use this libary within your own scripts

    # we create a new fio_bench.Command objects
    # to collect a meaningful result, we always use size 8G
    # block sizes:
    # 4M for sequential
    # 8K for mixed
    # 4K for random

    commands = []

    for type in ["write", "read", "randread", "randwrite", "readwrite", "randrw"]:
        for blocksize in ["4M", "8K", "4K"]:
            commands.append(fio_bench.Command(
                type=type, size="8G", bs=blocksize)
            )

    for command in commands:
        command.run()
        # after each command, we wait 30 seconds
        # drives get slower when their caches are full
        # so we wait 60 seconds to let the drive cool down
        # each run should be done under the same conditions
        time.sleep(60)


if __name__ == "__main__":
    """
    When you run `python3 src/fio_bench/cli.py`, this block will be called.
    """

    main()
