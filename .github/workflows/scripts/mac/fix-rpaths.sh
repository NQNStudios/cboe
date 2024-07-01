#!/bin/sh -v

# add_rpath_to_app <app name>
add_rpath_to_app() {
    APP="$1.app/Contents/MacOS/$1"
    install_name_tool -add_rpath @loader_path/../Frameworks "$APP" 
}

# connect_dylib_in_app <app name> <system lib path> <lib name> <system lib version suffix> <bundled lib version suffix> 
connect_dylib_in_app() {
    APP="$1.app/Contents/MacOS/$1"
    FRAMEWORKS="$1.app/Contents/Frameworks"
    OLD_SUFFIX=${4:-""}
    if [ -n "$OLD_SUFFIX" ]; then
        OLD_SUFFIX=".${OLD_SUFFIX}"
    fi
    NEW_SUFFIX=${5:-""}
    if [ -n "$NEW_SUFFIX" ]; then
        NEW_SUFFIX=".${NEW_SUFFIX}"
    fi

    # Connect the executable to the bundled dylib:
    install_name_tool -change "$2/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$APP"
    # Connect the other dylibs to the bundled dylib
    # (This is a safe no-op for other dylibs which don't depend on this dylib
    # and in cases where the paths don't match exactly)
    install_name_tool -change "@rpath/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-window.2.6.1.dylib"
    install_name_tool -change "$2/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-window.2.6.1.dylib"
    install_name_tool -change "@rpath/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-audio.2.6.1.dylib"
    install_name_tool -change "$2/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-audio.2.6.1.dylib"
    install_name_tool -change "@rpath/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-graphics.2.6.1.dylib"
    install_name_tool -change "$2/$3$OLD_SUFFIX.dylib" "@rpath/$3$NEW_SUFFIX.dylib" "$FRAMEWORKS/libsfml-graphics.2.6.1.dylib"
}

# fix_app <app name>
fix_app() {
    if [ -e "$1.app" ]; then
        add_rpath_to_app "$1"
        connect_dylib_in_app "$1" /usr/local/opt/zlib/lib libz "1" "1.3.1"
        connect_dylib_in_app "$1" /usr/local/opt/boost/lib libboost_system
        connect_dylib_in_app "$1" /usr/local/opt/boost/lib libboost_filesystem
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-system "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-window "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-audio "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-graphics "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/freetype/lib libfreetype "6" "6"
        connect_dylib_in_app "$1" /usr/local/opt/flac/lib libFLAC "12" "12"
        connect_dylib_in_app "$1" /usr/local/opt/libogg/lib libogg "0" "0.8.5"
        connect_dylib_in_app "$1" /usr/local/opt/libvorbis/lib libvorbis "0" "0"
        connect_dylib_in_app "$1" /usr/local/opt/libvorbis/lib libvorbisenc "2" "2"
        connect_dylib_in_app "$1" /usr/local/opt/libvorbis/lib libvorbisfile "3" "3"
        connect_dylib_in_app "$1" /usr/local/opt/libpng/lib libpng16 "16" "16"
    fi
}

fix_app "Blades of Exile"
fix_app "BoE Scenario Editor"
fix_app "BoE Character Editor"
