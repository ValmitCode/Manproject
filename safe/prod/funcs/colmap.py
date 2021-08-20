'''
Description:
    | * creates 3d model from ~50 8k photos
    | * photos location -> input/imgs
    |   videos location (in .mp4 format) -> input/vids
    | * if input/vids not empty
        | * create frames from each video and write frames to input/imgs
    | * run colmap from console
        | * result writes into output/3d_model

Requirements:
    | * CUDA 11.x
    | * NVIDIA DRIVERS >= 140
    | * opencv

Usage:
    | * from colmap import generate_3d_model()
        | * path -> input path (../input)
        | * quality -> quality of 3d model {low, medium, high} (low)
        | * gpu_index -> gpu which will be used (0, 1)
        | * DEBUG -> prints info in console
'''

def generate_3d_model(path='../input', quality='low', gpu_index='0,1', DEBUG=True):
    import os
    import cv2

    videos = os.listdir(os.path.join(path, 'vids'))                     # list of videos
    count = 0                                                           # number of video's frame
    for video_name in videos:
        if video_name[-4:] != '.mp4':                                   # if file is not in mp4 format -> skip it
            continue
        if DEBUG:
            print('[Found video in]:', os.path.join(os.path.join(path, 'vids'), video_name))
        
        video = cv2.VideoCapture(os.path.join(os.path.join(path, 'vids'), video_name))

        success,image = video.read()
        while success:
            cv2.imwrite("../input/imgs/frame%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = video.read()
            if DEBUG:
                print('Read a new frame', count, ': ', success)
            count += 1

    if DEBUG:
        print('[Running command]:', 'colmap automatic_reconstructor --workspace_path ' + '../output/3d_model' + ' --image_path ' + os.path.join(path, 'imgs') + ' --quality ' + quality + ' --dense 1 --gpu_index=' + gpu_index)
    os.system('colmap automatic_reconstructor --workspace_path ' + '../output/3d_model' + ' --image_path ' + os.path.join(path, 'imgs') + ' --quality ' + quality + ' --dense 1 --gpu_index=' + gpu_index)


generate_3d_model()