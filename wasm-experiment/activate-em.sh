# Fetch the latest registry of available tools.
emsdk/emsdk update

# Download and install the latest SDK tools.
emsdk/emsdk install latest

# Make the "latest" SDK "active" for the current user. (writes ~/.emscripten file)
emsdk/emsdk activate latest

# Activate PATH and other environment variables in the current terminal
source emsdk/emsdk_env.sh
