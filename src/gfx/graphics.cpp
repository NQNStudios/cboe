#include "graphics.hpp"

#include "fileio/resmgr/res_image.hpp"
#include "render_image.hpp"
#include "scenario/terrain.hpp"

extern bool is_road(int x, int y);
extern ter_num_t coord_to_ter(short x, short y);
extern const cTerrain& get_ter_type(ter_num_t t);
extern size_t cur_town_max_dim();
extern size_t out_max_dim;

bool extend_road_terrain(int x, int y) {
	if(is_road(x, y)) return true;
	ter_num_t ter = coord_to_ter(x,y);
	const cTerrain& type = get_ter_type(ter);
	eTrimType trim = type.trim_type;
	eTerSpec spec = type.special;
	ter_num_t flag = type.flag1;
	if(trim == eTrimType::CITY || trim == eTrimType::WALKWAY)
		return true;
	if(spec == eTerSpec::BRIDGE)
		return true;
	if(spec == eTerSpec::TOWN_ENTRANCE && trim != eTrimType::NONE)
		return true; // cave entrance, most likely
	if(spec == eTerSpec::UNLOCKABLE || spec == eTerSpec::CHANGE_WHEN_STEP_ON)
		return true; // closed door, possibly locked; or closed portcullis
	if(spec == eTerSpec::CHANGE_WHEN_USED){
		const cTerrain& to_type = get_ter_type(flag);
		if(to_type.special == eTerSpec::CHANGE_WHEN_STEP_ON && to_type.flag1 == ter)
			return true; // open door (I think) TODO: Verify this works
	} 
	if(spec == eTerSpec::LOCKABLE)
		return true; // open portcullis (most likely)
	return false;
}

void place_road(sf::RenderTarget& targ, short q,short r,location where,bool here,bool is_out, location screen_offset) {
	rectangle to_rect;
	static const rectangle road_rects[5] = {
		{76,28,80,41},	// horizontal partial
		{72,60,90,64},	// vertical partial
		{72,28,75,56},	// horizontal full
		{72,56,108,60},	// vertical full
		{80,28,84,32},	// central spot
	};
	static const rectangle road_dest_rects[7] = {
		{0,12,18,16},	// top
		{16,15,20,28},	// right
		{18,12,36,16},	// bottom
		{16,0,20,13},	// left
		{0,12,36,16},	// top + bottom
		{16,0,20,28},	// right + left
		{16,12,20,16},	// central spot
	};
	
	sf::Texture& roads_gworld = *ResMgr::graphics.get("fields");
	
	if(here){
		to_rect = road_dest_rects[6];
		to_rect.offset(13 + q * 28,13 + r * 36);
		to_rect.offset(screen_offset);
		rect_draw_some_item(roads_gworld, road_rects[4], targ, to_rect);
		
		if((where.y == 0) || extend_road_terrain(where.x, where.y - 1)) {
			to_rect = road_dest_rects[0];
			to_rect.offset(13 + q * 28,13 + r * 36);
			to_rect.offset(screen_offset);
			rect_draw_some_item (roads_gworld, road_rects[1], targ, to_rect);
		}
		
		if((is_out && (where.x == out_max_dim)) || (!is_out && (where.x == cur_town_max_dim() - 1))
			|| extend_road_terrain(where.x + 1, where.y)) {
			to_rect = road_dest_rects[1];
			to_rect.offset(13 + q * 28,13 + r * 36);
			to_rect.offset(screen_offset);
			rect_draw_some_item (roads_gworld, road_rects[0], targ, to_rect);
		}
		
		if((is_out && (where.y == out_max_dim)) || (!is_out && (where.y == cur_town_max_dim() - 1))
			|| extend_road_terrain(where.x, where.y + 1)) {
			to_rect = road_dest_rects[2];
			to_rect.offset(13 + q * 28,13 + r * 36);
			to_rect.offset(screen_offset);
			rect_draw_some_item (roads_gworld, road_rects[1], targ, to_rect);
		}
		
		if((where.x == 0) || extend_road_terrain(where.x - 1, where.y)) {
			to_rect = road_dest_rects[3];
			to_rect.offset(13 + q * 28,13 + r * 36);
			to_rect.offset(screen_offset);
			rect_draw_some_item (roads_gworld, road_rects[0], targ, to_rect);
		}
	}
}
