import cv2 
import numpy as np


def Harris_Corner_Detection(reference_image):
    img = cv2.imread(reference_image)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255] 
           
    cv2.imwrite('assignment_4/solutions/harris.png',img)



def SIFT(image_to_align, reference_image, max_features, good_match_precision):
    MIN_MATCH_COUNT = 10
    img1 = cv2.imread(image_to_align, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(reference_image, cv2.IMREAD_GRAYSCALE)
    
    

    # Initiate SIFT detector
    sift = cv2.SIFT_create()
    
    
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(des1,des2,k=2)
    
    # store all the good matches as per Lowe's ratio test.
    good = [] 
    
    for m,n in matches:
        if m.distance < good_match_precision*n.distance:
            good.append(m)
            
            
            
    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        
        
        h2,w2 = img2.shape
        aligned = cv2.warpPerspective(img1, M, (w2, h2))  
        
        
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    else:
        print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
        matchesMask = None

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)
    
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

    cv2.imwrite('assignment_4/solutions/SIFT_matches.png',img3)
    cv2.imwrite('assignment_4/solutions/SIFT_aligned.png',aligned)
    
    
    
if __name__ == "__main__":
    
    
    while(True):
         
        print("""\n         Meny:
              0     = Quit
              1     = Task 1: Harris Corner Detection
              2     = Task 2: SIFT
              """)
        
        userInput = input(">> ").strip()
        
        if userInput == "0":
            break
        elif userInput == "1":
            reference_image = 'assignment_4/reference_img.png'
            Harris_Corner_Detection(reference_image)
        elif userInput == "2":
            image_to_align = 'assignment_4/align_this.jpg'
            reference_image = 'assignment_4/reference_img.png'
            max_features=10 # Antar at denne er ment å være min_match_count, siden koden ikke fungerer når nfeatures er 10
            good_match_precent=0.7 
            SIFT(image_to_align, reference_image, max_features, good_match_precent)
            
            