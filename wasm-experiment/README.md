# Porting Classic Blades of Exile to WebAssembly


Install the Emscripten SDK. First, follow the platform-specific instructions for your operating system here: https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html

Then run `source ./activate-em.sh`

## Process

My first instinct is to cut the project into manageable chunks. I'm going to start by making sure the various dependencies (other than SFML) can be compiled with Emscripten, and from there, maybe trying to run the unit tests in the browser.

### Building Boost with Emscripten

https://stackoverflow.com/questions/15724357/using-boost-with-emscripten


