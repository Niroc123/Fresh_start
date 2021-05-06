import arcade

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


class SniperCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.xX_SIP_Xx = 0
        self.cur_texture = 0
        self.cur_attack_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.scale = SPRITE_SCALING_PLAYER

        self.bam = False
        self.sniper_pressed = True
        self.jumping = False


        self.idle_texture_pair = load_texture_pair("Sprites/Characters/Shotgunner/Shotgun_idle.png")
        self.jump_texture_pair = load_texture_pair("Sprites/Characters/Jumping.png")

        # walking left and right
        self.walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Shotgunner/Shotgun running" + str(i) + ".png")
            self.walk_textureslr.append(texture)

        self.attack_texture = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Shotgunner/Shotgun_attack" + str(i) + ".png")
            self.attack_texture.append(texture)

        self.texture = self.idle_texture_pair[0]

    def on_key_press(self, key: int):

        if key == arcade.key.M:
            self.sniper_pressed = False
            self.xX_SIP_Xx = 1
            #print("1")
            print(f'pressed:{self.sniper_pressed}')

    def on_key_release(self, key: int):

        if key == arcade.key.M:
            self.sniper_pressed = False
            print(f'releaded press:{self.sniper_pressed}')





    def update_animation(self, delta_time: float = 1/60):
        #print(self.pressed)
        #print(self.chez)
        """if self.pressed:

            self.bam = True
            print(self.bam)"""



        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0 and self.sniper_pressed:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            return

        if self.change_x < 0 or self.change_x > 0:
            # Walking animation
            self.cur_texture += 1
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.walk_textureslr[self.cur_texture // UPDATES_PER_FRAME][self.character_face_direction]

        if self.change_y > 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return
        elif self.change_y < 0:
            self.texture = self.jump_texture_pair[self.character_face_direction]
            return


        if not self.sniper_pressed:

            self.xX_SIP_Xx += delta_time

            print("Head Shot")

            if self.xX_SIP_Xx >= 1/60:
                self.xX_SIP_Xx = 0
                self.cur_attack_texture += 1
                if self.cur_attack_texture > 4 * ATTACK_UPDATES_PER_FRAME:
                    self.cur_attack_texture = 0
                    self.sniper_pressed = True
                    self.attack_timer = 20
                self.texture = self.attack_texture[self.cur_attack_texture // ATTACK_UPDATES_PER_FRAME][
                    self.character_face_direction]
