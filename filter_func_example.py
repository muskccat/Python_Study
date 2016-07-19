import maya.cmds as cmds

cms = cmds.ls(typ='camera')
cmt = lambda x:cmds.listRelatives(x,p=True)

cm_list = filter(lambda x:not(cmds.getAttr(x+".orthographic")) , cms)
cmt = cmt(cm_list)


print cmt