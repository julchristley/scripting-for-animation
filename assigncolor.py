import maya.cmds as cmds

def change_colors(color) :

    objects = cmds.ls(selection=True)

    for obj in objects : 
        shape = cmds.listRelatives(obj, shapes=True, fullPath=True)

        cmds.setAttr(f'{shape[0]}.overrideEnabled', 1)
        cmds.setAttr(f'{shape[0]}.overrideColor', color)




import maya.cmds as cmds

class Change_Colors_UI() :
    def __init__(self) :
        self.mWindow = 'ftWindow'

    def create(self) :
        self.delete()

        self.mWindow = cmds.window(self.mWindow, title="Change Colors", widthHeight=(300, 400), resizeToFitChildren=True)
        mColumn = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)

        self.button1 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("default (dark blue)", "black", "dark gray", "light gray"))
        self.button2 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("red", "dark blue (default)", "light blue", "dark green"))
        self.button3 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("dark purple", "pinkish purple", "brown", "dark brown"))
        self.button4 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("dark orange", "orange", "grass green", "blue"))
        self.button5 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("white", "yellow", "light blue", "pastel green"))
        self.button6 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("pastel pink", "tan", "pastel yellow", "dark pastel green"))
        self.button7 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("peach", "sunny yellow", "pea green", "teal green"))
        self.button8 = cmds.radioButtonGrp(parent=mColumn,
                                            numberOfRadioButtons=4,
                                            labelArray4=("lighter sky blue", "darker sky blue", "light purple", "pink"))
        cmds.button(parent=mColumn, label="Run", command=lambda *args: self.CC_ButtonCmd())
        self.CCResult = cmds.textField(parent=mColumn, editable=False)
        cmds.showWindow(self.mWindow)

    def delete(self) :
        if(cmds.window(self.mWindow, exists=True)) :
            cmds.deleteUI(self.mWindow)

    def CC_ButtonCmd(self) :
        but1 = cmds.radioButtonGrp(self.button1, q=True, select=True)
        but2 = cmds.radioButtonGrp(self.button2, q=True, select=True)
        but3 = cmds.radioButtonGrp(self.button3, q=True, select=True)
        but4 = cmds.radioButtonGrp(self.button4, q=True, select=True)
        but5 = cmds.radioButtonGrp(self.button5, q=True, select=True)
        but6 = cmds.radioButtonGrp(self.button6, q=True, select=True)
        but7 = cmds.radioButtonGrp(self.button7, q=True, select=True)
        but8 = cmds.radioButtonGrp(self.button8, q=True, select=True)

        all_buttons = [but1, but2, but3, but4, but5, but6, but7, but8]
        
        color_map = [   
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23],
            [24, 25, 26, 27],
            [28, 29, 30, 31]
        ]

        for i, selection in enumerate(all_buttons):
            if selection and i < len(color_map):
                color = color_map[i][selection - 1]  
                change_colors(color)

ui = Change_Colors_UI()
ui.create()