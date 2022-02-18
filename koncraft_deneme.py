from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
sky_texture = load_texture('assets/skybox')
arm_texture = load_texture('')
khontkar_texture = load_texture('assets\khontkar')
kontt_texture = load_texture('assets\kontt')
kont_ses = Audio('assets/kontses',loop = False, autoplay = False)
block_pick = 1 
 

def update():
      global block_pick

      if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
      else:
        hand.passive()    

      if held_keys['1']: block_pick = 1
      if held_keys['2']: block_pick = 2


class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
        parent = scene,
        position = position,
        model = 'cube',
        origin_y = 0.5,
        texture = 'kont.kafa2',
        color = color.white,
        highlight_color =  color.lime)


      

    def input(self, key):
         if self.hovered:
             if key == 'left mouse down':
                 kont_ses.play()
                 if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = kontt_texture)
                 if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = khontkar_texture)
                 
             if key == 'right mouse down':
                 kont_ses.play()
                 destroy(self)                   




class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 200,
            double_sided = True)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = (150,-10,0),
            position = (0.5,-0.3))    
    
    def active(self):
        self.rotation = Vec3(150,-10,0)
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.5,-0.3)    





for z in range(30):
    for x in range(30):
        voxel = Voxel(position =(x,0,z))

player = FirstPersonController()
sky = Sky()        
hand = Hand()
#voxel = Voxel()

app.run()  