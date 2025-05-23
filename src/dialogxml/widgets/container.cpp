/*
 *  container.cpp
 *  BoE
 *
 *  Created by Celtic Minstrel on 2020-12-21.
 *
 */

#include "container.hpp"
#include "dialogxml/dialogs/dialog.hpp"
#include "dialogxml/widgets/button.hpp"
#include "dialogxml/widgets/field.hpp"
#include "dialogxml/widgets/ledgroup.hpp"
#include "dialogxml/widgets/line.hpp"
#include "dialogxml/widgets/message.hpp"
#include "dialogxml/widgets/pict.hpp"
#include "dialogxml/widgets/scrollbar.hpp"
#include "replay.hpp"

std::string cContainer::generateId(const std::string& explicitId) const {
	return explicitId.empty() ? generateRandomString() : explicitId;
}

bool cContainer::parseChildControl(ticpp::Element& elem, std::map<std::string,cControl*>& controls, std::string& id, std::string fname) {
	ctrlIter inserted;
	std::string tag = elem.Value();
	if(tag == "field") {
		auto field = getDialog()->parse<cTextField>(elem, *this);
		inserted = controls.insert(field).first;
		getDialog()->tabOrder.push_back(field);
		id = field.first;
	} else if(tag == "text") {
		auto text = getDialog()->parse<cTextMsg>(elem, *this);
		inserted = controls.insert(text).first;
		id = text.first;
	} else if(tag == "pict") {
		auto pict = getDialog()->parse<cPict>(elem, *this);
		inserted = controls.insert(pict).first;
		id = pict.first;
	} else if(tag == "slider") {
		auto slide = getDialog()->parse<cScrollbar>(elem, *this);
		inserted = controls.insert(slide).first;
		id = slide.first;
	} else if(tag == "button") {
		auto button = getDialog()->parse<cButton>(elem, *this);
		inserted = controls.insert(button).first;
		id = button.first;
	} else if(tag == "led") {
		auto led = getDialog()->parse<cLed>(elem, *this);
		inserted = controls.insert(led).first;
		id = led.first;
	} else if(tag == "line") {
		auto line = getDialog()->parse<cConnector>(elem, *this);
		inserted = controls.insert(line).first;
		id = line.first;
	} else if(tag == "group") {
		auto group = getDialog()->parse<cLedGroup>(elem, *this);
		inserted = controls.insert(group).first;
		id = group.first;
	} else return false;
	if(prevCtrl.second) {
		if(inserted->second->anchor == "$$prev$$" && prevCtrl.second->anchor == "$$next$$") {
			throw xBadVal(tag, "anchor", "<circular dependency>", elem.Row(), elem.Column(), fname);
		} else if(inserted->second->anchor == "$$prev$$") {
			inserted->second->anchor = prevCtrl.first;
		} else if(prevCtrl.second->anchor == "$$next$$") {
			prevCtrl.second->anchor = inserted->first;
		}
	}
	prevCtrl = *inserted;
	return true;
}

bool cContainer::handleClick(location where, cFramerateLimiter& fps_limiter) {
	std::string which_clicked;
	bool success = false;
	forEach([&](std::string id, cControl& ctrl) {
		if(!success && ctrl.isClickable() && ctrl.getBounds().contains(where)) {
			if(ctrl.handleClick(where, fps_limiter)){
				success = true;
				which_clicked = id;
			}
		}
	});
	if(!which_clicked.empty())
		clicking = which_clicked;
	return success;
}

void cContainer::callHandler(event_fcn<EVT_CLICK>::type onClick, cDialog& me, std::string id, eKeyMod mods) {
	// When replaying, a click event for the specifically child control comes next
	if(replaying){
		auto child_click_action = pop_next_action("click_control");
		auto info = info_from_action(child_click_action);
		clicking = info["id"];
	}
	std::string which_clicked = clicking;
	clicking = "";
	
	if(onClick) onClick(me, id, mods);
	if(!which_clicked.empty())
		getChild(which_clicked).triggerClickHandler(me, which_clicked, mods);
}

void cContainer::validatePostParse(ticpp::Element& who, std::string fname, const std::set<std::string>& attrs, const std::multiset<std::string>& nodes) {
	cControl::validatePostParse(who, fname, attrs, nodes);
	if(!anchor.empty()) return;
	bool allResolved = true;
	forEach([&allResolved](std::string, cControl& ctrl) {
		if(!ctrl.anchor.empty()) allResolved = false;
	});
	if(allResolved) postChildrenResolve();
}
