import maya.cmds as cmds
import maya.cmds as cmds

def change_colors(color) :

    objects = cmds.ls(selection=True)

    for obj in objects : 
        shape = cmds.listRelatives(obj, shapes=True, fullPath=True)

        cmds.setAttr(f'{shape[0]}.overrideEnabled', 1)
        cmds.setAttr(f'{shape[0]}.overrideColor', color)

change_colors()  #gotta put a number in there

# 0 = default (dark blue), 1 = black, 2 = dark gray, 3 = light gray, 4 = red, 5 = dark blue (default)
# 6 = light blue, 7 = dark green, 8 = dark purple, 9 = pinkish purple, 10 = brown
# 11 = dark brown, 12 = dark orange, 13 = orange, 14 = grass green, 15 = blue
# 16 = white, 17 = yellow, 18 = light blue, 19 = pastel green, 20 = pastel pink
# 21 = tan, 22 = pastel yellow (looks exactly the same as the other yellow), 23 = dark pastel green, 24 = peach, 25 = sunny yellow
# 26 = pea green, 27 = teal green, 28 = lighter sky blue, 29 = darker sky blue, 30 = light purple, 31 = pinkS