# import arcade
import arcade.color

import Striker
from Striker import *

import Sniper
from Sniper import *

import random

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1250
SCREEN_TITLE = "Platformer"
VIEWPORT_MARGIN = 350

HEALTHBAR_WIDTH = 175
HEALTHBAR_HEIGHT = 20
HEALTHBAR_OFFSET_Y = -10

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_WALL = 0.3


MOVEMENT_SPEED = 5
JUMP_SPEED = 6
GRAVITY = 0.5

RIGHT_FACING = 0
LEFT_FACING = 1

UPDATES_PER_FRAME = 7


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


class GameView(arcade.View):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.player_attack_timer = 0
        self.challenger_attack_timer = 0
        self.timer = 0
        self.platform_list = None
        self.player = None
        self.player_list = None
        self.challenger = None
        self.challenger_list = None
        self.player = None
        self.challenger = None
        self.view_left = 0
        self.view_bottom = 0
        self.background_list = None
        self.attack_texture = None
        self.player_bullet_list = None
        self.challenger_bullet_list = None
        self.bullet_count = 1
        self.screen_center_x = None
        self.screen_center_y = None
        self.player_health = None
        self.challenger_health = None
        self.wall_rescale = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False
        self.attack_key_pressed = False

        self.challenger_left_pressed = False
        self.challenger_right_pressed = False
        self.challenger_up_pressed = False
        self.challenger_down_pressed = False
        self.challenger_jump_needs_reset = False
        self.challenger_attack_key_pressed = False
        self.background = None

        self.cur_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.player_face_direction = RIGHT_FACING
        self.challenger_face_direction = RIGHT_FACING

        self.physics_engine = None
        self.challenger_physics_engine = None

        self.list = None
        self.other_list = None
        self.bullet_spread = None

    def setup(self):
        self.list = [1,4,3,5,2]
        self.other_list = [-1,0,2,1,-2]
        self.bullet_spread = [-0.2,0.1,0,0.2,-0.1]

        self.player_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()

        self.challenger_list = arcade.SpriteList()
        self.challenger_bullet_list = arcade.SpriteList()

        self.player_health = 20
        self.challenger_health = 20

        self.player_maxhealth = 20
        self.challenger_maxhealth = 20

        # arcade.Sprite("Sprites/Player_Ball.png", SPRITE_SCALING_PLAYER)
        self.player = Striker.PlayerCharacter()
        self.player.center_x = 300
        self.player.center_y = 185
        self.player.scale = 0.5
        self.player_list.append(self.player)

        self.challenger = Sniper.SniperCharacter()
        self.challenger.center_x = 1100
        self.challenger.center_y = 185
        self.challenger.scale = 0.5
        self.challenger_list.append(self.challenger)

        self.platform_list = arcade.SpriteList()
        self.background = arcade.SpriteList()

        map_name = "Arena.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        platform_layer_name = "platform"

        background_layer_name = "background"

        self.platform_list = arcade.tilemap.process_layer(map_object=my_map,
                                                          layer_name=platform_layer_name,
                                                          scaling=SPRITE_SCALING_WALL)

        self.background_list = arcade.tilemap.process_layer(my_map, background_layer_name, SPRITE_SCALING_WALL)

        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        """wall = arcade.Sprite("Sprites/MovingPlat.png", SPRITE_SCALING_WALL)
        wall.center_y = 150
        wall.center_x = 250
        wall.boundary_left = 500
        wall.boundary_right = 1100

        wall.boundary_top = 400
        wall.boundary_bottom = 100
        wall.change_x = 1
        wall.change_y = 0

        self.platform_list.append(wall)"""





        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player,
                                           self.platform_list,
                                           gravity_constant=GRAVITY, )

        self.challenger_physics_engine = \
            arcade.PhysicsEnginePlatformer(self.challenger,
                                           self.platform_list,
                                           gravity_constant=GRAVITY, )

    def on_show(self):
        self.setup()


    def on_draw(self):
        arcade.start_render()

        # self.background_list.draw()
        self.platform_list.draw()
        self.player_list.draw()
        self.challenger_list.draw()
        self.challenger_bullet_list.draw()
        self.player_bullet_list.draw()

        output = f"Player Health: {self.player_health}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 600, arcade.color.RED, 20)

        output = f"Challenger Health: {self.challenger_health}"
        arcade.draw_text(output, self.view_left + 1010, self.view_bottom + 600, arcade.color.RED, 20)

        output = f"Player cooldown : {self.player_attack_timer}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 525, arcade.color.BLUE, 20)

        output = f"Challenger cooldown: {self.challenger_attack_timer}"
        arcade.draw_text(output, self.view_left + 990, self.view_bottom + 525, arcade.color.BLUE, 20)

        arcade.draw_rectangle_filled(center_x=self.view_left + 100,
                                     center_y=self.view_bottom + 650 + HEALTHBAR_OFFSET_Y,
                                     width=HEALTHBAR_WIDTH,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.RED)

        health_width = HEALTHBAR_WIDTH * (self.player_health / self.player_maxhealth)

        arcade.draw_rectangle_filled(center_x= self.view_left + 100 - 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.view_bottom + 650 + HEALTHBAR_OFFSET_Y,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)

        arcade.draw_rectangle_filled(center_x=self.view_left + 1150,
                                     center_y=self.view_bottom + 650 + HEALTHBAR_OFFSET_Y,
                                     width=HEALTHBAR_WIDTH,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.RED)

        health_width = HEALTHBAR_WIDTH * (self.challenger_health / self.challenger_maxhealth)

        arcade.draw_rectangle_filled(center_x=self.view_left + 1150 + 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=self.view_bottom + 650 + HEALTHBAR_OFFSET_Y,
                                     width=health_width,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)




    def process_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # playerkeys

        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = MOVEMENT_SPEED
            elif self.physics_engine.can_jump(y_distance=10) and not self.jump_needs_reset:
                self.player.change_y = JUMP_SPEED
                self.jump_needs_reset = True

        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player.change_y = -MOVEMENT_SPEED

        # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self.player.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self.player.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player.change_x = MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player.change_x = -MOVEMENT_SPEED
        else:
            self.player.change_x = 0

        # playerbasic attack
        if self.attack_key_pressed and self.player_attack_timer == 0:
            self.player_attack_timer = 30

            player_bullet = arcade.Sprite("sprites/energy -1.png.png", 0.1)


            # Position the bullet at the player's current location
            p_start_x = self.player.center_x
            p_start_y = self.player.center_y
            if self.player_face_direction == RIGHT_FACING:

                player_bullet.center_x = p_start_x
                player_bullet.center_y = p_start_y + 5
                player_bullet.change_x = 13

            elif self.player_face_direction == LEFT_FACING:

                player_bullet.center_x = p_start_x
                player_bullet.center_y = p_start_y + 5
                player_bullet.change_x = -13


            self.player_bullet_list.append(player_bullet)

            # challenger keys

        if self.challenger_up_pressed and not self.challenger_down_pressed:
            if self.physics_engine.is_on_ladder():
                self.challenger.change_y = MOVEMENT_SPEED
            elif self.challenger_physics_engine.can_jump(y_distance=10) and not self.challenger_jump_needs_reset:
                self.challenger.change_y = JUMP_SPEED
                self.challenger_jump_needs_reset = True

        elif self.challenger_down_pressed and not self.challenger_up_pressed:
            if self.challenger_physics_engine.is_on_ladder():
                self.challenger.change_y = -MOVEMENT_SPEED

            # Process up/down when on a ladder and no movement
        if self.physics_engine.is_on_ladder():
            if not self.challenger_up_pressed and not self.challenger_down_pressed:
                self.challenger.change_y = 0
            elif self.challenger_up_pressed and self.challenger_down_pressed:
                self.challenger.change_y = 0

            # Process left/right
        if self.challenger_right_pressed and not self.challenger_left_pressed:
            self.challenger.change_x = MOVEMENT_SPEED
        elif self.challenger_left_pressed and not self.challenger_right_pressed:
            self.challenger.change_x = -MOVEMENT_SPEED
        else:
            self.challenger.change_x = 0

        # challenger attack
        if self.challenger_attack_key_pressed and self.challenger_attack_timer == 0:
            self.challenger_attack_timer = 50
            for x in range(6):
                challenger_bullet = arcade.Sprite("sprites/energy -1.png.png", 0.05)



                # Position the bullet at the player's current location
                p_start_x = self.challenger.center_x
                p_start_y = self.challenger.center_y

                if self.challenger_face_direction == 0:


                    challenger_bullet.center_x = p_start_x + 5
                    challenger_bullet.center_y = p_start_y - 30 + 8 * random.randint(2, 5)
                    challenger_bullet.change_x = 10 + random.randint(-2, 2) / 5
                    challenger_bullet.change_y = random.randint(-5, 5) / 10


                elif self.challenger_face_direction == 1:

                    challenger_bullet.center_x = p_start_x - 5
                    challenger_bullet.center_y = p_start_y - 30 + 8 * self.list[random.randint(0, 4)]
                    challenger_bullet.change_x = -10 + self.other_list[random.randint(0, 4)]
                    challenger_bullet.change_y = self.bullet_spread[random.randint(0, 4)]


                # Get from the mouse the destination location for the bullet
                # IMPORTANT! If you have a scrolling screen, you will also need
                # to add in self.view_bottom and self.view_left.

                # Add the bullet to the appropriate lists
                self.challenger_bullet_list.append(challenger_bullet)

    def on_key_press(self, key, modifiers):

        self.player.on_key_press(key)
        self.challenger.on_key_press(key)

        # playerkeys
        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.KEY_1:
            self.attack_key_pressed = True

        # challenger keys
        if key == arcade.key.UP:
            self.challenger_up_pressed = True
        elif key == arcade.key.DOWN:
            self.challenger_down_pressed = True
        elif key == arcade.key.LEFT:
            self.challenger_left_pressed = True
        elif key == arcade.key.RIGHT:
            self.challenger_right_pressed = True
        elif key == arcade.key.M:
            self.challenger_attack_key_pressed = True

        self.process_keychange()

    def on_key_release(self, key, modifiers):

        self.player.on_key_release(key)
        self.challenger.on_key_release(key)

        # playerkeys
        if key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False
        elif key == arcade.key.KEY_1:
            self.attack_key_pressed = False

        # challenger keys
        if key == arcade.key.UP:
            self.challenger_up_pressed = False
            self.challenger_jump_needs_reset = False
        elif key == arcade.key.DOWN:
            self.challenger_down_pressed = False
        elif key == arcade.key.LEFT:
            self.challenger_left_pressed = False
        elif key == arcade.key.RIGHT:
            self.challenger_right_pressed = False
        elif key == arcade.key.M:
            self.challenger_attack_key_pressed = False

        self.process_keychange()

    def on_update(self, delta_time):

        self.physics_engine.update()
        self.player_list.update_animation()
        self.player_list.update()
        self.player_bullet_list.update()

        self.challenger_physics_engine.update()
        self.challenger_list.update_animation()
        self.challenger_list.update()
        self.challenger_bullet_list.update()
        changed = False

        if self.physics_engine.can_jump():
            self.player.can_jump = False
        else:
            self.player.can_jump = True

        if self.player_attack_timer > 0:
            self.player_attack_timer -= 1

        if self.challenger_attack_timer > 0:
            self.challenger_attack_timer -= 1


        for bullet in self.player_bullet_list:
            challenger_hit = arcade.check_for_collision_with_list(bullet, self.challenger_list)
            if len(challenger_hit) > 0:
                bullet.remove_from_sprite_lists()
                self.challenger_health -= 2

        for bullet in self.challenger_bullet_list:
            player_hit = arcade.check_for_collision_with_list(bullet, self.player_list)
            if len(player_hit) > 0:
                bullet.remove_from_sprite_lists()
                self.player_health -= 1

        for bullet in self.player_bullet_list:
            plat_hit = arcade.check_for_collision_with_list(bullet, self.platform_list)
            if len(plat_hit) > 0:
                bullet.remove_from_sprite_lists()

        for bullet in self.challenger_bullet_list:
            plat_hit = arcade.check_for_collision_with_list(bullet, self.platform_list)
            if len(plat_hit) > 0:
                bullet.remove_from_sprite_lists()

        if self.challenger_health < 0 or self.player_health < 0:
            print("we have a winner")

        # focusing the screen on the center between the players





        if self.challenger.change_x < 0 and self.challenger_face_direction == RIGHT_FACING:
            self.challenger_face_direction = LEFT_FACING
        elif self.challenger.change_x > 0 and self.challenger_face_direction == LEFT_FACING:
            self.challenger_face_direction = RIGHT_FACING

        if self.player.change_x < 0 and self.player_face_direction == RIGHT_FACING:
            self.player_face_direction = LEFT_FACING
        elif self.player.change_x > 0 and self.player_face_direction == LEFT_FACING:
            self.player_face_direction = RIGHT_FACING

        if self.player.center_x > self.challenger.center_x:
            self.screen_center_x = (self.player.center_x + self.challenger.center_x) / 2
        else:
            self.screen_center_x = (self.challenger.center_x + self.player.center_x) / 2

        if self.player.center_y > self.challenger.center_y:
            self.screen_center_y = (self.player.center_y + self.challenger.center_y) / 2
        else:
            self.screen_center_y = (self.challenger.center_y + self.player.center_y) / 2

            # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.screen_center_x < left_boundary:
            self.view_left -= left_boundary - self.screen_center_x
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.screen_center_x > right_boundary:
            self.view_left += self.screen_center_x - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.screen_center_y > top_boundary:
            self.view_bottom += self.screen_center_y - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.screen_center_y < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.screen_center_y
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        # if self.player.center_y < -50:
        # arcade.close_window()







def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()


main()
