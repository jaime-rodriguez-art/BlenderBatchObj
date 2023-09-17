import bpy
import os

script_directory = os.path.dirname(bpy.data.filepath)

output_directory = os.path.join(script_directory, "exported_objs")

os.makedirs(output_directory, exist_ok=True)

for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        output_file = os.path.join(output_directory, obj.name + ".obj")
        
        bpy.ops.export_scene.obj(
            filepath=output_file,
            use_selection=True,
            use_materials=False  
        )
        
        obj.select_set(False)

print("Exported all objects as .obj files to", output_directory)