import arcade
import random

RIGHT_FACING = 0
LEFT_FACING = 1

UPDATES_PER_FRAME = 7
ATTACK_UPDATES_PER_FRAME = 3

SPRITE_SCALING_PLAYER = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


class Character(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.xX_SIP_Xx = 0
        self.cur_texture = 0
        self.cur_attack_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.scale = SPRITE_SCALING_PLAYER

        self.list = None
        self.other_list = None
        self.bullet_spread = None

        self.attack_timer = 0

        self.character_type = 0
        self.attack_type = 0
        self.list_of_attacks = [self.attack, self.attack_2, self.attack, self.attack_2, self.attack, self.attack_2]



        """self.lots_of_attacks = {
            0: self.attack,
            1: self.attack_2
        }"""





        self.primary_attack = None

        self.bullet = Bullet()
        self.bullet_list = None

        self.bam = False
        self.shotgun_pressed = True
        self.jumping = False

        self.Striker_idle_texture_pair = load_texture_pair("Sprites/Characters/Striker/idle.png")
        self.Shotgun_idle_texture_pair = load_texture_pair("Sprites/Characters/Shotgunner/idle.png")
        self.Sniper_idle_texture_pair = load_texture_pair("Sprites/Characters/Sniper/idle.png")
        self.Sword_idle_texture_pair = load_texture_pair("Sprites/Characters/SwordnShield/idle.png")
        self.Spear_idle_texture_pair = load_texture_pair("Sprites/Characters/Spear/idle.png")
        self.Dagger_idle_texture_pair = load_texture_pair("Sprites/Characters/Daggers/idle.png")

        self.Striker_jump_texture_pair = load_texture_pair("Sprites/Characters/Striker/Jumping.png")
        self.Shotgun_jump_texture_pair = load_texture_pair("Sprites/Characters/Shotgunner/Jumping.png")
        self.Sniper_jump_texture_pair = load_texture_pair("Sprites/Characters/Sniper/Jumping.png")
        self.Sword_jump_texture_pair = load_texture_pair("Sprites/Characters/SwordnShield/Jumping.png")
        self.Spear_jump_texture_pair = load_texture_pair("Sprites/Characters/Spear/Jumping.png")
        self.Dagger_jump_texture_pair = load_texture_pair("Sprites/Characters/Daggers/Jumping.png")



        self.Striker_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Striker/Run" + str(i) + ".png")
            self.Striker_walk_textureslr.append(texture)

        # walking left and right
        self.Shotgun_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Shotgunner/Run" + str(i) + ".png")
            self.Shotgun_walk_textureslr.append(texture)

        self.Sniper_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Sniper/Run" + str(i) + ".png")
            self.Sniper_walk_textureslr.append(texture)

        self.Sword_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/SwordnShield/Run" + str(i) + ".png")
            self.Sword_walk_textureslr.append(texture)

        self.Spear_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Spear/Run" + str(i) + ".png")
            self.Spear_walk_textureslr.append(texture)

        self.Daggers_walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Daggers/Run" + str(i) + ".png")
            self.Daggers_walk_textureslr.append(texture)

        self.Striker_attack_texture = []
        for i in range(3):
            texture = load_texture_pair("Sprites/Characters/Striker/punch" + str(i) + ".png")
            self.Striker_attack_texture.append(texture)

        self.Shotgun_attack_texture = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Shotgunner/Shotgun_attack" + str(i) + ".png")
            self.Shotgun_attack_texture.append(texture)


        if self.character_type == 0:
            self.texture = self.Striker_idle_texture_pair[self.character_face_direction]
        elif self.character_type == 1:
            self.texture = self.Shotgun_idle_texture_pair[self.character_face_direction]

        self.setup()

        self.character_run = {
            0: self.Striker_walk_textureslr,
            1: self.Shotgun_walk_textureslr,
            2: self.Sniper_walk_textureslr,
            3: self.Sword_walk_textureslr,
            4: self.Spear_walk_textureslr,
            5: self.Daggers_walk_textureslr

        }

        self.character_idle = {
            0: self.Striker_idle_texture_pair,
            1: self.Shotgun_idle_texture_pair,
            2: self.Sniper_idle_texture_pair,
            3: self.Sword_idle_texture_pair,
            4: self.Spear_idle_texture_pair,
            5: self.Dagger_idle_texture_pair
        }

        self.character_jump = {
            0: self.Striker_jump_texture_pair,
            1: self.Shotgun_jump_texture_pair,
            2: self.Sniper_jump_texture_pair,
            3: self.Sword_jump_texture_pair,
            4: self.Spear_jump_texture_pair,
            5: self.Dagger_jump_texture_pair


        }

    def setup(self):  # setting up spritelists so player can detect them

        self.list = [1, 4, 3, 5, 2]
        self.other_list = [-1, 0, 2, 1, -2]
        self.bullet_spread = [-0.2, 0.1, 0, 0.2, -0.1]


        self.bullet_list = arcade.SpriteList()
        self.primary_attack = self.list_of_attacks[self.character_type]

    def on_key_press(self, key: int):

        if key == arcade.key.M:
            #self.shotgun_pressed = False
            #self.xX_SIP_Xx = 1
            # Character.attack(self)
            # print("1")
            print(f'pressed:{self.shotgun_pressed}')

    def on_key_release(self, key: int):

        if key == arcade.key.M:

            print(f'releaded press:{self.shotgun_pressed}')

    def on_draw(self):
        self.bullet_list.draw()

    def update(self):
        self.bullet_list.update()

    def on_update(self, delta_time: float = 1/60):
        return

    def update_animation(self, delta_time: float = 1/60):
        # print(self.pressed)
        # print(self.chez)
        """if self.pressed:

            self.bam = True
            print(self.bam)"""

        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0 and self.shotgun_pressed:
            self.texture =self.character_idle[self.character_type][self.character_face_direction]


        if self.change_x < 0 or self.change_x > 0:
            # Walking animation
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.character_run[self.character_type][self.cur_texture // UPDATES_PER_FRAME][
                    self.character_face_direction]





        if self.change_y > 0:
            self.texture = self.character_jump[self.character_type][self.character_face_direction]
            return
        elif self.change_y < 0:
            self.texture = self.character_jump[self.character_type][self.character_face_direction]
            return

        if not self.shotgun_pressed:

            self.xX_SIP_Xx += delta_time

            if self.xX_SIP_Xx >= 1/60:
                self.xX_SIP_Xx = 0
                self.cur_attack_texture += 1
                if self.cur_attack_texture > 4 * ATTACK_UPDATES_PER_FRAME:
                    self.cur_attack_texture = 0
                    self.shotgun_pressed = True
                self.texture = self.Shotgun_attack_texture[self.cur_attack_texture // ATTACK_UPDATES_PER_FRAME][
                    self.character_face_direction]

    def attack(self):
        # bullet = Bullet()
        if self.attack_timer == 0:
            self.attack_timer = 30
            bullet = arcade.Sprite()
            bullet.texture = arcade.load_texture("sprites/BLUEBALL.png")
            bullet.scale = 0.5
            print("bing bong")

            # Position the bullet at the player's current location
            p_start_x = self.center_x
            p_start_y = self.center_y
            if self.character_face_direction == RIGHT_FACING:

                bullet.center_x = p_start_x
                bullet.center_y = p_start_y + 5
                bullet.change_x = 20
            elif self.character_face_direction == LEFT_FACING:

                bullet.center_x = p_start_x
                bullet.center_y = p_start_y + 5
                bullet.change_x = -13

            self.bullet_list.append(bullet)




        else:
            return
    def attack_2(self):
        # bullet = Bullet()
        if self.attack_timer == 0:

            self.shotgun_pressed = False
            self.xX_SIP_Xx = 1

            self.attack_timer = 50
            for x in range(6):
                bullet = arcade.Sprite()
                bullet.texture = arcade.load_texture("sprites/energy -1.png.png")
                bullet.scale = 0.05
                print("bing bong")

                # Position the bullet at the player's current location
                p_start_x = self.center_x
                p_start_y = self.center_y
                if self.character_face_direction == RIGHT_FACING:

                    bullet.center_x = p_start_x + 5
                    bullet.center_y = p_start_y - 30 + 8 * self.list[random.randint(0, 4)]
                    bullet.change_x = 10 + self.other_list[random.randint(0, 4)]
                    bullet.change_y = self.bullet_spread[random.randint(0, 4)]

                elif self.character_face_direction == LEFT_FACING:

                    bullet.center_x = p_start_x - 5
                    bullet.center_y = p_start_y - 30 + 8 * self.list[random.randint(0, 4)]
                    bullet.change_x = -10 + self.other_list[random.randint(0, 4)]
                    bullet.change_y = self.bullet_spread[random.randint(0, 4)]

                self.bullet_list.append(bullet)
            else:
                return

class Bullet(arcade.Sprite):  # this is the attack sprite produced when attacking
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("sprites/energy -1.png.png")
