{ lib
, buildPythonPackage

  # propagates
, fio
, typing-extensions
}:

buildPythonPackage rec {
  pname = "fio_bench";
  version = (lib.strings.removePrefix ''__version__ = "''
    (lib.strings.removeSuffix ''
      "
    ''
      (builtins.readFile ./src/fio_bench/version.py)));
  format = "setuptools";

  src = ./.;

  propagatedBuildInputs = [
    fio
    typing-extensions
  ];

  meta = with lib; {
    description = "A simple API for OpenAI's Whisper";
    homepage = "https://github.com/MayNiklas/fio_bench";
    maintainers = with maintainers; [ MayNiklas ];
  };

}
