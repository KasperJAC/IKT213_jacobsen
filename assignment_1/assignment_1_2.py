import cv2


def findeCamInfo():
    try:
        cam = cv2.VideoCapture(0)
        print(f"Funnet kamera {cam}")

    except Exception as e:
        print("Error under oppkobling av kamera")


    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cam.get(cv2.CAP_PROP_FPS)


    try: 
        with open('assignment_1/solutions/camera_outputs.txt', 'w') as f:
            f.write(f"fps: {fps}\n")
            f.write(f"height: {frame_height}\n")
            f.write(f"width: {frame_width}\n")
            
            print("Skrevet data til fil")
            
    except Exception as e:
        print(f"Error under skriving til fil. Typ: {e}")



    cam.release()

    print("Alt ok")
    
  
  
  
if __name__ == "__main__":
    findeCamInfo()