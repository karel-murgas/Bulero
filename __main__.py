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


#############
# Constants #
#############

MOVE_LENGTH = 20
MOVE_SPEED = 0.1
PROTAGONIST_SCALE = 0.25


###########
# Classes #
###########


class HeroLayer(cocos.layer.Layer):
    """Layer containing the protagonists"""

    is_event_handler = True

    def __init__(self):
        super(HeroLayer, self).__init__()

        self.hero = cocos.sprite.Sprite("sprites/vesely_tank.png")
        self.hero.position = (200, 200)
        self.hero.scale = PROTAGONIST_SCALE
        self.add(self.hero, z=1)

    def move_hero(self, key):
        """Move the hero sprite by WSAD keys"""
        move = None

        if key == "W":
            move = cocos.actions.MoveBy((0, MOVE_LENGTH), MOVE_SPEED)
        elif key == "S":
            move = cocos.actions.MoveBy((0, -MOVE_LENGTH), MOVE_SPEED)
        elif key == "A":
            move = cocos.actions.MoveBy((-MOVE_LENGTH, 0), MOVE_SPEED)
        elif key == "D":
            move = cocos.actions.MoveBy((MOVE_LENGTH, 0), MOVE_SPEED)

        if move is not None:
            self.hero.do(move)

    def on_key_press(self, key, modifiers):
        """Handles key pressing"""
        self.move_hero(pyglet.window.key.symbol_string(key))

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
