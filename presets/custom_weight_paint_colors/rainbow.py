import bpy
prefs = bpy.context.preferences

colRange = prefs.view.weight_color_range
colRangeElm = prefs.view.weight_color_range.elements

prefs.view.use_weight_color_range = True
prefs.view.weight_color_range.color_mode = 'RGB'

# Dirty delete < 2.92 doesnt have operator
#if bpy.app.version <= (2,93):
for elm in range(len(colRangeElm)):
    totElm = len(colRangeElm)
    #First delete all export first and list
    if totElm == 0:
        colRangeElm.new(position=[1,1])
        colRangeElm.new(position=[0,0])
    if totElm > 2:
        for i in range(1,totElm-1):
            colRangeElm.remove(colRangeElm[elm])
        #Reset first and last to 0,0 and 1,1
        resetLst = [0.0,1.0]
        for i in range(2):
            colRangeElm[i].position=resetLst[i]

posList=[0.0, 0.009999999776482582, 0.5, 0.8999999761581421, 1.0]
colList=[(0.31110239028930664, 0.31110239028930664, 0.31110239028930664, 1.0), (0.04803777486085892, 0.1857939064502716, 1.0, 1.0), (1.0, 0.0, 0.00037143140798434615, 1.0), (1.0, 0.7384565472602844, 0.009093190543353558, 1.0), (1.0, 1.0, 1.0, 1.0)]
#print("list %s" % len(colList))
for i in range(len(colList)):
   # Update first and last > dont add new
   if i == 0 or i == (len(colList)):
#        print(colList[i])
        colRangeElm[i].color = colList[i]
        colRangeElm[i].position=float(posList[i])
   else:
        colRangeElm.new(position=float(posList[i]))
        colRangeElm[i].color = colList[i]