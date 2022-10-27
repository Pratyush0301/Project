import os 
import cv2 
from uuid import uuid1

save_path = os.path.join('Data', 'Images')
os.makedirs(save_path, exist_ok=True)


feed_path = os.path.join('Data', 'Videos')
vid_name = os.listdir(feed_path)[0]

cap = cv2.VideoCapture(os.path.join(feed_path, vid_name))
counter = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (640,640))
        imgname = str(uuid1())
        imgname = f'{imgname}.png'
        imgpath = os.path.join(save_path, imgname)
        cv2.imwrite(imgpath, frame)
        counter += 1
        if counter % 100 == 0:
            print(f'Processed {counter} frames')

cap.release()