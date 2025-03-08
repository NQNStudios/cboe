/*
 *  res_dialog.cpp
 *  BoE
 *
 *  Created by Celtic Minstrel on 20-01-07.
 *
 */

#include "res_dialog.hpp"
#include <iostream>
#include <fstream>
#include <boost/lexical_cast.hpp>

// Redeclare this instead of including "fileio.h"
extern std::ostream& std_fmterr(std::ostream& out);

class DialogLoader : public ResMgr::cLoader<DialogDefn> {
	/// Load a dialog definition from an XML file.
	DialogDefn* operator() (const fs::path& fpath) const override {
		return load_dialog_defn(fpath);
	}

	ResourceList expand(const std::string& name) const override {
		return {name + ".xml"};
	}

	std::string typeName() const override {
		return "dialog definition";
	}
};

DialogDefn* load_dialog_defn(const fs::path& fpath) {
	TiXmlBase::SetCondenseWhiteSpace(false);
	ticpp::Document xml(fpath.string().c_str());
	try {
		xml.LoadFile();
	} catch(ticpp::Exception& e) {
		std::cerr << "Error reading XML file: " << e.what();
		throw ResMgr::xError(ResMgr::ERR_LOAD, "Failed to load dialog: " + fpath.string());
	}
	// See if there are precalculated frames
	std::vector<rectangle> frames;
	fs::path layout_path = fpath;
	layout_path.replace_extension(".layout.xml");
	if(fs::exists(layout_path)){
		ticpp::Document layout_xml(layout_path.string().c_str());
		layout_xml.LoadFile();
		ticpp::Element* root = layout_xml.FirstChildElement();
		ticpp::Element* next_rect = root->FirstChildElement();
		while(next_rect != nullptr){
			frames.push_back(boost::lexical_cast<rectangle>(next_rect->GetText()));
			next_rect = next_rect->NextSiblingElement(false);
		}
	}

	return new DialogDefn{fpath.stem().string(), std::move(xml), frames};
}

// TODO: What's a good max dialogs count?
static DialogLoader loader;
ResMgr::cPool<DialogDefn> ResMgr::dialogs(loader, 80);
