import os
from typing import Literal


class Command:
    def __init__(self, type: Literal["write", "read", "readwrite"], name: str = "fio_test", ramp_time: int = 4, size: str = "4G", bs: str = "4M"):
        self.type = type
        self.name = name
        self.ramp_time = ramp_time
        self.size = size
        self.bs = bs

    def ARGS(self):
        """
        get args for fio
        """
        return f"--readwrite={self.type} --bs={self.bs} --size={self.size} --ramp_time={self.ramp_time} --name=tmp/{self.name} --output-format=json --output=out/{self.name}-{self.type}-{self.bs}-{self.size}.json"

    def fio_path(self):
        """
        get fio path from system
        """
        return os.popen("which fio").read().replace("\n", "")

    def run(self):
        """
        run fio
        """

        if not os.path.exists("tmp/"):
            os.mkdir("tmp/")

        if not os.path.exists("out/"):
            os.mkdir("out/")

        result = os.popen(f"{self.fio_path()} {self.ARGS()}").read()

        # delete all files in tmp/
        for file in os.listdir("tmp/"):
            os.remove(f"tmp/{file}")

        return result
