import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert to HSV for skin/hand detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Skin color range (this may need tuning!)
    lower = np.array([0, 30, 60], dtype="uint8")
    upper = np.array([20, 150, 255], dtype="uint8")
    
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    
    # Find contours (possible hand shapes)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Largest contour = hand
        c = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(c)
        cv2.drawContours(frame, [hull], -1, (0,255,0), 2)
    
    cv2.imshow("Hand Gesture", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
