import maya.cmds as cmds

def rename(name) :
    objects = cmds.ls(selection=True)

    temp = name.count("#")
    old_name = name.replace("#" * temp, "{:0" + str(temp) + "d}")

    new_names = []

    for i, obj in enumerate(objects, start=1) :
        name_full = old_name.format(i)
        new_name = cmds.rename(obj, name_full)
        new_names.append(new_name)
        



rename('Leg_###_jnt')