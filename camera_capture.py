import cv2
def capture():
    '''
    * Logic: <capture and save the arena image>
    '''
    result, frame = cap.read()
    if not result:
        print("Error: Could not read frame.")
    cv2.imwrite("arena.png", frame)


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    capture()
    