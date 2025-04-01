import cv2

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    cv2.imshow('Eye controlled Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit when 'q' is pressed
        break

cam.release()
cv2.destroyAllWindows()
