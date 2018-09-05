"""All constants for game."""
#    Copyright (C) 2018 by
#    Karel "laird Odol" Murgas - karel.murgas@gmail.com
#    Tobias "Insolitus" Kucera - tobias.kucera@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Have fun!

###########
# Imports #
###########


import cocos
import pyglet


#############
# Constants #
#############

# Heroes constants
HERO_BODY_IMAGE = "resources/heroes/hero_body_quadropod_tank.png"
HERO_BODY_SCALE = 0.25
HERO_TURRET_IMAGE = "resources/heroes/hero_turret_quadropod_tank.png"
HERO_TURRET_SCALE = 2

HERO_MOVE_LENGTH = 1000
HERO_MOVE_SPEED = 10