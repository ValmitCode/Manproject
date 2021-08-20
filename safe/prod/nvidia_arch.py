#ssd_folder
def nvidia_tree(dataset_name='objects', classes=['chips']):
    import os
    try:
        #os.chdir('../..')
        os.chdir(dataset_name)
    except Exception as e:
        os.chdir('../..')
        os.mkdir(dataset_name)
        os.chdir(dataset_name)
        file = open("labels.txt","w")
        for item in classes:
            file.write("%s\n" % item)
        file.close()    
        os.mkdir('Annotations')
        os.system("cp /data/prod/output/xmls*.xml /data/"+dataset_name+"/Annotations")
        os.mkdir('ImageSets')
        os.chdir('ImageSets')
        os.mkdir('Main')
        os.chdir('Main')
        file1 = open("train.txt", "w")
        file2 = open("trainval.txt", "w")
        os.chdir('../..')
        os.mkdir('JPEGImages')
        os.system("cp /data/prod/output/dataset*.jpg /data/"+dataset_name+"/JPEGImages")
        for filename in os.listdir('JPEGImages'):
            file1.write("%s\n" % filename)
            file2.write("%s\n" % filename)
        file1.close()  
        file2.close()
def nvidia_train(dataset_name='objects', classes=['chips'], batch_size=2, workers=1, epochs=10, showresult=True, device='dev/video1'):
    import os
    os.chdir('..')
    train="python3 train_ssd.py --dataset-type=voc --data=data/"+dataset_name+" --model-dir=models/"+dataset_name+" --batch-size="+batch_size+" --workers="+workers+" --epochs="+epochs+""
    onnx_convert="python3 onnx_export.py --model-dir=models/"+dataset_name+""
    detectnet_start="detectnet --model=models/"+dataset_name+"/ssd-mobilenet.onnx --labels="+dataset_name+"/labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes "+device+""
    os.system(train)
    os.system(onnx_convert)
    if showresult==True:
        os.system(detectnet_start)
####
nvidia_tree(dataset_name='objects1')
"""detectnet --model=models/"+dataset_name+"/ssd-mobilenet.onnx --labels=$NET/labels.txt \
          --input-blob=input_0 --output-cvg=scores --output-bbox=boxes \
            csi://0"""
