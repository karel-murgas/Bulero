"""Scripts for classes."""
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


from bulero.constants import *


###########
# Classes #
###########

class HeroBody(cocos.sprite.Sprite):
    """Layer containing the body of hero"""

    def __init__(self, pic):
        super(HeroBody, self).__init__(pic)

        self.position = (200, 200)
        self.scale = HERO_BODY_SCALE
        self.default_turret = HeroTurret(HERO_TURRET_IMAGE)
        self.add(self.default_turret)

    def move_hero(self, key):
        """Move the hero sprite by WSAD keys"""
        move = None

        if key == "W":
            move = cocos.actions.MoveBy((0, HERO_MOVE_LENGTH), HERO_MOVE_SPEED)
        elif key == "S":
            move = cocos.actions.MoveBy((0, -HERO_MOVE_LENGTH), HERO_MOVE_SPEED)
        elif key == "A":
            move = cocos.actions.MoveBy((-HERO_MOVE_LENGTH, 0), HERO_MOVE_SPEED)
        elif key == "D":
            move = cocos.actions.MoveBy((HERO_MOVE_LENGTH, 0), HERO_MOVE_SPEED)

        if move is not None:
            self.do(move)

    def stop_hero(self, key):
        """Stop the hero sprite by WSAD keys"""

        if key in ["W", "S", "A", "D"]:
            self.stop()


class HeroTurret(cocos.sprite.Sprite):
    """Layer containing the turret of hero"""

    def __init__(self, pic):
        super(HeroTurret, self).__init__(pic)

        self.position = (0, 0)
        self.scale = HERO_TURRET_SCALE

    def rotate_turret(self, key):
        """Rotate turrer by QE keys"""
        rotate = None

        if key == "Q":
            rotate = cocos.actions.RotateBy(-1000, 5)
        elif key == "E":
            rotate = cocos.actions.RotateBy(1000, 5)

        if rotate is not None:
            self.do(rotate)

    def stop_turret(self, key):
        """Stop the hero sprite by QE keys"""

        if key in ["Q", "E"]:
            self.stop()

class HeroLayer(cocos.layer.Layer):
    """Layer containing the hero"""
    is_event_handler = True

    def __init__(self):
        super(HeroLayer, self).__init__()

        self.player1 = HeroBody(HERO_BODY_IMAGE)
        self.add(self.player1)

    def on_key_press(self, key, modifiers):
        """Handle key pressing"""
        self.player1.move_hero(pyglet.window.key.symbol_string(key))
        self.player1.default_turret.rotate_turret(pyglet.window.key.symbol_string(key))

    def on_key_release(self, key, modifiers):
        """Handle key pressing"""
        self.player1.stop_hero(pyglet.window.key.symbol_string(key))
        self.player1.default_turret.stop_turret(pyglet.window.key.symbol_string(key))

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse position"""
        print (x, y)

#############
# Functions #
#############


def classes():
    """Run the game"""
    cocos.director.director.init(resizable=True)
    game = cocos.scene.Scene(HeroLayer())
    cocos.director.director.run(game)


classes()