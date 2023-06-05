{ pkgs ? import
    (
      let
        lock = builtins.fromJSON (builtins.readFile ./flake.lock);
      in
      builtins.fetchGit {
        name = "whisper-revision";
        url = "https://github.com/NixOS/nixpkgs/";
        ref = "refs/heads/nixos-unstable";
        rev = "${lock.nodes.nixpkgs.locked.rev}";
      }
    )
    {
      config = { };
    }
}:
let
  python-with-packages = pkgs.python3.withPackages
    (p: with p; [
    ] ++
    # only needed for development
    [
      autopep8
      pytest
    ]);
in
pkgs.mkShell
{

  buildInputs = with pkgs;[
    # only needed for development
    nixpkgs-fmt
    pre-commit

    fio
    python-with-packages
  ];

  shellHook = ''
    export PYTHONPATH=${python-with-packages}/${python-with-packages.sitePackages}
    echo ${python-with-packages}
    echo "PYTHONPATH=$PYTHONPATH"
  '';

}
