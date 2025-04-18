#include "winutil.hpp"

#include <boost/filesystem/operations.hpp>
#include "keymods.hpp"

// The default scale should be the largest that the user's screen can fit all three
// BoE application windows (because they should probably default to match each other).
double fallback_scale() {
	static double scale = 0;
	// Suppress the float comparison warning.
	// We know it's safe here - we're just comparing static values.
	#ifdef __GNUC__
	#pragma GCC diagnostic push
	#pragma GCC diagnostic ignored "-Wfloat-equal"
	#endif
	if(scale == 0){
		sf::VideoMode desktop = sf::VideoMode::getDesktopMode();

		short max_width = max(boe_width, max(pc_width, scen_width));
		short max_height = max(boe_height, max(pc_height, scen_height)) + getMenubarHeight();

		std::vector<double> scale_options = {1.0, 1.5, 2.0, 3.0, 4.0};
		for(auto it = scale_options.rbegin(); it != scale_options.rend(); ++it){
			short max_scaled_width = max_width * (*it);
			short max_scaled_height = max_height * (*it);

			if(max_scaled_width <= desktop.width && max_scaled_height <= desktop.height){
				scale = (*it);
				break;
			}
		}
	}
	// Hopefully no one would ever have such a small monitor to not fit the default size.
	// But just in case:
	if(scale == 0){
		scale = 1.0;
	}
	#ifdef __GNUC__
	#pragma GCC diagnostic pop
	#endif

	return scale;
}

// We use many nested event loops in this codebase. Each one of them
// calls pollEvent() and they each need to remember to call handleModifier()
// or else modifier keys will claim to be held forever.
// The best solution for this is to wrap pollEvent() so that it calls
// handleModifier for us every time.
bool pollEvent(sf::Window& win, sf::Event& event){
    if(win.pollEvent(event)) {
        if(kb.handleModifier(event)) return false;
        return true;
    }

    return false;
}

bool pollEvent(sf::Window* win, sf::Event& event){
    return pollEvent(*win, event);
}

extern fs::path progDir;

void launchDocs(std::string relative_url) {
	if(fs::is_directory(progDir/"doc")){
		launchURL("file://" + (progDir/"doc"/relative_url).string());
	}else{
		launchURL("http://openboe.com/docs/" + relative_url);
	}
}
