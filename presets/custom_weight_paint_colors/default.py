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
    if totElm > 1:
        colRangeElm.remove(colRangeElm[totElm-1])
#Reset first to 0,0
colRangeElm[0].position=float(0.0)

posList= [0.0, 0.10000000149011612, 0.25, 0.5, 0.75, 1.0]
colList= [(0.31110239028930664, 0.31110239028930664, 0.31110239028930664, 1.0), (0.02038206160068512, 0.07970469444990158, 1.0, 1.0), (0.0662011206150055, 1.0, 0.011089849285781384, 1.0), (0.882996678352356, 1.0, 0.008982541039586067, 1.0), (0.9086891412734985, 0.5, 0.004491270519793034, 1.0), (0.9343815445899963, 0.0, 0.0, 1.0)]

for i in range(0,len(colList)):
    # Update first and last > dont add new
    if i == 0 or i == (len(colList)):
        colRangeElm[i].color = colList[i]
        colRangeElm[i].position=float(posList[i])
    else:
        colRangeElm.new(position=float(posList[i]))
        colRangeElm[i].color = colList[i]



prefs.view.use_weight_color_range = True
prefs.view.weight_color_range.color_mode = 'RGB'
prefs.view.weight_color_range.interpolation = 'LINEAR'