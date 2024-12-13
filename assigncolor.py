import maya.cmds as cmds

def change_colors(color) :

    objects = cmds.ls(selection=True)

    for obj in objects : 
        shape = cmds.listRelatives(obj, shapes=True, fullPath=True)

        cmds.setAttr(f'{shape[0]}.overrideEnabled', 1)
        cmds.setAttr(f'{shape[0]}.overrideColor', color)
