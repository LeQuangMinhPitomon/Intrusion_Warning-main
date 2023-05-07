import cv2	
import imutils
from playsound import playsound
import threading
import winsound


cap=cv2.VideoCapture('E:/tin/tin hoc tre/2023/MiAI_Intrusion_Warning-main/Cận cảnh trộm đu dây đột nhập nhà dân lấy tài sản ở Củ Chi.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
	

_,stframe=cap.read()
stframe=imutils.resize(stframe, width=500)
stframe=cv2.cvtColor(stframe, cv2.COLOR_BGR2GRAY)
stframe= cv2.GaussianBlur(stframe, (21,21),0)


canhbao=False
chedo=False
dem=0

def beep():
	global canhbao
	for i in range(5):
		if not chedo:
			break
		winsound.Beep(3000,2000)
	canhbao=False		
while True:
	_,frame=cap.read()
	frame=imutils.resize(frame, width=500)
	if chedo:
		frame2=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame2= cv2.GaussianBlur(frame2, (21,21),0)
		difference = cv2.absdiff(frame2, stframe)
		threshold=cv2.threshold(difference,25,255,cv2.THRESH_BINARY)[1]
		stframe=frame2
		if threshold.sum()>1000:
			dem+=1
		else:
			if dem>0:
				dem-=1
		cv2.imshow("camera", threshold)
	else:
		cv2.imshow("camera",frame)		
	if dem>20:
		if not canhbao:
			canhbao=True
			threading.Thread(target=beep).start()
			#playsound('E:/tin/tin hoc tre/2023/MiAI_Intrusion_Warning-main/13.mp3')
	key_pressed=cv2.waitKey(30)
	if key_pressed == ord("t"):
		chedo=not chedo
		dem=0
	if key_pressed==ord("q"):
		chedo=False
		break
cap.release()
cv2.destroyAllWindows()

				



