#! /bin/bash

# Pass any argument to make it a dry run (for putting at the start of your CI, to catch failure early)
test="${1}"

butler_channel=""
butler_exe=""
release_dir=""
if [ "$BUILD_OS" = "ubuntu" ]; then
    butler_channel=linux-amd64
    butler_exe=butler
    release_dir="linux"

    # TEMPORARY
    butler_exe=.github/workflows/scripts/linux/butler/butler
elif [ "$BUILD_OS" = "windows" ]; then
    butler_channel=windows-amd64
    butler_exe=butler.exe
    release_dir="windows"

    # TEMPORARY
    butler_exe=.github/workflows/scripts/win/butler/butler.exe
elif [ "$BUILD_OS" = "macos" ]; then
    butler_channel=darwin-amd64
    butler_exe=butler
    release_dir="macos"

    # TEMPORARY
    butler_exe=.github/workflows/scripts/mac/butler/butler
fi


# Butler download is disabled because something is wrong with the automated download links
## -L follows redirects
## -O specifies output name
# if [ ! -f ./${butler_exe} ]; then
#   curl -L -o butler.zip https://broth.itch.ovh/butler/${butler_channel}/LATEST/archive/default
#   unzip butler.zip
# fi

# GNU unzip tends to not set the executable bit even though it's set in the .zip
chmod +x ${butler_exe}
# just a sanity check run (and also helpful in case you're sharing CI logs)
./${butler_exe} -V

if [ -z "$test" ]; then
    ./${butler_exe} push "build/Blades of Exile/" nqn/blades-of-exile:${release_dir}
fi