//
//  dialogs.cpp
//  BoE
//
//  Created by Nat Nelson on 2023-01-06
//

#include "catch.hpp"
#include <boost/filesystem.hpp>
#include "dialogxml/dialogs/dialog.hpp"

TEST_CASE("Construct each type of dialog in the engine") {
    fs::path dialogsPath = fs::current_path()/".."/"Blades of Exile"/"data"/"dialogs";
	fs::directory_iterator it{dialogsPath};
	auto end = fs::directory_iterator{};
  	while (it != end) {
		std::string xmlFile = it->path().string();
		CAPTURE(xmlFile);
		xmlFile = xmlFile.replace(xmlFile.find(".xml", 0), 4, "");
		CHECK_NOTHROW(cDialog dialog(xmlFile, NULL, false));
		
		++it;
	}
}