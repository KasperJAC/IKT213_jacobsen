import cv2
import numpy as np


def sobel_edge_detection(image):
    Gblur = cv2.GaussianBlur(image, (3,3), 0) 
    sobelxy = cv2.Sobel(src=Gblur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1) 
    cv2.imwrite("assignment_3/solutions/III_1_sobel_edge_detection.jpg", sobelxy)

    
def canny_edge_detection(image, threshold_1, threshold_2):
    Gblur = cv2.GaussianBlur(image, (3,3), 0) 
    edges = cv2.Canny(img, threshold_1, threshold_2)
    cv2.imwrite("assignment_3/solutions/III_2_canny_edge_detection.jpg", edges)


def template_match(image, template):
    res = cv2.matchTemplate(img,template,method)
    pass



if __name__ == "__main__":

    image = "assignment_3/lambo.png"
    img = cv2.imread(image)
    
    
    while(True):
         
        print("""\n         Meny:
              0     = Quit
              1     = Task 1: Sobel edge detection
              2     = Task 2: Canny edge detection
              3     = Task 3: Template match
              4     = Task 4: Resizing
              """)
        
        userInput = input(">> ").strip()
        
        if userInput == "0":
            break
        
        elif userInput == "1":
            sobel_edge_detection(img)
            
        elif userInput == "2":
            t1 = 50
            t2 = 50
            canny_edge_detection(img, t1, t2)
        
        elif userInput == "3":
            pass
        
        elif userInput == "4":
            pass