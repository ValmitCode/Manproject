'''
Description:
    | * Makes images from 3d model by rotating it on transparent background
    | * 3d model location -> output/3d_model/dense/0/meshed-poisson.ply
    | * rendered photos location -> output/bpy_transparent_dataset

Requirements:
    | * CUDA 11.x
    | * bpy >= 2.8

Usage:
    | * make_transparent_images()
        | * quantity -> number of images
'''


def make_transparent_images(quantity=125):
    import bpy
    import os


    obj_path = os.path.join('../output/3d_model/dense/0', 'meshed-poisson.ply')


    bpy.data.scenes[0].render.engine = "CYCLES"

    bpy.context.preferences.addons[
        "cycles"
    ].preferences.compute_device_type = "CUDA" # or "OPENCL"

    bpy.context.scene.cycles.device = "GPU"

    bpy.context.preferences.addons["cycles"].preferences.get_devices()
    print(bpy.context.preferences.addons["cycles"].preferences.compute_device_type)
    for d in bpy.context.preferences.addons["cycles"].preferences.devices:
        d["use"] = 1 # Using all devices, include GPU and CPU
        print(d["name"], d["use"])



    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    file_loc = obj_path
    print('file_loc:', file_loc)
    bpy.ops.import_mesh.ply(filepath=file_loc)
    obj_object = bpy.context.selected_objects[0]
    print('Imported name:', obj_object.name)

    obj_name = obj_object.name

    bpy.data.objects[obj_name].location = (-0.046226635575294495, 0.12255986034870148, 1.403902530670166)
    bpy.data.objects[obj_name].rotation_euler = (3.5534353256225586, 1.4173777103424072, 1.743028163909912)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')

    bpy.data.objects[obj_name].location = (0, 0, -12)


    bpy.data.objects[obj_name].select_set(True)
    bpy.ops.paint.vertex_paint_toggle()

    bpy.context.view_layer.update()


    bpy.ops.material.new()

    mat = bpy.data.materials.get("Material")
    if len(bpy.context.active_object.data.materials) == 0:
        bpy.context.active_object.data.materials.append(bpy.data.materials['Material'])
    else:
        bpy.context.active_object.data.materials[0] = bpy.data.materials['Material']

    bpy.ops.material.new()

    bpy.context.view_layer.update()

    if mat:
        mat.node_tree.nodes.new("ShaderNodeVertexColor")
        mat.node_tree.links.new(mat.node_tree.nodes[2].outputs['Color'], mat.node_tree.nodes[1].inputs['Base Color'])


    bpy.context.view_layer.update()

    light_data = bpy.data.lights.new(name="Light_Back", type='SUN')
    light_data.energy = 0.9
    light_object = bpy.data.objects.new(name="Light_Back", object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    bpy.context.view_layer.objects.active = light_object
    light_object.location = (0, 0, 15)
    light_object.rotation_euler = (0, 0, 0)
    bpy.data.objects["Light_Back"].location = (0, 0, 20)



    bpy.data.objects["Camera"].location = (0, 0, 0)
    bpy.data.objects["Camera"].rotation_euler = (0, 0, 0)

    bpy.data.objects["Light"].location = (0, 0, 0)



    bpy.data.objects[obj_name].select_set(False)


    mat = bpy.data.materials.new(name="New_Mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')


    i = -1


    def rotate_and_render(output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 5, rotation_angle = 360.0, subject = bpy.context.object):
        import os
        import math

        ext = False
        nonlocal i
        print(i)
            

        original_rotation = subject.rotation_euler
        
        for stepx in range(0, rotation_steps):
            if ext:
                break
            
            subject.rotation_euler[0] = math.radians(stepx * (rotation_angle / rotation_steps))
            for stepy in range(0, rotation_steps):
                if ext:
                    break
                subject.rotation_euler[1] = math.radians(stepy * (rotation_angle / rotation_steps))
                for stepz in range(0, rotation_steps):
                    if ext:
                        break
                    i = i + 1
                    if quantity <= i:
                        ext = True
                        break
                    subject.rotation_euler[2] = math.radians(stepz * (rotation_angle / rotation_steps))
            
                    bpy.context.scene.render.film_transparent = True
                    bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % i))
                    bpy.context.scene.render.engine = 'CYCLES'
                    bpy.ops.render.render('INVOKE_DEFAULT', write_still = True)
                    print(i)
                    
                    
                
            
        subject.rotation_euler = original_rotation

    rotate_and_render('../output/bpy_transparent_dataset', 'render%d.png', subject = bpy.data.objects[obj_name])

