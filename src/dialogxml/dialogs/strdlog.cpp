/*
 *  dlogutil.cpp
 *  BoE
 *
 *  Created by Celtic Minstrel on 11/05/09.
 *
 */

#include "strdlog.hpp"

#include <sstream>
#include "tools/winutil.hpp"
#include "dialogxml/widgets/pict.hpp"
#include "fileio/resmgr/res_dialog.hpp"
#include "mathutil.hpp"
#include "utility.hpp"

// Pick a layout variant depending on number of strings, picture size, and whether a title is given
DialogDefn& cStrDlog::getDefn(short n_strs, ePicType type, bool hasTitle){
	std::ostringstream sout;
	sout << minmax(1, 2, n_strs) << "str";
	if(hasTitle) sout << "-title";
	if(type == PIC_DLOG_LG || type == PIC_CUSTOM_DLOG_LG || type == PIC_SCEN_LG)
		sout << "-lg";
	return *ResMgr::dialogs.get(sout.str());
}

// This uses a 1str- or 2str- layout variant depending on if one of the strings are empty
cStrDlog::cStrDlog(std::string str1,std::string str2,std::string title,pic_num_t pic,ePicType t,cDialog* parent)
	  : dlg(cStrDlog::getDefn((str1 != "") + (str2 != ""), t, title != ""), parent), type(t) {
	using namespace std::placeholders;
	cPict& pic_ctrl = dynamic_cast<cPict&>(dlg["pict"]);
	pic_ctrl.setPict(pic, type);
	if(str1 != "") {
		dlg["str1"].setText(str1);
		if(str2 != "") dlg["str2"].setText(str2);
	}else if(str2 != "") dlg["str1"].setText(str2);
	if(title != "") dlg["title"].setText(title);
	dlg["record"].hide();
	dlg["record"].attachClickHandler(std::bind(&cStrDlog::onRecord, this, _2));
	dlg["done"].attachClickHandler(std::bind(&cStrDlog::onDismiss, this));
}

bool cStrDlog::onRecord(std::string id){
	if(hasRecord) rec_f(dlg);
	else dlg[id].hide();
	return hasRecord;
}

bool cStrDlog::onDismiss(){
	dlg.toast(true);
	return true;
}

cStrDlog& cStrDlog::setSound(snd_num_t snd){
	sound = snd;
	return *this;
}

cStrDlog& cStrDlog::setRecordHandler(record_callback_t rec){
	if(rec == nullptr){
		hasRecord = false;
		dlg["record"].hide();
	}else{
		hasRecord = true;
		rec_f = rec;
		dlg["record"].show();
	}
	return *this;
}

cDialog* cStrDlog::operator->() {
	return &dlg;
}

void cStrDlog::show(){
	if(sound > 0) play_sound(sound);
	dlg.run();
}

static void giveError(pic_num_t pic, std::string title, std::string str1, std::string str2, cDialog* parent) {
	// If giveError() is called before UI is initialized, print to console
	if (!cDialog::wasInitCalled()) {
		std::cout << title << std::endl << str1 << std::endl << str2 << std::endl;
		return;
	}

	cStrDlog error(str1,str2,title,pic,PIC_DLOG,parent);
	error->getControl("record").setText("Copy");
	error.setRecordHandler([](cDialog& me) {
		std::string error = me["str1"].getText();
		try {
			std::string error2 = me["str2"].getText();
			error += "\n\n" + error2;
		} catch(std::invalid_argument) {}
		for(char& c : error) {
			if(c == '|') c = '\n';
		}
		set_clipboard(error);
	});
	error.show();
}

void showError(std::string str1, cDialog* parent) {
	showError(str1, "", parent);
}

void showError(std::string str1, std::string str2, cDialog* parent) {
	giveError(25, "Error", str1, str2, parent);
}

void showWarning(std::string str1, cDialog* parent) {
	showWarning(str1, "", parent);
}

void showWarning(std::string str1, std::string str2, cDialog* parent) {
	giveError(24, "Warning", str1, str2, parent);
}

void showFatalError(std::string str1, cDialog* parent) {
	showFatalError(str1, "", parent);
}

void showFatalError(std::string str1, std::string str2, cDialog* parent) {
	giveError(25, "Error!!!", str1, str2, parent);
}

// Call this anywhere, but don't forget parent!!!
static void give_help(short help1,short help2,cDialog* parent,bool help_forced) {
	std::string str1,str2;
	
	if(help_text_rsrc.empty()){
		throw std::string {"Tried to call give_help() without setting help_text_rsrc!"};
	}

	if(!help_forced && help_text_rsrc == "help" &&
		(!get_bool_pref("ShowInstantHelp", true) || get_iarray_pref_contains("ReceivedHelp", help1))){
		return;
	}
	append_iarray_pref("ReceivedHelp", help1);
	if(help2 != -1)
		append_iarray_pref("ReceivedHelp", help2);
	sync_prefs();
	str1 = get_str(help_text_rsrc,help1);
	if(help2 > 0)
		str2 = get_str("help",help2);
	cStrDlog display_strings(str1,str2,"Instant Help",24,PIC_DLOG, parent);
	display_strings.setSound(57);
	display_strings.show();
}

void give_help(short help1, short help2, bool help_forced) {
	give_help(help1, help2, nullptr, help_forced);
}

void give_help(short help1, short help2, cDialog& parent, bool help_forced) {
	give_help(help1, help2, &parent, help_forced);
}