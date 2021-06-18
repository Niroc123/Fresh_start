# import arcade
import arcade.color


import Type
from Type import *
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1250
SCREEN_TITLE = "Platformer"
VIEWPORT_MARGIN = 350

HEALTH_BAR_WIDTH = 175
HEALTH_BAR_HEIGHT = 20
HEALTH_BAR_OFFSET_Y = -10

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_WALL = 0.3


MOVEMENT_SPEED = 5
JUMP_SPEED = 10
GRAVITY = 0.6

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


class TitleView(arcade.View):
    def __init__(self):
        super().__init__()
        self.title = None

    def on_show(self):
        arcade.set_background_color((58, 57, 53))
        self.title = arcade.load_texture("sprites/Stick man Menu.png")

    def on_draw(self):
        arcade.start_render()

        self.title.draw_scaled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0.4)

        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, SCREEN_HEIGHT/2-200, arcade.color.GRAY, font_size=20,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        character_choice_1 = Choice1()
        self.window.show_view(character_choice_1)


class Choice1(arcade.View):
    def __init__(self):
        super().__init__()
        self.title = None

        self.Next = None

        self.Shotgun = None
        self.Striker = None
        self.Sword = None
        self.Spear = None
        self.Sniper = None
        self.Daggers = None

        self.character_chosen_list = None

        self.chosen = 0
        
        self.selector = None
        self.selector_list = None

        self.selector_x = [300, 900, 200, 1000, 200, 1000]

        self.selector_y = [150, 150, 350, 350, 550, 550]
    
    def on_show(self):

        arcade.set_background_color((58, 57, 53))

        self.character_chosen_list = arcade.SpriteList()
        self.selector_list = arcade.SpriteList()

        self.selector = arcade.Sprite("Sprites/Choice selector.png")
        self.selector.center_x = 100
        self.selector.center_y = 111
        self.selector.scale = 3
        self.selector_list.append(self.selector)

        self.Striker = arcade.Sprite("Sprites/Buttons/Striker button.png")
        self.Striker.center_x = 300
        self.Striker.center_y = 150
        self.Striker.scale = 0.25
        self.character_chosen_list.append(self.Striker)

        self.Sniper = arcade.Sprite("Sprites/Buttons/Sniper button.png")
        self.Sniper.center_x = 200
        self.Sniper.center_y = 350
        self.Sniper.scale = 0.25
        self.character_chosen_list.append(self.Sniper)

        self.Spear = arcade.Sprite("Sprites/Buttons/Spear button.png")
        self.Spear.center_x = 200
        self.Spear.center_y = 550
        self.Spear.scale = 0.25
        self.character_chosen_list.append(self.Spear)

        self.Shotgun = arcade.Sprite("Sprites/Buttons/Shotgun button.png")
        self.Shotgun.center_x = 900
        self.Shotgun.center_y = 150
        self.Shotgun.scale = 0.25
        self.character_chosen_list.append(self.Shotgun)

        self.Sword = arcade.Sprite("Sprites/Buttons/Swordboard button.png")
        self.Sword.center_x = 1000
        self.Sword.center_y = 350
        self.Sword.scale = 0.25
        self.character_chosen_list.append(self.Sword)

        self.Daggers = arcade.Sprite("Sprites/Buttons/Daggers.png")
        self.Daggers.center_x = 1000
        self.Daggers.center_y = 550
        self.Daggers.scale = 0.25
        self.character_chosen_list.append(self.Daggers)

        self.Next = arcade.Sprite("Sprites/Next button.png")
        self.Next.center_x = 1150
        self.Next.center_y = 100
        self.Next.scale = 1
        self.character_chosen_list.append(self.Next)

    def on_draw(self):
        arcade.start_render()
        self.character_chosen_list.draw()
        self.selector_list.draw()

        arcade.draw_text("Player", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GRAY, font_size=40,
                         anchor_x="center")

    def on_update(self, delta_time: float):
        global chosen_1
        chosen_1 = self.chosen

        self.selector.center_x = self.selector_x[chosen_1] - 5
        self.selector.center_y = self.selector_y[chosen_1] - 70

    def on_mouse_press(self, x: float, y: float, _button, _modifiers):
        """instructions_view = InstructionView()
        self.window.show_view(instructions_view)"""

        chosen = arcade.get_sprites_at_point((x, y), self.character_chosen_list)
        if len(chosen) > 0:

            if self.Striker in chosen:
                print("Striker")
                self.chosen = 0
            elif self.Shotgun in chosen:
                print("Shotgun")
                self.chosen = 1
            elif self.Sniper in chosen:
                print("Sniper")
                self.chosen = 2
            elif self.Sword in chosen:
                print("Sword")
                self.chosen = 3
            elif self.Spear in chosen:
                print("Spear")
                self.chosen = 4
            elif self.Daggers in chosen:
                print("Daggers")
                self.chosen = 5
            elif self.Next in chosen:
                self.window.show_view(Choice2())


class Choice2(arcade.View):
    def __init__(self):
        super().__init__()
        self.title = None

        self.Next = None

        self.Shotgun = None
        self.Striker = None
        self.Sword = None
        self.Spear = None
        self.Sniper = None
        self.Daggers = None

        self.character_chosen_list = None

        self.chosen = 0

        self.selector_list = None
        self.selector = None
        
        self.selector_x = [300, 900, 200, 1000, 200, 1000]

        self.selector_y = [150, 150, 350, 350, 550, 550]

    def on_show(self):

        arcade.set_background_color((58, 57, 53))

        self.character_chosen_list = arcade.SpriteList()

        self.selector_list = arcade.SpriteList()

        self.selector = arcade.Sprite("Sprites/Choice selector.png")
        self.selector.center_x = 100
        self.selector.center_y = 111
        self.selector.scale = 3
        self.selector_list.append(self.selector)

        self.Striker = arcade.Sprite("Sprites/Buttons/Striker button.png")
        self.Striker.center_x = 300
        self.Striker.center_y = 150
        self.Striker.scale = 0.25
        self.character_chosen_list.append(self.Striker)

        self.Sniper = arcade.Sprite("Sprites/Buttons/Sniper button.png")
        self.Sniper.center_x = 200
        self.Sniper.center_y = 350
        self.Sniper.scale = 0.25
        self.character_chosen_list.append(self.Sniper)

        self.Spear = arcade.Sprite("Sprites/Buttons/Spear button.png")
        self.Spear.center_x = 200
        self.Spear.center_y = 550
        self.Spear.scale = 0.25
        self.character_chosen_list.append(self.Spear)

        self.Shotgun = arcade.Sprite("Sprites/Buttons/Shotgun button.png")
        self.Shotgun.center_x = 900
        self.Shotgun.center_y = 150
        self.Shotgun.scale = 0.25
        self.character_chosen_list.append(self.Shotgun)

        self.Sword = arcade.Sprite("Sprites/Buttons/Swordboard button.png")
        self.Sword.center_x = 1000
        self.Sword.center_y = 350
        self.Sword.scale = 0.25
        self.character_chosen_list.append(self.Sword)

        self.Daggers = arcade.Sprite("Sprites/Buttons/Daggers.png")
        self.Daggers.center_x = 1000
        self.Daggers.center_y = 550
        self.Daggers.scale = 0.25
        self.character_chosen_list.append(self.Daggers)

        self.Next = arcade.Sprite("Sprites/Next button.png")
        self.Next.center_x = 1150
        self.Next.center_y = 100
        self.Next.scale = 1
        self.character_chosen_list.append(self.Next)

    def on_draw(self):
        arcade.start_render()

        self.character_chosen_list.draw()
        self.selector_list.draw()

        arcade.draw_text("Challenger", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.GRAY, font_size=40,
                         anchor_x="center")

    def on_update(self, delta_time: float):
        global chosen_2
        chosen_2 = self.chosen

        self.selector.center_x = self.selector_x[chosen_2] - 5
        self.selector.center_y = self.selector_y[chosen_2] - 70

    def on_mouse_press(self, x: float, y: float, _button, _modifiers):
        """instructions_view = InstructionView()
        self.window.show_view(instructions_view)"""

        chosen = arcade.get_sprites_at_point((x, y), self.character_chosen_list)
        if len(chosen) > 0:

            if self.Striker in chosen:
                print("Striker")
                self.chosen = 0
            elif self.Shotgun in chosen:
                print("Shotgun")
                self.chosen = 1
            elif self.Sniper in chosen:
                print("Sniper")
                self.chosen = 2
            elif self.Sword in chosen:
                print("Sword")
                self.chosen = 3
            elif self.Spear in chosen:
                print("Spear")
                self.chosen = 4
            elif self.Daggers in chosen:
                print("Daggers")
                self.chosen = 5
            elif self.Next in chosen:
                self.window.show_view(InstructionView())


class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.candle = arcade.load_texture("sprites/Instructions -1.png.png")

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.candle.draw_scaled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0.4)

        arcade.draw_text("Instructions Screen", SCREEN_WIDTH/2 , SCREEN_HEIGHT - 100,
                         arcade.color.WHITE, font_size=45, anchor_x="center")

        arcade.draw_text("Player 1", SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT - 200,
                         arcade.color.WHITE, font_size=30, anchor_x="center")
        arcade.draw_text("Player 2", SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT - 200,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("Arrow keys for movement", SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT - 300,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("WASD keys for movement", SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT - 300,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("1  to attack ", SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT - 400,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("M  to attack", SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT - 400,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150, arcade.color.GRAY, font_size=20,
                         anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class GameView(arcade.View):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        self.timer = 0
        self.wall_list = None
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

        self.player_jump_count = 0
        self.challenger_jump_count = 0

        self.player_max_health = None
        self.challenger_max_health = None

        self.bingo = 0
        self.ding =0

        self.bullet_list = None

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

        self.Choice_1 = Choice1()
        self.Choice_2 = Choice2()

        # jump
        # damage
        # Knockback

        self.character_info = {
         # Striker info
         0: {
                0: 2,
                1: 2,
                2: 25
            },
         # Shotgun info
         1: {
                0: 1,
                1: 1,
                2: 10
            },
         # sniper
         2: {
                0: 1,
                1: 5,
                2: 50
            },
         # sword
         3: {
                0: 2,
                1: 2,
                2: 10

            },
         # Spear
         4: {
                0: 2,
                1: 2,
                2: 50

            },
         # Dagger
         5: {
                0: 2,
                1: 1,
                2: 5

         }

        }

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.challenger_list = arcade.SpriteList()

        self.player_health = 20
        self.challenger_health = 20

        self.player_max_health = 20
        self.challenger_max_health = 20

        self.player = Type.Character()
        self.player.character_type = chosen_1
        self.player.setup()
        self.player.center_x = 300
        self.player.center_y = 185
        self.player.scale = SPRITE_SCALING_PLAYER
        self.player_list.append(self.player)

        self.challenger = Type.Character()
        self.challenger.character_type = chosen_2
        self.challenger.setup()
        self.challenger.center_x = 1100
        self.challenger.center_y = 185
        self.challenger.scale = SPRITE_SCALING_PLAYER
        self.challenger_list.append(self.challenger)

        self.wall_list = arcade.SpriteList()
        self.background = arcade.SpriteList()

        map_name = "Arena.tmx"

        my_map = arcade.tilemap.read_tmx(map_name)

        platform_layer_name = "platform"

        background_layer_name = "background"

        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
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

        self.wall_list.append(wall)"""

        self.physics_engine = \
            arcade.PhysicsEnginePlatformer(self.player,
                                           self.wall_list,
                                           gravity_constant=GRAVITY, )

        self.challenger_physics_engine = \
            arcade.PhysicsEnginePlatformer(self.challenger,
                                           self.wall_list,
                                           gravity_constant=GRAVITY, )

    def on_show(self):
        self.setup()

    def on_draw(self):
        arcade.start_render()

        self.player.on_draw()

        self.challenger.on_draw()

        # self.background_list.draw()
        self.wall_list.draw()
        self.player_list.draw()
        self.challenger_list.draw()

        output = f"Player Health: {self.player_health}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 600, arcade.color.RED, 20)

        output = f"Challenger Health: {self.challenger_health}"
        arcade.draw_text(output, self.view_left + 1010, self.view_bottom + 600, arcade.color.RED, 20)

        output = f"Player cool down : {self.player.attack_timer}"
        arcade.draw_text(output, self.view_left + 10, self.view_bottom + 525, arcade.color.BLUE, 20)

        output = f"Challenger cool down: {self.challenger.attack_timer}"
        arcade.draw_text(output, self.view_left + 990, self.view_bottom + 525, arcade.color.BLUE, 20)

        arcade.draw_rectangle_filled(center_x=self.view_left + 100,
                                     center_y=self.view_bottom + 650 + HEALTH_BAR_OFFSET_Y,
                                     width=HEALTH_BAR_WIDTH,
                                     height=HEALTH_BAR_HEIGHT,
                                     color=arcade.color.RED)

        health_width = HEALTH_BAR_WIDTH * (self.player_health / self.player_max_health)

        arcade.draw_rectangle_filled(center_x=self.view_left + 100 - 0.5 * (HEALTH_BAR_WIDTH - health_width),
                                     center_y=self.view_bottom + 650 + HEALTH_BAR_OFFSET_Y,
                                     width=health_width,
                                     height=HEALTH_BAR_HEIGHT,
                                     color=arcade.color.GREEN)

        arcade.draw_rectangle_filled(center_x=self.view_left + 1150,
                                     center_y=self.view_bottom + 650 + HEALTH_BAR_OFFSET_Y,
                                     width=HEALTH_BAR_WIDTH,
                                     height=HEALTH_BAR_HEIGHT,
                                     color=arcade.color.RED)

        health_width = HEALTH_BAR_WIDTH * (self.challenger_health / self.challenger_max_health)

        arcade.draw_rectangle_filled(center_x=self.view_left + 1150 + 0.5 * (HEALTH_BAR_WIDTH - health_width),
                                     center_y=self.view_bottom + 650 + HEALTH_BAR_OFFSET_Y,
                                     width=health_width,
                                     height=HEALTH_BAR_HEIGHT,
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
            elif not self.jump_needs_reset:
                self.player.change_y = JUMP_SPEED
                self.player_jump_count += 1
                if self.player_jump_count > self.character_info[self.player.character_type][0]:
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

            # challenger keys
        if self.challenger_up_pressed and not self.challenger_down_pressed:
            if self.physics_engine.is_on_ladder():
                self.challenger.change_y = MOVEMENT_SPEED
            elif not self.challenger_jump_needs_reset:
                self.challenger.change_y = JUMP_SPEED
                self.challenger_jump_count += 1
                if self.challenger_jump_count > self.character_info[self.challenger.character_type][0]:
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

        if self.challenger_attack_key_pressed:

            self.challenger.primary_attack()

        if self.attack_key_pressed:
            self.player.primary_attack()

    def on_key_press(self, key, modifiers):

        self.player.on_key_press(key)
        self.challenger.on_key_press(key)

        # player keys
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

        self.challenger_physics_engine.update()
        self.challenger_list.update_animation()
        self.challenger_list.update()

        changed = False

        if self.physics_engine.can_jump():
            self.player.can_jump = False
        else:
            self.player.can_jump = True

        if self.challenger_physics_engine.can_jump():
            self.challenger.can_jump = False
        else:
            self.challenger.can_jump = True

        if self.player.attack_timer > 0:
            self.player.attack_timer -= 1

        if self.challenger.attack_timer > 0:
            self.challenger.attack_timer -= 1

        if self.physics_engine.can_jump(y_distance=10):

            self.jump_needs_reset = False
            self.player_jump_count = 0

        if self.challenger_physics_engine.can_jump(y_distance=10):

            self.challenger_jump_needs_reset = False
            self.challenger_jump_count = 0

        # player damage to challenger
        for bullet in self.player.bullet_list:
            challenger_hit = arcade.check_for_collision_with_list(bullet, self.challenger_list)
            if len(challenger_hit) > 0:
                bullet.remove_from_sprite_lists()
                self.challenger_health -= self.character_info[self.player.character_type][1]
                if bullet.change_x > 0:
                    self.challenger.center_x += self.character_info[self.player.character_type][2]

                elif bullet.change_x < 0:
                    self.challenger.center_x -= self.character_info[self.player.character_type][2]

        # challenger damage to player
        for bullet in self.challenger.bullet_list:
            player_hit = arcade.check_for_collision_with_list(bullet, self.player_list)
            if len(player_hit) > 0:
                bullet.remove_from_sprite_lists()
                self.player_health -= self.character_info[self.challenger.character_type][1]

                if bullet.change_x < 0:
                    self.player.center_x -= self.character_info[self.challenger.character_type][2]

                elif bullet.change_x > 0:

                    self.player.center_x += self.character_info[self.challenger.character_type][2]



        for bullet in self.player.bullet_list:
            plat_hit = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(plat_hit) > 0:
                bullet.remove_from_sprite_lists()

        for bullet in self.challenger.bullet_list:
            plat_hit = arcade.check_for_collision_with_list(bullet, self.wall_list)
            if len(plat_hit) > 0:
                bullet.remove_from_sprite_lists()

        for bullet in self.player.bullet_list:
            if self.player.character_type == 0:

                self.bingo += delta_time
                if self.bingo >= 1/60:
                    self.bingo = 0
                    self.ding += 1
                    if self.ding > 5:
                        self.ding = 0
                        bullet.remove_from_sprite_lists()

        for bullet in self.challenger.bullet_list:
            if self.challenger.character_type == 0:

                self.bingo += delta_time
                if self.bingo >= 1/60:
                    self.bingo = 0
                    self.ding += 1
                    if self.ding > 5:
                        self.ding = 0
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


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = TitleView()
    window.show_view(menu_view)
    arcade.run()


main()
