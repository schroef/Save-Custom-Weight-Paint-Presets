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

posList= [0.0, 0.009999999776482582, 0.5, 0.75, 1.0]
colList= [(0.31110239028930664, 0.31110239028930664, 0.31110239028930664, 1.0), (0.006538354326039553, 0.9655017256736755, 1.0, 1.0), (1.0, 0.0031068515963852406, 0.8270024657249451, 1.0), (1.0, 0.8930725455284119, 0.0038679656572639942, 1.0), (1.0, 1.0, 1.0, 1.0)]

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
prefs.view.weight_color_range.interpolation = 'CONSTANT'