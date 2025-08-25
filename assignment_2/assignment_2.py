import cv2
import numpy as np
from matplotlib import pyplot as plt


def padding(image, border_width):
    reflect = cv2.copyMakeBorder(image,border_width,border_width,border_width,border_width,cv2.BORDER_REFLECT)
    cv2.imwrite("assignment_2/solutions/II_1_reflect.jpg", reflect)
    #plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    #plt.show()


def crop(image, x_0, x_1,  y_0, y_1):
    cropped_image = image[y_0:y_1, x_0:x_1]
    cv2.imwrite("assignment_2/solutions/II_2_crop.jpg", cropped_image)


def resize(image, width, height):
    resize = cv2.resize(image, (width, height))
    cv2.imwrite("assignment_2/solutions/II_3_resize.jpg", resize)


def copy(image, emptyPictureArray):
    emptyPictureArray[:] = image
    cv2.imwrite("assignment_2/solutions/II_4_copy.jpg", emptyPictureArray)
    

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("assignment_2/solutions/II_5_grayscale.jpg", gray)
    
    
def hsv(image):    	
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite("assignment_2/solutions/II_6_hsv.jpg", hsvImage)
    
    
def hue_shifted(image, emptyPictureArray, hue):
    emptyPictureArray[:] = np.clip(image.astype(np.int16) + hue, 0, 255).astype(np.uint8)
    cv2.imwrite("assignment_2/solutions/II_7_hue_shifted.jpg", emptyPictureArray)


def smoothing(image):
    smoothing = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
    cv2.imwrite("assignment_2/solutions/II_8_smoothing.jpg", smoothing)
   
    
def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite("assignment_2/solutions/II_9_rotation_90.jpg", rotated)
    elif rotation_angle == 180:
        rotated = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite("assignment_2/solutions/II_9_rotation_180.jpg", rotated)
    else:
        print("Invalid angle")




if __name__ == "__main__":
    
    
    #Loading image
    image = "assignment_2/lena-1.png"
    img = cv2.imread(image)
    
    
    while(True):
         
        print("""\n         Meny:
              0     = Quit
              1     = Task 1: padding
              2     = Task 2: crop 
              3     = Task 3: resize
              4     = Task 4: copy
              5     = Task 5: grayscale
              6     = Task 6: hsv
              7     = Task 7: color shifting
              8     = Task 8: smoothing
              9     = Task 9: rotation""")
        
        userInput = input(">> ").strip()
        
        if userInput == "0":
            break
        
        elif userInput == "1":
            print("Task 1")
            border = 100
            padding(img, border)
        
        elif userInput == "2":
            print("Task 2")
            x_0 = 80
            y_0 = 80
            x_1 = 512-130 #We know the image is 512 from assignment 1
            y_1 = 512-130
            crop(img, x_0, x_1, y_0, y_1)
            
        elif userInput == "3":
            print("Task 3")
            width_task3 = 200
            height_task3 = 200
            resize(img, width_task3, height_task3)
            
        elif userInput == "4":
            print("Task 4")
            
            #Using the same code from assignment 1:
            dimensions = img.shape
    
            height = dimensions[0]
            width = dimensions[1]
            channels = dimensions[2]
            size = img.size
            dataType = img.dtype
            
            emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
            
            copy(img, emptyPictureArray)
        
        elif userInput == "5":
            print("Task 5")
            grayscale(img)
        
        elif userInput == "6":
            print("Task 6")
            hsv(img)
            
        elif userInput == "7":
            print("Task 7")
            hue = 50
            
            #Using the same code from assignment 1:
            dimensions = img.shape
    
            height = dimensions[0]
            width = dimensions[1]
            channels = dimensions[2]
            emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
            
            hue_shifted(img, emptyPictureArray, hue)
        
        elif userInput == "8":
            print("Task 8")
            smoothing(img)
        
        elif userInput == "9":
            print("Task 9")
            print("""Part meny:
                  1     : 90
                  2     : 180
            """)
            iput9 = input("9 >>")
            
            if iput9 == "1":
                rotation(img, 90)
            elif iput9 == "2":
                rotation(img, 180)