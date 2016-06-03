from picraft import *
import server
import random


w = World(server.address)

w.say('setting X Y frame')

size = 16

# choose which parts to put blocks for
put_fill = True
put_corners = True
put_edges = True

# choose what blocks to use
fill_block = Block('air')
corner_block = Block('wool', random.randint(0, 16))
edge_block = Block('wool', random.randint(0, 16))

# # # # # # # # # # # # # # # #

#  two Vectors set the framed area
v1 = Vector(w.player.tile_pos.x + 2,
            w.player.tile_pos.y + 1,
            w.player.tile_pos.z)
v2 = v1 + (X * size) + (Y * size)

#  four corner block Vectors
c1 = v1 - X - Y
c2 = v1 - X + (Y * (size+1))
c3 = v2 + X + Y
c4 = v2 + X - (Y * (size+1))

#  put block to fill the frame?
if put_fill:
    w.blocks[v1:v2 + Z] = fill_block

#  put the edges?
if put_edges:
    w.blocks[c1:c2 + 1] = edge_block
    w.blocks[c2:c3 + 1] = edge_block
    w.blocks[c4:c3 + 1] = edge_block
    w.blocks[c1:c4 + 1] = edge_block

#  put the corners?
if put_corners:
    w.blocks[c1] = corner_block
    w.blocks[c2] = corner_block
    w.blocks[c3] = corner_block
    w.blocks[c4] = corner_block