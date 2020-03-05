import os
import glob
import numpy as np
import cv2


def define_new_pose_configuration(configName, noAnimals, noBps, Imagepath, BpNameList, animalNumber):
    global ix, iy
    global centerCordStatus

    def draw_circle(event,x,y,flags,param):
        global ix,iy
        global centerCordStatus
        if (event == cv2.EVENT_LBUTTONDBLCLK):
            if centerCordStatus == False:
                cv2.circle(overlay,(x,y-sideImageHeight),10,colors[-i],-1)
                cv2.putText(overlay,str(bpNumber+1), (x+4,y-sideImageHeight), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colors[i], 2)
                cv2.imshow('Define pose', overlay)
                centerCordStatus = True

    im = cv2.imread(Imagepath)
    imHeight, imWidth = im.shape[0], im.shape[1]
    cv2.namedWindow('Define pose', cv2.WINDOW_NORMAL)
    overlay = im.copy()
    for i in range(len(BpNameList)):
        colors = [(255, 0, 255), (0,0,255), (255,204,102), (102,102,255), (152, 255, 255), (153,153,255), (51,153,255), (255, 102, 102), (152,255,102), (0,153,204), ( 204, 153, 0), (153, 204,255), (102, 255, 153), (80, 80, 255), (255, 0, 255), (0,0,255), (255,204,102), (102,102,255), (152, 255, 255), (153,153,255), (51,153,255), (255, 102, 102), (152,255,102), (0,153,204), ( 204, 153, 0), (153, 204,255), (102, 255, 153), (80, 80, 255), (255, 0, 255), (0,0,255), (255,204,102), (102,102,255), (152, 255, 255), (153,153,255), (51,153,255), (255, 102, 102), (152,255,102), (0,153,204), ( 204, 153, 0), (153, 204,255), (102, 255, 153), (80, 80, 255),(255, 0, 255), (0,0,255), (255,204,102), (102,102,255), (152, 255, 255), (153,153,255), (51,153,255), (255, 102, 102), (152,255,102), (0,153,204), ( 204, 153, 0), (153, 204,255), (102, 255, 153), (80, 80, 255)]
        cv2.namedWindow('Define pose', cv2.WINDOW_NORMAL)
        centerCordStatus = False
        bpNumber = i
        sideImage = np.zeros((100, imWidth, 3), np.uint8)
        sideImageHeight, sideImageWidth = sideImage.shape[0], sideImage.shape[1]
        cv2.putText(sideImage, 'Left click ' + BpNameList[i] + '. Press ESC to continue.', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (144, 0, 255), 2)
        ix, iy = -1, -1
        while (1):
            cv2.setMouseCallback('Define pose', draw_circle)
            imageConcat = cv2.vconcat([sideImage, overlay])
            cv2.imshow('Define pose', imageConcat)
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                cv2.destroyWindow('Define pose')
                break

    overlay = cv2.resize(overlay, (250,300))
    imagePath = os.path.join(os.getcwd(), 'pose_configurations', 'schematics')
    namePath = os.path.join(os.getcwd(), 'pose_configurations', 'configuration_names', 'pose_config_names.csv')
    bpPath = os.path.join(os.getcwd(), 'pose_configurations', 'bp_names', 'bp_names.csv')
    noAnimalsPath = os.path.join(os.getcwd(), 'pose_configurations', 'no_animals', 'no_animals.csv')
    imageNos = len(glob.glob(imagePath + '/*.png'))
    newImageName = 'Picture' + str(imageNos+1) + '.png'
    imageOutPath = os.path.join(imagePath, newImageName)
    BpNameList = ','.join(BpNameList)
    print(BpNameList)

    with open(namePath, 'a') as fd:
        fd.write(configName + '\n')
    with open(bpPath, 'a') as fd:
        fd.write(BpNameList + '\n')
    with open(noAnimalsPath, 'a') as fd:
        fd.write(animalNumber + '\n')
    cv2.imwrite(imageOutPath, overlay)














