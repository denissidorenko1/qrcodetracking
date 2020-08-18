
import cv2

cap = cv2.VideoCapture(0)
width  = int(cap.get(3))
height = int(cap.get(4))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #col = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    fps = int(cap.get(5))
    print(fps)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()