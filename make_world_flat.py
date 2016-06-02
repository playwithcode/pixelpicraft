# running this will cause lag / freeze for a few minutes!
from picraft import *
import server
import time

w = World(server.address)

w.say('Making the world flat...')
w.say('please wait - this will take a while!')
time.sleep(3) # give time for the chat to display

v1 = Vector(-128, 0, -128)
v2 = Vector(128, 64, 128)
v3 = Vector(-128, -64, -128)
v4 = Vector(128, 0, 128)

w.blocks[v1:v2 + 1] = Block('air')
w.blocks[v3:v4 + 1] = Block('sandstone')

time.sleep(3)
w.say('flat world')

