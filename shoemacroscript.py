#makes a shoe

import maya.cmds as mc


# making the sole
sole1 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 1.5, 2.568, relative=True)
mc.scale(4, 1, 4, relative=True)

sole2 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 1.5, -1.915, relative=True)
mc.scale(4, 1, 3, relative=True)

sole3 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 2.5, 0.578, relative=True)
mc.scale(4, 1, 8, relative=True)


# top part
top1 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 3.75, 0.537, relative=True)
mc.scale(3.6, 1.5, 7.5, relative=True)

top2 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 4.97, 0.259, relative=True)
mc.scale(3.2, 1, 7, relative=True)

top3 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)[0]
mc.move(0, 5.971, -1.447, relative=True)
mc.scale(3.2, 1, 3.6, relative=True)


# slanting
mc.select(top1 + ".e[1]")
mc.move(0,-0.0267067, -0.539584, relative=True, objectSpace=True, worldSpaceDistance=True)

mc.select(top1 + ".e[7]")
mc.move(-0.215817, 0, 0, relative=True, objectSpace=True, worldSpaceDistance=True)
mc.select(top1 + ".e[6]")
mc.move(0.206596, 0, 0, relative=True, objectSpace=True, worldSpaceDistance=True)

mc.select(top2 + ".e[1]")
mc.move(0, 0, -3.411145, relative=True, objectSpace=True, worldSpaceDistance=True)

mc.select(top3 + ".e[2]")
mc.move(0, -0.583573, 0, relative=True, objectSpace=True, worldSpaceDistance=True)


#laces
lace1 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
mc.move(0, 5.235, 0.920, relative=True)
mc.scale(3.5, 0.5, 0.5, relative=True)

lace2 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
mc.move(0, 4.954, 1.899, relative=True)
mc.scale(3.5, 0.5, 0.5, relative=True)

lace3 = mc.polyCube(width=1, height=1, depth=1, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=[0, 1, 0], createUVs=4, constructionHistory=1)
mc.move(0, 4.631, 2.927, relative=True)
mc.scale(3.5, 0.5, 0.5, relative=True)

mc.select([lace1[0], lace2[0], lace3[0]])
mc.rotate(22.195695, 0, 0, relative=True, objectSpace=True, forceOrderXYZ=True)