
#include "scen.global.hpp"
#include "tools/undo.hpp"
#include "scen.undo.hpp"

void handle_close_terrain_view(eScenMode new_mode);
void restore_editor_state();
void init_screen_locs();
void handle_action(location the_point,sf::Event event);
void flash_rect(rectangle to_flash);
void swap_terrain();
void set_new_terrain(ter_num_t selected_terrain);
void handle_keystroke(sf::Event event);
void handle_editor_screen_shift(int dx, int dy);
void handle_scroll(const sf::Event& event);
void get_wandering_monst();
void get_town_info();
void get_sign_resource();
void set_info_strings();
cTown::cItem edit_item(cTown::cItem item);
void change_circle_terrain(location center,short radius,ter_num_t terrain_type,short probability);
void change_rect_terrain(rectangle r,ter_num_t terrain_type,short probability,bool hollow);
void flood_fill_terrain(location start, ter_num_t terrain_type);
void frill_up_terrain();
void unfrill_terrain();
long get_town_entrance(location l);
void set_town_entrance(location l, long town_num);
void set_terrain(location l,ter_num_t terrain_type,stroke_ter_changes_t& stroke_changes,bool handle_special=true);
void adjust_space(location l,stroke_ter_changes_t& stroke_changes);
void commit_stroke();
bool is_lava(short x,short y);
ter_num_t coord_to_ter(short x,short y);
bool place_item(location spot_hit,short which_item,bool property,bool always,short odds,item_changes_t& items_placed);
void place_items_in_town();
bool place_creature(location spot_hit,mon_num_t which,creature_changes_t& creatures_placed);
void set_up_start_screen();
void set_up_main_screen();
void start_town_edit();
void start_out_edit();
void start_type_editing(eDrawMode mode);
void start_special_item_editing();
void start_quest_editing(bool just_redo_text);
void start_shops_editing(bool just_redo_text);
void start_string_editing(eStrMode mode,short just_redo_text);
void start_special_editing(short mode,short just_redo_text);
void town_entry(location spot_hit);
void start_dialogue_editing(short restoring);
void update_mouse_spot(location the_point);

bool monst_on_space(location loc,short m_num);
void place_edit_special(location loc);
void set_special(location spot_hit);
bool save_check(std::string which_dlog, bool allow_no = true);
