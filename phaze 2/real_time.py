from hashlib import new
import cv2
import numpy 
import time
import torch
# Load Yolo
import pandas
from tkinter import *
from datetime import datetime

#get the weights from our custom data traind model (Yolov5s)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='final_best_.pt', force_reload=False)

# Loading image
starting_time = time.time()
font = cv2.FONT_HERSHEY_COMPLEX_SMALL 
frame_id = 0
tc=0
t=[]
ddd = ''

#game logic
def play(tarneeb,f, s, t, fo):
	www = ''
	C = {2: '2c',3: '3c',4: '4c',5: '5c',6: '6c',7: '7c',8: '8c',9: '9c',10: '10c',11: 'Jc',12: 'Qc',13: 'Kc',14: 'Ac'}
	H = {2: '2h',3: '3h',4: '4h',5: '5h',6: '6h',7: '7h',8: '8h',9: '9h',10: '10h',11: 'Jh',12: 'Qh',13: 'Kh',14: 'Ah'}
	S = {2: '2s',3: '3s',4: '4s',5: '5s',6: '6s',7: '7s',8: '8s',9: '9s',10: '10s',11: 'Js',12: 'Qs',13: 'Ks',14: 'As'}
	D = {2: '2d',3: '3d',4: '4d',5: '5d',6: '6d',7: '7d',8: '8d',9: '9d',10: '10d',11: 'Jd',12: 'Qd',13: 'Kd',14: 'Ad'}

	# tarneeb = input("Enter tarneeb: ")[-1]
	# print(tarneeb)

	# f = input("1st: ")
	# s = input("2st: ")
	# t = input("3st: ")
	# fo = input("4st: ")
	tarneeb = tarneeb[-1]
	f = f
	s = s
	t = t
	fo = fo

	start = time.time()
	#***********************************
	if f[-1] == 'c':
		for key, value in C.items(): 
			if value == f:
				f_key = key
				game_color = f[-1]    
	elif f[-1] == 'h':
		for key, value in H.items(): 
			if value == f:
				f_key = key
				game_color = f[-1]    
				
	elif f[-1] == 's':
		for key, value in S.items(): 
			if value == f:
				f_key = key
				game_color = f[-1]    

				
	elif f[-1] == 'd':
		for key, value in D.items(): 
			if value == f:
				f_key = key
				game_color = f[-1]  
		
	#******************************************
	if s[-1] == 'c':
		for key, value in C.items(): 
			if value == s:
				s_key = key
				
	elif s[-1] == 'h':
		for key, value in H.items(): 
			if value == s:
				s_key = key
				
	elif s[-1] == 's':
		for key, value in S.items(): 
			if value == s:
				s_key = key
				
	elif s[-1] == 'd':
		for key, value in D.items(): 
			if value == s:
				s_key = key
	#******************************************
	if t[-1] == 'c':
		for key, value in C.items(): 
			if value == t:
				t_key = key
				
	elif t[-1] == 'h':
		for key, value in H.items(): 
			if value == t:
				t_key = key
				
	elif t[-1] == 's':
		for key, value in S.items(): 
			if value == t:
				t_key = key
				
	elif t[-1] == 'd':
		for key, value in D.items(): 
			if value == t:
				t_key = key
	#******************************************
	if fo[-1] == 'c':
		for key, value in C.items(): 
			if value == fo:
				fo_key = key
				
	elif fo[-1] == 'h':
		for key, value in H.items(): 
			if value == fo:
				fo_key = key
				
	elif fo[-1] == 's':
		for key, value in S.items(): 
			if value == fo:
				fo_key = key
				
	elif fo[-1] == 'd':
		for key, value in D.items(): 
			if value == fo:
				fo_key = key
	#*****************************************
	if (f[-1] == tarneeb) and (s[-1] != tarneeb) and (t[-1] != tarneeb) and (fo[-1] != tarneeb):
		print("First player is winner :", f)
		www = f
		return www

		
	elif (f[-1] != tarneeb) and (s[-1] == tarneeb) and (t[-1] != tarneeb) and (fo[-1] != tarneeb):
		print("Second player is winner :", s)
		www = s
		return www

		
	elif (f[-1] != tarneeb) and (s[-1] != tarneeb) and (t[-1] == tarneeb) and (fo[-1] != tarneeb):
		print("Third player is winner :", t)
		www = t
		return www
		
	elif (f[-1] != tarneeb) and (s[-1] != tarneeb) and (t[-1] != tarneeb) and (fo[-1] == tarneeb):
		print("Forth player is winner :", fo)
		www = fo
		return www
		
	#*****************************************
	elif (f[-1] == tarneeb) and (s[-1] == tarneeb) and (t[-1] != tarneeb) and (fo[-1] != tarneeb):
		if (f_key > s_key):
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Second player is winner :", s)
			www = s
			return www
			
	elif (f[-1] == tarneeb) and (t[-1] == tarneeb) and (s[-1] != tarneeb) and (fo[-1] != tarneeb):
		if (f_key > t_key):
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Third player is winner :", t)
			www = t
			return www

			
	elif (f[-1] == tarneeb) and (fo[-1] == tarneeb) and (s[-1] != tarneeb) and (t[-1] != tarneeb):
		if (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Forth  player is winner :", fo)
			www = fo
			return www

			
			
	elif (s[-1] == tarneeb) and (t[-1] == tarneeb) and (f[-1] != tarneeb) and (fo[-1] != tarneeb):
		if s_key > t_key: 
			print("Second player is winner :", s)
			www = s
			return www
		else:
			print("Third player is winner :", t)
			www = t
			return www
				
	elif (s[-1] == tarneeb) and (fo[-1] == tarneeb) and (f[-1] != tarneeb) and (t[-1] != tarneeb):
		if (s_key > fo_key):
			print("Second player is winner :", s)
			www = s
			return www
		else:
			print("Forth player is winner :", fo)
			www = fo
			return www
 
			
	elif (t[-1] == tarneeb) and (fo[-1] == tarneeb) and (f[-1] != tarneeb) and (s[-1] != tarneeb):
		if (t_key > fo_key):
			print("Third player is winner :", t)
			www = t
			return www
		else:
			print("Forth player is winner :", fo)
			www = fo
			return www

			
	elif (f[-1] == tarneeb) and (s[-1] == tarneeb) and (t[-1] == tarneeb) and (fo[-1] != tarneeb):
		if (f_key > s_key) and (f_key > t_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (s_key > f_key) and (s_key > t_key):
			print("Second player is winner :", s)
			www = 'Secound player'
			return www
		else:
			print("Third player is winner :", t)
			www = t
			return www
			
	elif (f[-1] == tarneeb) and (s[-1] != tarneeb) and (t[-1] == tarneeb) and (fo[-1] == tarneeb):
		if (f_key > t_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (t_key > f_key) and (t_key > fo_key):
			print("Thirddd  player is winner :", t)
			www = t
			return www
		elif (fo_key > f_key) and (fo_key > t_key):
			print("Forth player is winner :", fo)
			www = fo
			return www

	elif (f[-1] == tarneeb) and (s[-1] == tarneeb) and (t[-1] != tarneeb) and (fo[-1] == tarneeb):
		if (f_key > s_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (s_key > f_key) and (s_key > fo_key):
			print("Second  player is winner :", s)
			www = s
			return www
		elif (fo_key > f_key) and (fo_key > s_key):
			print("Forth player is winner :", fo)
			www = fo
			return www
			

		elif (f[-1] != tarneeb) and (s[-1] == tarneeb) and (t[-1] == tarneeb) and (fo[-1] == tarneeb):
			if (s_key > t_key) and (s_key > fo_key):
				print("Second player is winner :", s)
				www =s
				return www

			elif (t_key > s_key) and (t_key > fo_key):
				print("Third  player is winner :", t)
				www = t
				return www

			elif (fo_key > s_key) and (fo_key > t_key):
				print("Forth player is winner :", fo)
				www = fo
				return www

	elif (f[-1] == tarneeb) and (s[-1] == tarneeb) and (t[-1] == tarneeb) and (fo[-1] == tarneeb):
		if (f_key > s_key) and (f_key > t_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (s_key > f_key) and (s_key > t_key)and (s_key > fo_key):
			print("Second player is winner :", s)
			www = s
			return www
		elif (t_key > f_key) and (t_key > s_key)and (t_key > fo_key):
			print("Third player is winner :", t)
			www = 'Third player'
			return www
		elif (fo_key > f_key) and (fo_key > s_key)and (fo_key > t_key):
			print("Forth player is winner :", fo)
			www = fo
			return www

	#***************************************************
	elif (s[-1] != game_color) and (t[-1] != game_color) and (fo[-1] != game_color):
		print('First Player is winner! :', f)
		www = f
		return www

	elif (s[-1] == game_color)and (t[-1] != game_color)and (fo[-1] != game_color):
		if f_key > s_key:
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Second player is winner :", s)
			www = s
			return www

	elif (t[-1] == game_color)and (s[-1] != game_color)and (fo[-1] != game_color):
		if f_key > t_key:
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Third player is winner :", t)
			www = t
			return www

	elif (fo[-1] == game_color)and (s[-1] != game_color)and (t[-1] != game_color):
		if f_key > fo_key:
			print("First player is winner :", f)
			www = f
			return www
		else:
			print("Forth player is winner :", fo)
			www = fo
			return www

	elif (s[-1] == game_color) and (t[-1] == game_color) and (fo[-1] != game_color):
		if (f_key > s_key) and (f_key > t_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (s_key > f_key) and (s_key > t_key):
			print("Second player is winner :", s)
			www = s
			return www
		else:
			print("Third player is winner :", t)
			www = t
			return www

	elif (s[-1] == game_color) and (fo[-1] == game_color)and (t[-1] != game_color):
		if (f_key > s_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www =f
			return www
		elif (s_key > f_key) and (s_key > fo_key):
			print("Second player is winner :", s)
			www = s
			return www
		else:
			print("Forth player is winner :", fo)
			www = fo
			return www

	elif (t[-1] == game_color) and (fo[-1] == game_color)and (s[-1] != game_color):
		if (f_key > t_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (t_key > f_key) and (t_key > fo_key):
			print("Third player is winner :", t)
			www = t
			return www
		else:
			print("Forth player is winner :", fo)
			www =fo
			return www        


	elif (s[-1] == game_color) and (t[-1] == game_color) and (fo[-1] == game_color):
		if (f_key > s_key) and (f_key > t_key) and (f_key > fo_key):
			print("First player is winner :", f)
			www = f
			return www
		elif (s_key > f_key) and (s_key > t_key) and (s_key > fo_key):
			print("Second player is winner :", s)
			www = s
			return www
		elif (t_key > f_key) and (t_key > s_key) and (t_key > fo_key):
			print("Third player is winner :", t)
			www = t
			return www
		else: 
			print("Forth  player is winner :", fo)
			www = fo
			return www
bids = []
def bid():
	while len(bids)<4:
         x = input("enter your talba : ")
         if x in ["7","8","9","10","11","12","13"]:
             bids.append(int(x))
         elif x=="pass":
             bids.append(x)
         else:
             print ("Input should be an integer from 7 to 13 or 'pass' ")
            
	print("max: ",max(bids))
	print(bids)
bid()        

#gets the tarneeb 		     
b=[]   
card_set=set({})
tarneeb_set = set({})
new_card = []


# video capture 
time_start = 0
w=[]
ii=0
ppp = 1
pppp = 1
tarneeb = ''

while ii <=13 :
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FPS, 10)
	ii+=1
	f=True
	while f:
		gray, frame = cap.read()
		frame_id += 1              
		#Detecting objects
		start_time = datetime.now()

		model.conf=.5
		outs=model(frame)
		outs.render()


		if len (outs.xyxy[0]) !=0 :
	
			if (len(tarneeb_set) < 1):
				tarneeb_set.add(outs.pandas().xyxy[0].name[0])
				print(tarneeb_set)
				ppp += 1
				cv2.waitKey(8000)


			elif (len(card_set) < 4):
				card_set.add(outs.pandas().xyxy[0].name[0])
				ppp+=1


				for i in card_set:
					if i not in new_card:
						new_card.append(i)
				
		else:	
			pass

		tarneeb = list(tarneeb_set)
		if len(tarneeb) == 1:
			tarneeb = tarneeb[-1]
		q=outs.pandas().xyxy[0].value_counts('name').to_dict()
		cc=list(q.keys())
		if len(cc) == 4:
			
			f = cc[0]
			s = cc[1]
			t = cc[2]
			fo = cc[3]
			ddd = play(tarneeb,f, s, t, fo)
			w.append(ddd)
			cc.clear()
			card_set.clear()
			f=False	
			cv2.putText(frame, f"Winner :{ddd}", (20, 150),font, 1, (0, 0, 255), 2, cv2.LINE_4)
			cv2.imshow("Image", frame)
			
			cv2.waitKey(8000)
			cap.release()
			cv2.destroyAllWindows()

			
			


		l=str(ii)
		cv2.putText(frame, f"Round:{l}", (20, 50),font, 1, (0, 0, 255), 2, cv2.LINE_4)
		cv2.imshow("Image", frame)
		cv2.putText(frame, f"tarneeb :{tarneeb}", (20, 250),font, 1, (0, 0, 255), 2, cv2.LINE_4)
		cv2.imshow("Image", frame)
		cv2.putText(frame, f"Inputcard :{cc}", (20, 100),font, 1, (0, 0, 255), 2, cv2.LINE_4)
		cv2.imshow("Image", frame)
		
		
		 
		key = cv2.waitKey(1)
		if key == 1:
			break
	
	print("winner in each round : ",w)
	

cap.release()
cv2.destroyAllWindows()

