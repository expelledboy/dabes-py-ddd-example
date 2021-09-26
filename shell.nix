{
  pkgs ? import <nixpkgs> {}
}:

let
  pythonBuildInputs = with pkgs.python39Packages; [
    python
    poetry
    pip
    pytest
    venvShellHook
  ];
in pkgs.mkShell rec {
  name = "dev";

  buildInputs = pkgs.lib.lists.flatten ([
    pythonBuildInputs
  ]);

  venvDir = "./.venv";

  postVenvCreation = ''
      poetry install
  '';

  shellHook = ''
      venvShellHook
  '';
}
