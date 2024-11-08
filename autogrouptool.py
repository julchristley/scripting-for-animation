import maya.cmds as cmds

objects = cmds.ls(selection=True)

for objs in objects:
    position = cmds.xform(objs, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(objs, query=True, worldSpace=True, rotation=True)

    gname = objs + '_Grp'
    group = cmds.group(empty=True, name=gname)
    cmds.xform(group, worldSpace=True, translation=position)
    cmds.xform(group, worldSpace=True, rotation=rotation)

    cmds.parent(objs, group)

    cmds.makeIdentity(objs, apply=True, translate=True, rotate=True, scale=True, normal=False)