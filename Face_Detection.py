import cv2

mouth_cascade = cv2.CascadeClassifier('C:\\Users\\ianwa\\science_fair_real\\haarcascade_frontalface_alt2.xml')


for i in range(1, 42132):
    p_num = str(i)
    image_num = "photos\\scene"
    for x in range(1, 6 - len(p_num)):
        image_num += "0"
    image_num += p_num + ".jpg"
    print(image_num)
    img = cv2.imread(image_num)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))
    for (x,y,w,h) in mouth_rects:

        crop_img = img[y:y + h, x:x + w]
        cv2.waitKey(0)
        cv2.imwrite(image_num, crop_img)
        break
        
