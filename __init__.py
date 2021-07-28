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
    "version": (0,0,3),
    "blender": (2, 83, 0),
    "location": "Preferences > Editting > Weight Paint",
    "description": "Save custom color ramps for weight painting",
    "warning": "https://github.com/schroef/Save-Custom-Weight-Paint-Presets/issues",
    "doc_url": "https://github.com/schroef/Save-Custom-Weight-Paint-Presets",
    "category": "Preferences",
}



import bpy, os
from . presets import AddPresetBase

# from bl_ui.space_userpref import CenterAlignMixIn

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
    source = "presets/custom-weight-paint-presets"
    
    # Destination path
    destination = "presets/"
    
    # Move the content of
    # source to destination
    dest = shutil.move(source, destination, copy_function = shutil.copytree)
    
    # print(dest) prints the
    # Destination of moved directory


def tool_weight_paint_presets(self, context):
    layout = self.layout
    tool_mode = context.mode
    layout.use_property_split = True
    layout.use_property_decorate = False

    tool_settings = context.tool_settings
    wpaint = tool_settings.weight_paint

    if tool_mode == 'PAINT_WEIGHT':
        # row = layout.row(align=True)
        # row = layout.column(align=True)
        layout.row().menu("SCWPP_PREFS_MT_weight_paint_presets",
                text=bpy.types.SCWPP_PREFS_MT_weight_paint_presets.bl_label)

def ui_weight_paint_presets(self, context):
    layout = self.layout

    row = layout.row(align=True)
    # row = layout.column(align=True)
    row.menu("SCWPP_PREFS_MT_weight_paint_presets",
             text=bpy.types.SCWPP_PREFS_MT_weight_paint_presets.bl_label)
    row.operator("preferences.weight_paint_preset_add", text="", icon="ADD")
    row.operator("preferences.weight_paint_preset_add",
                 text="", icon="REMOVE").remove_active = True
    layout.separator()


def register():
    bpy.utils.register_class(SCWPP_AddPresetWeightPaint)
    bpy.utils.register_class(SCWPP_PREFS_MT_weight_paint_presets)
    bpy.types.USERPREF_PT_edit_weight_paint.prepend(ui_weight_paint_presets)
    # bpy.types.VIEW3D_HT_tool_header.append(tool_weight_paint_presets)
    bpy.types.VIEW3D_PT_tools_weightpaint_options.append(tool_weight_paint_presets)


def unregister():
    bpy.utils.unregister_class(SCWPP_AddPresetWeightPaint)
    bpy.utils.unregister_class(SCWPP_PREFS_MT_weight_paint_presets)
    bpy.types.USERPREF_PT_edit_weight_paint.remove(ui_weight_paint_presets)
    # bpy.types.VIEW3D_HT_tool_header.remove(tool_weight_paint_presets)
    # bpy.types.VIEW3D_HT_tool_header.remove(tool_weight_paint_presets)
    bpy.types.VIEW3D_PT_tools_weightpaint_options.remove(tool_weight_paint_presets)
