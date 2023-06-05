# fio-bench

## Usage

This runs the default benchmark!
The results will be stored in json files in the `out/` directory.
You can also run your own benchmarks arround the `class` `fio_bench.object.Command`.

### NixOS

This repository provides a `flake.nix` file.

```sh
nix run 'github:MayNiklas/fio-bench'
```

### Other Linux distributions

1. make sure you have `fio` installed
2. make sure you have `python3` installed

```sh
git clone https://github.com/MayNiklas/fio-bench.git
cd fio-bench
python3 src/fio_bench/cli.py
```
