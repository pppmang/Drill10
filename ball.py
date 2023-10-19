from pico2d import load_image

import game_world


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1): # 생성좌표 (400, 300), 속도는 1
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity # x를 velocity 만큼 이동

        if self.x < 0 or self.x > 800:    # 공이 화면에서 사라지면 해당 객체 삭제
            game_world.remove_object(self)
