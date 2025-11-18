# this config is reliant on cachix to avoid compiling the cuda packages
# install cachix and do cachix use nix-community and dont forget to import it in your configuration.nix
# Ultralytics sometimes doesn't find the dataset images because it has a different path by default. To fix this just
# go to .config/Ultralytics/settings.json and change the path by removing the datasets directory
{
  description = "Leetcode";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfree = true;
          # cudaSupport = true;
        };
      };

      python = pkgs.python312;

      pythonWithPackages = python.withPackages (ps:
        with ps; [
        ]);
    in {
      devShells.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python312Packages.python-lsp-server
          black
          pythonWithPackages
        ];
      };
    });
}
