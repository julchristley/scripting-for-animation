import maya.cmds as cmds
import rename

class renameUI() :
    def __init__(self) :
        self.mWindow = 'ftWindow'

    def create(self) :
        self.delete()

        self.mWindow = cmds.window(self.mWindow,title="Sequential Renamer", widthHeight=(300, 400), resizeToFitChildren=True)
        mColumn = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)

        self.rnNameField = cmds.textField(parent=mColumn, placeholderText="Enter Name and number of # Here (Arm_##)")
        self.rnNumField = cmds.intField(parent=mColumn, value=1)
        self.rnNodeTypeField = cmds.textField(parent=mColumn, placeholderText="Enter Node Type Here")
        cmds.button(parent=mColumn, label="Run", command=lambda *args: self.RN_ButtonCmd())
        self.rnResult = cmds.textField(parent=mColumn, editable=False)
        cmds.showWindow(self.mWindow)

    def delete(self) :
        if(cmds.window(self.mWindow, exists=True)) :
            cmds.deleteUI(self.mWindow)
        
    def RN_ButtonCmd(self) :
        name = cmds.textField(self.rnNameField, q=True, text=True)
        num = cmds.intField(self.rnNumField, q=True, value=True)
        node_type = cmds.textField(self.rnNodeTypeField, q=True, text=True)
        
        result = rename.rename(name, num, node_type)
        cmds.textField(self.rnResult, e=True, text=result)


#what goes into the script editor

#import renameUI
#MyUI = renameUI.renameUI()
#myUI.create()