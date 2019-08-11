import cv2
import os, sys
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('Original')
cv2.namedWindow('Resized')

yonk = ' .,;"-+oz=aew&@#'

while(1):
	_, frame = cap.read()
	x_size, y_size = os.get_terminal_size(0)
	

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_resized = cv2.resize(gray, (x_size, y_size))
	ascii_img = ''
	for i in range(y_size):
		for j in range(x_size):
			ascii_img += yonk[gray_resized[i, j] // 16]

	cv2.imshow('Original', gray)
	cv2.imshow('Resized', gray_resized)
	print(ascii_img)

	key = cv2.waitKey(1) & 0xFF
	if(key == ord('q')):
		break

cv2.destroyAllWindows()