'''
Description:
    | * This function downloads lots of images from picsum website to
    |   add them later in each image with object
    | * Before downloading it deletes all data from output/backgrounds
    | * result location -> output/backgrounds

Usage:
    | * generate_backgrounds()
        | * quantity -> number of images to download (125)
'''

def generate_backgrounds(quantity=125):
    import os

    path='../output/backgrounds'
    os.system('rm ' + path + '/*')

    for i in range(0, quantity):
        os.system('cd ' + path + ' && wget https://picsum.photos/1920/1080 && mv 1080 ' + str(i) + '.jpg' + ' && cd ../../funcs')

###########
def generate_backgrounds_bind(quantity=125):
    from bing_image_downloader import downloader
    import cv2
    import os
    search_queries = (
    "colorful wallpapers without watermark",
    "famous paintings",
    "paintings"
    )
    path='../output/backgrounds'
    for i in search_queries:
        downloader.download(i, limit=quantity,  output_dir=path, adult_filter_off=True, force_replace=False, timeout=5, verbose=True)
        path = "../output/backgrounds"
        #print(path)
        test = os.listdir(path)
        for item in test:
            # print (test +"/"+item)
            if item.endswith(".jpg"):
                im = cv2.imread(path + i +item)
                h, w, _ = im.shape
                if w!=1920 or h!=1080:
                    os.remove(os.path.join(path, item))
            else: 
                os.remove(os.path.join(path, item))         