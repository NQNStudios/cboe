with (import <nixpkgs> {});

mkShell {
	buildInputs = [
		ripgrep
		clang
		scons
		sfml
		boost
		zlib
		(import ./tgui.nix)
		gnome.zenity
		libGL
		xorg.libX11
	];
}
