import maya.cmds as cmds

objects = cmds.ls(selection=True)

for objs in objects:
    # querying
    position = cmds.xform(objs, query=True, worldSpace=True, translation=True)
    rotation = cmds.xform(objs, query=True, worldSpace=True, rotation=True)

    if objs.endswith("_Jnt") :
        new_name = objs.replace("_Jnt", "_Ctrl")
    elif objs.endswith("_Geo"):
        new_name = objs.replace("Geo", "Ctrl")

    #creating group, renaming it
    group = cmds.group(empty=True, name=group_name)
    
    # matching group to object rotation/location
    cmds.xform(group, worldSpace=True, translation=position)
    cmds.xform(group, worldSpace=True, rotation=rotation)

    nurbs_control = cmds.circle(name=new_name, normal=(1,0,0))[0]
    #parenting object to group

    cmds.xform(nurbs_control, worldSpace=True, translation=position)
    cmds.xform(nurbs_control, worldSpace=True, rotation=rotation)

    cmds.parent(nurbs_control, group)