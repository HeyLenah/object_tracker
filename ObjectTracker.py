import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create() # initialize CSRT tracker
bbox = None 

while True:
    ret, frame = cap.read() 
    if not ret:
        break

    if bbox is not None:
        success, box = tracker.update(frame)
        if success: # draw bounding box if tracking is successful 
            x, y, w, h = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Object Tracking", frame) 
    key= cv2.waitKey(1) & 0xFF

    if key == ord("s"): # clicking s will allow drawing the bounding box
        bbox = cv2.selectROI("Object Tracking", frame, fromCenter=False, showCrosshair=True)
        tracker.init(frame,bbox)

    if key== ord("q"):# clicking q will break from the loop 
        break
           
cap.release()
cv2.destroyAllWindows()