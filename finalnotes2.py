import maya.cmds as cmds
import finalnotes

class FortuneUI() :
    def __init__(self) :
        self.mWindow = 'ftWindow'


    def create(self) :
        self.delete()

        self.mWindow = cmds.window(self.mWindow, title="Fortune Teller", widthHeight=(300, 400), resizeToFitChildren=True)
        mColumn = cmds.columnLayout(parent=self.mWindow, adjustableColumn=True)
        
        self.ftNameField= cmds.textField(parent=mColumn, placeholderText="Enter name here...")
        self.ftYearField = cmds.intField(parent=mColumn)
        self.ftOperation = cmds.radioButtonGrp(parent=mColumn, 
                                            numberOfRadioButtons=4, 
                                            labelArray4=("Lucky Numbers", "Best Friend", "Fortune Cookie", "Zodiac Sign"))
        cmds.button(parent=mColumn, label="GO!", command=lambda *args: self.FT_ButtonCmd())
        self.ftResult = cmds.textField(parent=mColumn, editable=False)
        cmds.showWindow(self.mWindow)


    def delete(self) :
        if(cmds.window(self.mWindow, exists=True)) :
            cmds.deleteUI(self.mWindow)


    def FT_ButtonCmd(self) :
        name = cmds.textField(self.ftNameField, q=True, text=True)
        year = cmds.intField(self.YearField, q=True, value=True)
        oper = cmds.radioButtonGrp(self.ftOperation, q=True, select=True)

        result = finalnotes.FortuneTeller(name, year, oper)
        cmds.textField(self.ftResult, e=True, text=result)


myUI = FortuneUI()
myUI.create()