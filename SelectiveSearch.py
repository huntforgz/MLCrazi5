import cv2 as cv

maxReg = 2000 # max # of bounding box

def regionGenerate(img):
    rects = imgSegment(img)
    res = []
    for i, rect in enumerate(rects):
        x, y, w, h = rect
        if i < max and w > 200 and h > 200:
            bb = img[y:y+h,x:x+w]
            temp = ([x,y,w,h],bb)
            res.append(temp)
        else:
            break
    return res


def imgSegment(img):
    # multithreads of opencv to speed-up
    cv.setUseOptimized(True);
    cv.setNumThreads(4)
    # create Selective Search Segmentation Object using default parameters
    ss = cv.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(img)
    # high recall but slow Selective Search method
    ss.switchToSelectiveSearchQuality()

    # fast but low recall Selective Search method
    #ss.switchToSelectiveSearchFast()


    # run selective search segmentation on input image
    rects = ss.process()
    return rects

# if __name__ == '__main__':
#     filename = '78.jpg'
#     img = cv.imread(filename)
#     print(img.shape)
#     regions = imgSegment(img)
#     i = 0
#     for i, rect in enumerate(regions):
#         if i < maxReg:
#             x,y,w,h = rect
#             bb = img[y:y+h,x:x+w]
#             a = cv.imwrite(('bbs/' + str(i) + '.jpg'),bb)
#             print(a)
