import numpy as np
import cv2

prototxt = "models/MobileNetSSD_deploy.prototxt"
caffe_model = "models/MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(prototxt, caffe_model)

classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    
    width = frame.shape[1] 
    height = frame.shape[0]
    blob = cv2.dnn.blobFromImage(frame, scalefactor = 1/127.5, size = (300, 300), mean = (127.5, 127.5, 127.5), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()
        # detections array is in the format 1,1,N,7, where N is the #detected bounding boxes
    # for each detection, the description (7) contains : [image_id, label, conf, x_min, y_min, x_max, y_max]
    for i in range(detections.shape[2]):
        # confidence of prediction
        confidence = detections[0, 0, i, 2]
        # set confidence level threshold to filter weak predictions
        if confidence > 0.5:
            # get class id
            class_id = int(detections[0, 0, i, 1])
            # scale to the frame
            x_top_left = int(detections[0, 0, i, 3] * width) 
            y_top_left = int(detections[0, 0, i, 4] * height)
            x_bottom_right   = int(detections[0, 0, i, 5] * width)
            y_bottom_right   = int(detections[0, 0, i, 6] * height)
            
            # draw bounding box around the detected object
            cv2.rectangle(frame, (x_top_left, y_top_left), (x_bottom_right, y_bottom_right),
                          (0, 255, 0))
            
            if class_id in classNames:
                # get class label
                label = classNames[class_id] + ": " + str(confidence)
                # get width and text of the label string
                (w, h),t = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                y_top_left = max(y_top_left, h)
                # draw bounding box around the text
                cv2.rectangle(frame, (x_top_left, y_top_left - h), 
                                   (x_top_left + w, y_top_left + t), (0, 0, 0), cv2.FILLED)
                cv2.putText(frame, label, (x_top_left, y_top_left),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
                
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) >= 0:  # Break with ESC 
        break

cap.release()
cv2.destroyAllWindows()