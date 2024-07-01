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
    # Connect the executable to the bundled dylib:
    install_name_tool -change "$2/$3.$4.dylib" "@rpath/$3.$5.dylib" "$APP"
    # Connect the other dylibs to the bundled dylib
    # (This is a safe no-op for other dylibs which don't depend on this dylib
    # and in cases where the paths don't match exactly)
    install_name_tool -change "@rpath/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-window.2.6.1.dylib"
    install_name_tool -change "$2/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-window.2.6.1.dylib"
    install_name_tool -change "@rpath/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-audio.2.6.1.dylib"
    install_name_tool -change "$2/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-audio.2.6.1.dylib"
    install_name_tool -change "@rpath/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-graphics.2.6.1.dylib"
    install_name_tool -change "$2/$3.$4.dylib" "@rpath/$3.$5.dylib" "$FRAMEWORKS/libsfml-graphics.2.6.1.dylib"
}

# fix_app <app name>
fix_app() {
    if [ -e "$1.app" ]; then
        add_rpath_to_app "$1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-system "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-window "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-audio "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/sfml/lib libsfml-graphics "2.6" "2.6.1"
        connect_dylib_in_app "$1" /usr/local/opt/freetype/lib libfreetype "6" "6"
    fi
}

fix_app "Blades of Exile"
fix_app "BoE Scenario Editor"
fix_app "BoE Character Editor"
