import time
from funcs.colmap import generate_3d_model 
from funcs.blender_operations import make_transparent_images
from funcs.blender_operations import rotate_and_render
from funcs.back_collect import generate_backgrounds
from funcs.back_collect import generate_backgrounds_bind 
from funcs.back_bord import get_border
from funcs.back_bord import add_background


try:
    generate_3d_model()
except Exception as e:
    print("ERROR: problems with generating 3d model using colmap.")
    time.sleep(5)
    message = template.format(type(e).__name__, e.args)
    print(message)
    exit(-1)
try:
    make_transparent_images()
except Exception as e: 
    print("ERROR: problems with saving transparent images in bpy.")
    time.sleep(5)
    message = template.format(type(e).__name__, e.args)
    print(message)
    exit(-1)
try:
    generate_backgrounds() 
except Exception as e: 
    try:
        print ("ERROR: problems with downloading background images. Using other func downloader (bind).")
        time.sleep(5)
        message = template.format(type(e).__name__, e.args)
        print(message)
        generate_backgrounds_bind()
    except Exception as er: 
        print("ERROR: problems with downloading background images. Using default dataset (1000 images).")
        time.sleep(5)
        message = template.format(type(er).__name__, er.args)
        print(message)
        exit(-1)
try:
    get_border()
except Exception as e: 
    print("ERROR: problems with cv2 try to reinstall by: 'pip3 install opencv-python'.")
    time.sleep(5)
    message = template.format(type(e).__name__, e.args)
    print(message)
    exit(-1)
try:
    add_background()
except Exception as e: 
    print("ERROR: problems with cv2 or with images size. Check if background images have the same size as transparent image with object.")
    time.sleep(5)
    message = template.format(type(e).__name__, e.args)
    print(message)
    exit(-1)

