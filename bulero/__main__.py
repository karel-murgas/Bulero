"""Main script for Bulero. Runs the game."""
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
from bulero.classes import *


###########
# Classes #
###########


#############
# Functions #
#############


def main():
    """Run the game"""
    cocos.director.director.init(resizable=True)
    game = cocos.scene.Scene(HeroLayer())
    cocos.director.director.run(game)


if __name__ == "__main__":
    main()
