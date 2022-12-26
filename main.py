bl_info = {
    "name": "Rig Remover",
    "author": "alisahanyalcin",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "Scene Properties > Rig Remover > Remover Button",
    "description": "Remove rig from your model",
    "warning": "",
    "doc_url": "https://github.com/alisahanyalcin/Blender-Rig-Remover",
    "category": "Rig Remover",
}

import bpy


def main(context):
    bpy.ops.object.posemode_toggle()
    opsObj = bpy.ops.pose

    opsObj.select_all(action="SELECT")
    bpy.ops.pose.user_transforms_clear()

    bpy.ops.object.posemode_toggle()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    bpy.ops.object.select_by_type(type='ARMATURE')
    bpy.ops.object.delete(use_global=False, confirm=False)


class Remover(bpy.types.Operator):
    bl_idname = "object.remover"
    bl_label = "Rig Remover"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


class DrawPanel(bpy.types.Panel):
    bl_label = "Rig Remover"
    bl_idname = "Rig_Remover_Panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        btnRow = layout.row()
        btnRow.scale_y = 1.0
        btnRow.operator("object.remover", text="Remove", icon='ARMATURE_DATA')


def register():
    bpy.utils.register_class(Remover)
    bpy.utils.register_class(DrawPanel)


def unregister():
    bpy.utils.unregister_class(Remover)
    bpy.utils.unregister_class(DrawPanel)


if __name__ == "__main__":
    register()
