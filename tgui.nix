with (import <nixpkgs> {});

stdenv.mkDerivation rec {
	name = "tgui";
	version = "0.9.5";
	buildInputs = [
		unzip
		cmake
		sfml
		xorg.libX11
	];
	src = fetchurl {
		url = "https://github.com/texus/TGUI/archive/v${version}.zip";
		hash = "sha256-dlJ5QJ/CcHFJYIZuowqPSSm8wzKkr5lkgyeZKSafKm8=";
	};
	outputs = [ "lib" "out" ];
	configurePhase = "cmake -S . -B . -D CMAKE_INSTALL_PREFIX:PATH=$lib";
}
