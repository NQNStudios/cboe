#! /bin/bash

if [ -z "$CONFIGURATION" ]; then
    CONFIGURATION=Release
fi

INTEL=cboe-macos-intel-$CONFIGURATION
SILICON=cboe-macos-silicon-$CONFIGURATION

mkdir "build/Blades of Exile"

combine() {
    mkdir -p "build/Blades of Exile/$1.app/Contents/MacOS"
    lipo -create "$SILICON/Blades of Exile/$1.app/Contents/MacOS/$1" "$INTEL/Blades of Exile/$1.app/Contents/MacOS/$1" -output "build/Blades of Exile/$1.app/Contents/MacOS"
    cp -r "$SILICON/Blades of Exile/$1.app/Contents/Frameworks" "build/Blades of Exile/$1.app/Contents/"
    cp -r "$SILICON/Blades of Exile/$1.app/Contents/Resources" "build/Blades of Exile/$1.app/Contents/"
    cp "$SILICON/Blades of Exile/$1.app/Contents/Info.plist" "build/Blades of Exile/$1.app/Contents/"
    cp "$SILICON/Blades of Exile/$1.app/Contents/PkgInfo" "build/Blades of Exile/$1.app/Contents/"
}

combine "Blades of Exile"
combine "BoE Scenario Editor"
combine "BoE Character Editor"