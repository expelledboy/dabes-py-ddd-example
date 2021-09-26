{
  pkgs ? import <nixpkgs> {}
}:

let
  pythonBuildInputs = with pkgs.python39Packages; [
    python
    poetry
    venvShellHook
  ];
in pkgs.mkShell rec {
  name = "dev";

  buildInputs = pkgs.lib.lists.flatten ([
    pythonBuildInputs
  ]);

  venvDir = "./.venv";

  # ENV
  VENV_DIR = venvDir;
  # https://python-poetry.org/docs/configuration/
  POETRY_VIRTUALENVS_CREATE = "true";
  POETRY_VIRTUALENVS_IN_PROJECT = "true";
  POETRY_VIRTUALENVS_PATH = venvDir;

  postVenvCreation = ''
    # Set SOURCE_DATE_EPOCH so that we can use python wheels.
    # This compromises immutability, but is what we need
    # to allow package installs from PyPI
    export SOURCE_DATE_EPOCH=$(date +%s)

    # Install python packages
    poetry install
  '';

  shellHook = ''
    venvShellHook
  '';
}
