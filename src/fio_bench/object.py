import json
import os
from typing import Literal


class Command:
    def __init__(self, type: Literal["write", "read", "readwrite"], name: str = "fio_test", ramp_time: int = 4, size: str = "4G", bs: str = "4M"):
        """
        A class containing the fio command.
        Parameters:
            type: Literal["write", "read", "readwrite"]
                the type of the fio command
            name: str
                the name of the fio command
            ramp_time: int
                the ramp time of the fio command
            size: str
                the size of the fio command
            bs: str
                the block size of the fio command
        """

        self.type = type
        self.name = name
        self.ramp_time = ramp_time
        self.size = size
        self.bs = bs

    def ARGS(self):
        """
        Returns argument string for fio.
        Does not include the fio path.
        """
        return f"--readwrite={self.type} --bs={self.bs} --size={self.size} --ramp_time={self.ramp_time} --name=tmp/{self.name} --output-format=json --output=out/{self.name}-{self.type}-{self.bs}-{self.size}.json"

    def fio_path(self):
        """
        Returns the path to the fio binary.
        """

        if (path := os.popen("which fio").read().replace("\n", "")) == "":
            raise Exception("fio is not installed. Please install fio.")

        return path

    def run(self) -> json:
        """
        Run the fio command.
        Returns the json output of the fio command.
        """

        # the out/ directory is needed to store the results
        if not os.path.exists("out/"):
            os.mkdir("out/")

        # the tmp/ directory is needed to store the temporary test files
        if not os.path.exists("tmp/"):
            os.mkdir("tmp/")

        # run the fio command and store the output in result
        result = os.popen(f"{self.fio_path()} {self.ARGS()}").read()

        # after running the command, remove the temporary test files
        # this is needed because fio does not remove them
        # and they would alter the results of the next run
        for file in os.listdir("tmp/"):
            os.remove(f"tmp/{file}")

        return result
