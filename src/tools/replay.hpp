#ifndef REPLAY_GLOBAL_H
#define REPLAY_GLOBAL_H

#include <string>
#include <sstream>
#include <map>
#include <boost/filesystem.hpp>
#include "location.hpp"
#include "dialogxml/keycodes.hpp"
#include "game/boe.newgraph.hpp"

// Input recording system
namespace ticpp {
    class Element;
    class Text;
}
using ticpp::Element;
using ticpp::Text;

struct word_rect_t;

extern bool recording;
// True if a replay is currently ongoing.
// False after actions run out, Ctrl+C interrupts the replay,
//   or an error occurs:
extern bool replaying;
// Always true if this session started as a replay:
extern bool was_replaying;

extern bool replay_strict;

extern std::string last_action_type;

extern bool init_action_log(std::string command, std::string file);
extern void record_action(std::string action_type, std::string inner_text, bool cdata = false);
extern void record_action(std::string action_type, std::map<std::string,std::string> info);
extern void record_action(Element& action);
extern void record_field_input(cKey key);
extern bool has_next_action(std::string type = "");
extern std::string next_action_type();
extern int next_action_line();
extern Element& pop_next_action(std::string expected_action_type="");
extern std::map<std::string,std::string> info_from_action(Element& action);
extern std::string encode_file(fs::path file);
extern void decode_file(std::string data, fs::path file);
extern location location_from_action(Element& action);
extern short short_from_action(Element& action);
extern cKey key_from_action(Element& action);
extern word_rect_t word_rect_from_action(Element& action);
extern void record_click_talk_rect(word_rect_t word_rect, bool preset);
extern void start_log_file(std::string file);

extern const std::string replay_warning;
extern const std::string replay_error;

#endif
