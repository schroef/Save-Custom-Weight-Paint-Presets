import bpy
prefs = bpy.context.preferences

colRangeElm = prefs.view.weight_color_range.elements
# Clean old Color Ramp
#if bpy.app.version <= (2,93):
for elm in range(len(colRangeElm)):
    totElm = len(colRangeElm)
    # Add 2 points if complete empty
    if totElm == 0:
        colRangeElm.new(position=[1,1])
        colRangeElm.new(position=[0,0])
    #First delete all export first and list
    if totElm > 2:
        for i in range(1,totElm-1):
            colRangeElm.remove(colRangeElm[elm])
        #Reset first and last to 0,0 and 1,1
        resetLst = [0.0,1.0]
        for i in range(2):
            colRangeElm[i].position=resetLst[i]

posList= [0.0, 0.009999999776482582, 0.2549999952316284, 0.5, 0.75, 1.0]
colList= [(0.31110239028930664, 0.31110239028930664, 0.31110239028930664, 1.0), (0.04803777486085892, 0.1857939064502716, 1.0, 1.0), (1.0, 0.0, 0.000371000001905486, 1.0), (1.0, 0.0, 0.00037143140798434615, 1.0), (1.0, 0.7384565472602844, 0.009093190543353558, 1.0), (1.0, 1.0, 1.0, 1.0)]

for i in range(len(colList)):
    # Update first and last > dont add new
    if i == 0 or i == (len(colList)):
        colRangeElm[i].color = colList[i]
        colRangeElm[i].position=float(posList[i])
    else:
        colRangeElm.new(position=float(posList[i]))
        colRangeElm[i].color = colList[i]



prefs.view.use_weight_color_range = True
prefs.view.weight_color_range.color_mode = 'RGB'
