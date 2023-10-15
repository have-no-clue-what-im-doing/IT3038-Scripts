import os
import ffmpeg

path = "E:\\yikes\\BlackVue\\Record"

videoList = os.listdir(path)

def OrganizeVideo():
    rejects = []
    frontView = []
    rearView = []
    for video in videoList:
        if "PR" in video:
            rejects.append(video)
        elif "PF" in video:
            rejects.append(video)    
        elif "R" in video:
            rearView.append(video)
        elif "F" in video:
            frontView.append(video)
    with open("video_front.txt", "w") as f:
        for file in frontView:
            f.write(f"file '{file}'")
            f.write("\n")
        f.close()
        os.system("move video_front.txt E:\\yikes\\BlackVue\\Record")
    with open("video_rear.txt", "w") as f:
        for file in rearView:
            f.write(f"file '{file}'")
            f.write("\n")
        f.close()    
        os.system("move video_rear.txt E:\\yikes\\BlackVue\\Record")
    os.system("E:")
    os.system("cd E:\\yikes\\BlackVue\\Record")
    
    #ffmpeg.input('video_rear.txt', format='concat', safe=0).output('rear.mkv', c='copy').run()
    ffmpeg.input('video_front.txt', format='concat', safe=0).output('front.mkv', c='copy').run()
            
OrganizeVideo()
    