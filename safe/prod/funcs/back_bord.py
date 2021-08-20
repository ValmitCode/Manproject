'''
    Code to find x1 y1 x2 y2 coords for object detection model xml file and adding background to transparent images for high-accuracy model. 

Description: 
(get_border):
    | * select image with transparent background from folder (path)
    | * photos location -> input/bpy_transparent_dataset
    | * going throw pixels and finding min and max for x and y non-transparent coords 
    | * TO DO write final border coords to xml file 
(add_background):
    | * select image with background from folder (path)
    | * adding background to transparent image
    | * saving all new pics to dataset for training model
'''
def get_border(path_transp):
    import os
    import cv2
    import numpy
    for item in os.listdir(path_transp):
        if item.endswith(".png"):
            img1 = cv2.imread(path_transp+'/'+item, cv2.IMREAD_UNCHANGED)

            h=img1.shape[0]
            w=img1.shape[1]

            x1=99999
            y1=-99999
            x2=-99999
            y2=99999

            for y in range (0,h):
                for x in range (0,w):
                    k=img1[y,x]
                    if k[3]!=0 and x1>x:
                        x1=x
                    if k[3]!=0 and x2<x:
                        x2=x
                    if k[3]!=0 and y1<y:
                        y1=y
                    if k[3]!=0 and y2>y:
                        y2=y    
            print (x1, y1, x2, y1)
            #Code to visualise borsers I get
            # cv2.line(img,(x1,y1),(x2,y1), (0, 0, 200, 255), 10)
            # cv2.line(img,(x2,y1),(x2,y2), (0, 0, 200, 255), 10)
            # cv2.line(img,(x2,y2),(x1,y2), (0, 0, 200, 255), 10)
            # cv2.line(img,(x1,y2),(x1,y1), (0, 0, 200, 255), 10)

    # cv2.imwrite('connected.png', img1)
def add_background(path_transp, path_back):
    import cv2 
    import os
    iter=0
    iback=0
    for item in os.listdir(path_transp):
        iter=iter+1
        if item.endswith(".png"):
            img2 = cv2.imread(path_transp+'/'+item)
        for back in os.listdir(path_back):
            iback=iback+1
            if iback==iter:
                print(iter)
                img1 = cv2.imread(path_back+'/'+back)

                brows, bcols = img1.shape[:2]
                rows,cols,channels = img2.shape
                    # Ниже я изменил roi, чтобы картинка выводилась посередине, а не в левом верхнем углу
                roi = img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
                int(cols/2):int(bcols/2)+int(cols/2) ]

                img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

                img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

                dst = cv2.add(img1_bg,img2_fg)
                img1[int(brows/2)-int(rows/2):int(brows/2)+int(rows/2), int(bcols/2)- 
                int(cols/2):int(bcols/2)+int(cols/2) ] = dst
                cv2.imwrite('./testimg/res%d.jpg' %iter,img1)
                iback=0
    
