import maya.cmds as cmds

objects = cmds.ls(selection=True)

for objs in objects:
    













for objs in objects:
    # querying
    position = cmds.xform(objs, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(objs, query=True, worldSpace=True, rotation=True)

    #creating group, renaming it
    group = cmds.group(empty=True, name=objs + '_Grp')
    
    # matching group to object rotation/location
    cmds.xform(group, worldSpace=True, translation=position)
    cmds.xform(group, worldSpace=True, rotation=rotation)

    #parenting object to group
    cmds.parent(objs, group)