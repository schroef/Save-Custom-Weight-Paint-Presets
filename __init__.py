#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""
Custom Weight Paint Presets

Save your Custom Weight Paint colors as presets, for easy re-use.

"""

bl_info = {
    "name": "Save Custom Weight Paint Presets",
    "author": "Rombout Versluijs",
    "version": (0,0,9),
    "blender": (2, 83, 0),
    "location": "Preferences > Editting > Weight Paint",
    "description": "Save custom color ramps for weight painting",
    "tracker_url": "https://github.com/schroef/Save-Custom-Weight-Paint-Presets/issues",
    "doc_url": "https://github.com/schroef/Save-Custom-Weight-Paint-Presets",
    "category": "Preferences",
}



import bpy, os
from shutil import Error
from . presets import AddPresetBase

class SCWPP_PREFS_MT_weight_paint_presets(bpy.types.Menu):

    """List of Weight Paint presets"""
    bl_label = "Weight Paint Presets"

    # script_file = os.path.realpath(__file__)
    # directory = os.path.dirname(script_file)
    # target_path = os.path.join(directory,"presets\\")
    # target_path = directory
    # searchpaths= str(target_path)

    # preset_subdir = str('C:/Users/romboutversluijs/AppData/Roaming/Blender Foundation/Blender/2.91/scripts/addons/Save-Custom-Weight-Paint-Presets/presets/')
    # preset_subdir = "presets"
    # Addon preset path
    # prop_filepath= target_path

    preset_subdir = "custom_weight_paint_colors"

    preset_operator = "script.execute_preset"
    draw = bpy.types.Menu.draw_preset


class SCWPP_AddPresetWeightPaint(AddPresetBase, bpy.types.Operator):

    """Add or remove a Weight Paint preset"""
    bl_idname = "preferences.weight_paint_preset_add"
    bl_label = "Add Weight Paint Preset"
    preset_menu = "SCWPP_PREFS_MT_weight_paint_presets"

    preset_defines = [
        "prefs = bpy.context.preferences",
    ]

    preset_values = [
        "prefs.view.use_weight_color_range",
        "prefs.view.weight_color_range.color_mode",
        "prefs.view.weight_color_range.interpolation",
    ]

    preset_subdir = "custom_weight_paint_colors"
    # preset_subdir = "custom_weight_paint_colors"


# def drawcentered(self, context, layout):
#     layout = self.layout
#     width = context.region.width
#     ui_scale = context.preferences.system.ui_scale
#     # No horizontal margin if region is rather small.
#     is_wide = width > (350 * ui_scale)

#     layout.use_property_split = True
#     layout.use_property_decorate = False  # No animation.

#     row = layout.row()
#     if is_wide:
#         row.label()  # Needed so col below is centered.

#     col = row.column()
#     col.ui_units_x = 50

#     # Implemented by sub-classes.
#     self.draw_centered(context, col)

#     if is_wide:
#         row.label()  # Needed so col above is centered.

def install_presets():
    # https://www.geeksforgeeks.org/how-to-move-files-and-directories-in-python/
    import shutil
    

    # Source path
    cwppFold = "custom_weight_paint_colors"
    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(script_file)
    presetSrc = os.path.join("presets", cwppFold) 
    source = os.path.join(directory, presetSrc)
    

    # Possible fix for bl3.0
    # fix for user_resource error > from store_vieews
    # https://git.blender.org/gitweb/gitweb.cgi/blender-addons.git/blob/HEAD:/space_view3d_stored_views/stored_views_test.py
            
    # paths = bpy.utils.preset_paths("stored_views")
        # if not paths:
            # stored_views preset folder doesn't exist, so create it
            # paths = [os.path.join(bpy.utils.user_resource('SCRIPTS'), "presets","stored_views")]

    # other fix from eevee_presets
    # from pathlib import Path
    # user_path = Path(bpy.utils.resource_path('USER'))
    # preset_path = user_path / Path(f"scripts/presets/{PRESET_SUBDIR}")

    # bl3 fix > https://blender.stackexchange.com/a/245232/7631
    # Destination path 
    if bpy.app.version[0] >= 3:
        destination = bpy.utils.user_resource('SCRIPTS',path="presets/",create=True)
    else:
        destination = bpy.utils.user_resource('SCRIPTS',"presets/",create=True)


    # Move the content of
    # source to destination
    # print("Dest %s" % os.path.isdir(os.path.join(destination,cwppFold)))
    destPath = os.path.isdir(os.path.join(destination,cwppFold))
    try: 
        # dest = shutil.move(source, destination, copy_function = shutil.copytree(source, destination,dirs_exist_ok=False))
        # dest = shutil.move(source, destination, copy_function=shutil.copy2) # copy_function = shutil.copytree(source, destination,dirs_exist_ok=False))
        print(source)
        print(os.path.isdir(source))
        if os.path.isdir(source) or destPath:
            dest = shutil.move(source, destination, copy_function = shutil.copytree)
            if dest:
                print("Weight Paint presets installed")
        else:
            print("Weight Paint Preset already installed")
    except Error:
        print("Issue Save-Custom-WeightPaint_presets \n %s" % Error)
        


def brush_weight_paint(self, context):
    '''
    bpy.ops.paint.weight_paint_toggle()
    PAINT_OT_BRUSH_SELECT.weight_tool()
    '''
    layout = self.layout
    tool_mode = context.mode
    layout.use_property_split = True
    layout.use_property_decorate = False

    tool_settings = context.tool_settings
    wpaint = tool_settings.weight_paint

    if tool_mode == 'PAINT_WEIGHT':
        col = layout.column()
        sub = col.split()

        sub.separator()
        sub.operator("paint.brush_select", text="Draw").weight_tool='DRAW'
        sub.operator("paint.brush_select", text="Blur").weight_tool='BLUR'
        sub.operator("paint.brush_select", text="Average").weight_tool='AVERAGE'
        sub.operator("paint.brush_select", text="Smear").weight_tool='Smear'
        # sub.operator("paint.brush_select", text="Gradient").weight_tool='GRADIENT'


def tool_weight_paint_presets(self, context):
    layout = self.layout
    tool_mode = context.mode
    layout.use_property_split = True
    layout.use_property_decorate = False

    tool_settings = context.tool_settings
    wpaint = tool_settings.weight_paint

    if tool_mode == 'PAINT_WEIGHT':
        col = layout.column()
        row = col.split(factor=0.33)
        row.label(text="Weightpaint")
        sub = row.row()
        sub.menu("SCWPP_PREFS_MT_weight_paint_presets",
                text=bpy.types.SCWPP_PREFS_MT_weight_paint_presets.bl_label)


def ui_weight_paint_presets(self, context):
    layout = self.layout
    width = context.region.width
    prefs = context.preferences
    ui_scale = prefs.system.ui_scale
    # No horizontal margin if region is rather small.
    is_wide = width > (350 * ui_scale)

    layout.use_property_split = True
    layout.use_property_decorate = False  # No animation.

    if prefs.view.use_weight_color_range:
        layout.separator()
        row = layout.row()
        if is_wide:
            row.label()  # Needed so col below is centered.

        col = row.column()
        col.ui_units_x = 50

        sub = col.row(align=True)
        # sub.label(text="Presets")
        sub.menu("SCWPP_PREFS_MT_weight_paint_presets",
                text=bpy.types.SCWPP_PREFS_MT_weight_paint_presets.bl_label)
        sub.operator("preferences.weight_paint_preset_add", text="", icon="ADD")
        sub.operator("preferences.weight_paint_preset_add",
                    text="", icon="REMOVE").remove_active = True
        
        if is_wide:
            row.label()  # Needed so col above is centered.


def register():
    # bpy.utils.register_class(CenterAlignMixIn)
    bpy.utils.register_class(SCWPP_AddPresetWeightPaint)
    bpy.utils.register_class(SCWPP_PREFS_MT_weight_paint_presets)
    bpy.types.USERPREF_PT_edit_weight_paint.append(ui_weight_paint_presets)
    bpy.types.VIEW3D_PT_paint_weight_context_menu.append(brush_weight_paint)
    bpy.types.VIEW3D_PT_overlay_weight_paint.append(tool_weight_paint_presets)
    bpy.types.VIEW3D_PT_tools_weightpaint_options.append(tool_weight_paint_presets)
    install_presets()


def unregister():
    # bpy.utils.unregister_class(CenterAlignMixIn)
    bpy.utils.unregister_class(SCWPP_AddPresetWeightPaint)
    bpy.utils.unregister_class(SCWPP_PREFS_MT_weight_paint_presets)
    bpy.types.USERPREF_PT_edit_weight_paint.remove(ui_weight_paint_presets)
    bpy.types.VIEW3D_PT_paint_weight_context_menu.remove(brush_weight_paint)
    bpy.types.VIEW3D_PT_overlay_weight_paint.remove(tool_weight_paint_presets)
    bpy.types.VIEW3D_PT_tools_weightpaint_options.remove(tool_weight_paint_presets)
