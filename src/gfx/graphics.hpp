#ifndef BOE_SHARED_GRAPHICS_H
#define BOE_SHARED_GRAPHICS_H

#include <SFML/Graphics.hpp>
#include "location.hpp"
#include "tools/framerate_limiter.hpp"

bool extend_road_terrain(int x, int y);
void place_road(sf::RenderTarget& targ, short q,short r,location where,bool here, bool is_out, location screen_offset = {0,0});

#endif