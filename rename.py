import maya.cmds as cmds

def rename(name, num, node_type) :
    objects = cmds.ls(selection=True)

    temp = name.count("#")
    old_name = name.replace("#" * temp, "{:0" + str(temp) + "d}")

    new_names = []

    for i, obj in enumerate(objects, start=num) :
        name_full = old_name.format(i)
        final_name = f"{name_full}_{node_type}"
        new_name = cmds.rename(obj, final_name)
        new_names.append(new_name)

        


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
        result = rename(name, num, node_type)
        cmds.textField(self.rnResult, e=True, text=result)

ui = renameUI()
ui.create()