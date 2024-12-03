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
    group = cmds.group(empty=True, name=new_name)
    
    # matching group to object rotation/location
    cmds.xform(group, worldSpace=True, translation=position)
    cmds.xform(group, worldSpace=True, rotation=rotation)

    nurbs_control = cmds.circle(name=new_name, normal=(1,0,0))[0]
    #parenting object to group

    cmds.xform(nurbs_control, worldSpace=True, translation=position)
    cmds.xform(nurbs_control, worldSpace=True, rotation=rotation)

    cmds.parent(nurbs_control, group)



import maya.cmds as cmds

def create_control() :
    sels = cmds.ls(sl=True)

    for sel in sels:
        sel_position = cmds.xform(sel, q=True, ws=True, translation=True)
        sel_rotation = cmds.xform(sel, q=True, ws=True, rotation=True)

    new_ctrl = cmds.circle(center=(0,0,0), normal=(1,0,0), sweep=360, radius=1, d=3, ut=False, tol=0.01, s=8, ch=True)[0]
    cmds.xform(new_ctrl, ws=True, translation=sel_position)
    cmds.xform(new_ctrl, ws=True, rotation=sel_position)

    new_group = cmds.group(empty=True, world=True)
    cmds.xform(new_group, ws=True, translation=sel_position)
    cmds.xform(new_group, ws=True, rotation=sel_position)

    cmds.parent(new_ctrl, new_group)

    name, temp_var, suffix = sel.rpartition('_')
    if suffix.lower() not in ['jnt', 'geo'] :
        name = sel

    new_ctrl = cmds.rename(new_ctrl, '%s_Ctrl' % name)
    new_group = cmds.rename(new_group, '%s_Grp' %new_ctrl)

create_control()