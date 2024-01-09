import cv2

# Access the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('Mirror Image', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
