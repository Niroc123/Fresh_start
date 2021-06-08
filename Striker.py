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


class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.attack_timer = 0
        self.chez = 0
        self.cur_texture = 0
        self.cur_attack_texture = 0
        self.character_face_direction = RIGHT_FACING
        self.scale = SPRITE_SCALING_PLAYER

        self.health = 100

        self.bam = True
        self.pressed = True
        self.jumping = False


        self.idle_texture_pair = load_texture_pair("Sprites/Characters/Striker/Striker_idle.png")
        self.jump_texture_pair = load_texture_pair("Sprites/Characters/Jumping.png")


        # walking left and right
        self.walk_textureslr = []
        for i in range(5):
            texture = load_texture_pair("Sprites/Characters/Striker/Striker Running" + str(i) + ".png")
            self.walk_textureslr.append(texture)

        self.attack_texture = []
        for i in range(3):
            texture = load_texture_pair("Sprites/Characters/Striker/punch" + str(i) + ".png")
            self.attack_texture.append(texture)

        self.texture = self.idle_texture_pair[0]

    def on_key_press(self, key: int):

        if key == arcade.key.KEY_1:

            if self.attack_timer == 0 or self.attack_timer < 0:
                self.pressed = False
                #print("1")
                print(f'pressed:{self.pressed}')

    def on_key_release(self, key: int):

        if key == arcade.key.KEY_1:

            print(f'releaded press:{self.pressed}')

    def on_draw(self):
        return


    def update_animation(self, delta_time: float = 1/60):
        #print(self.pressed)
        #print(self.chez)


        if self.attack_timer > 0:
            self.attack_timer -= 1

        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        if self.change_x == 0 and self.change_y == 0 and self.pressed:
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


        if not self.pressed:

            self.chez += delta_time

            print("check345")

            if self.chez >= 1/120:
                self.chez = 0
                self.cur_attack_texture += 1
                if self.cur_attack_texture > 2 * ATTACK_UPDATES_PER_FRAME:
                    self.cur_attack_texture = 0
                    self.pressed = True
                    self.attack_timer = 20
                self.texture = self.attack_texture[self.cur_attack_texture // ATTACK_UPDATES_PER_FRAME][
                    self.character_face_direction]















