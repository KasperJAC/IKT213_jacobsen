import cv2
import numpy as np


def sobel_edge_detection(image):
    Gblur = cv2.GaussianBlur(image, (3,3), 0) 
    sobelxy = cv2.Sobel(src=Gblur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=1) 
    cv2.imwrite("assignment_3/solutions/III_1_sobel_edge_detection.jpg", sobelxy)

    
def canny_edge_detection(image, threshold_1, threshold_2):
    Gblur = cv2.GaussianBlur(image, (3,3), 0) 
    edges = cv2.Canny(Gblur, threshold_1, threshold_2)
    cv2.imwrite("assignment_3/solutions/III_2_canny_edge_detection.jpg", edges)


def template_match(image, template):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    
    res = cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2) 
    cv2.imwrite("assignment_3/solutions/III_3_template_match.jpg", image)


def resize( image, scale_factor: int, up_or_down: str):
    rows, cols, _channels = map(int, image.shape)
    
    if up_or_down == "up":
        image = cv2.pyrUp(image, dstsize=(scale_factor * cols, scale_factor * rows))
        print (f'** Zoom In: Image x {scale_factor}')    
    elif up_or_down == 'down':
        image = cv2.pyrDown(image, dstsize=(cols // scale_factor, rows // scale_factor))
        print (f'** Zoom Out: Image / {scale_factor}')
    cv2.imwrite("assignment_3/solutions/III_4_resize_down.jpg", image)



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
            shape_image = "assignment_3/shapes-1.png"
            shape_img = cv2.imread(shape_image)
            
            template_image = "assignment_3/shapes_template.jpg"
            template_img = cv2.imread(template_image)
            
            template_match(shape_img, template_img)
        
        elif userInput == "4":
            up_Or_down = "down"
            scale_factor = 2
            
            resize(img, scale_factor, up_Or_down)