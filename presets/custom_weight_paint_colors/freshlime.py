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

posList= [0.0, 0.009999999776482582, 0.37141817808151245, 0.7328363656997681, 1.0]
colList= [(0.31110239028930664, 0.31110239028930664, 0.31110239028930664, 1.0), (0.04803777486085892, 0.1857939064502716, 1.0, 1.0), (0.004202490672469139, 0.5928969383239746, 0.11618726700544357, 1.0), (0.7453177571296692, 1.0, 0.004896974191069603, 1.0), (1.0, 1.0, 1.0, 1.0)]

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