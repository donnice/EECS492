import cv2
import numpy as np
import draw
import random
import copy
import sys

imHeight = 102
imWidth = 102
img = cv2.imread('mon_child.jpg')

n = int(sys.argv[1])
k = int(sys.argv[2])
e = int(sys.argv[3])



'''
vout = cv2.VideoWriter()
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
success = vout.open(
   'output_gril.mov', # must end in '.mov' to match codec choice
   fourcc,
   15,
   (imHeight,imWidth),
   True)
assert success
'''

def replace(array):
	[r1,r2,r3,r4,r5,r6] = random.sample(range(1, 102), 6)
	x = [ (r1,r2), (r3,r4), (r5,r6)]
	rm3 = random.randint(0,len(array)-1)
	array[rm3] = x

def shuffle(array):
	rm1 = random.randint(0,len(array)-1)
	rm2 = random.randint(0,len(array)-1)
	if rm1+1 < len(array)-1:
		temp = array[rm1]
		array[rm1] = array[rm1+1]
		array[rm1+1] = temp
	elif rm1-1 > 0:
		temp = array[rm1]
		array[rm1] = array[rm1-1]
		array[rm1-1] = temp

def colorShuffle(array):
	rm4 = random.randint(0,len(array)-1)
	rm7 = random.randint(0,2);
	array[rm4][0] = random.randint(0,255)
	array[rm4][1] = random.randint(0,255)
	array[rm4][2] = random.randint(0,255)
	array[rm4][3] = random.random()

def changeVortex(array):
	rm5 = random.randint(0,len(array)-1)
	rm6 = random.randint(0,2)
	array[rm5][rm6] = [random.randint(0,101),random.randint(0,101)]

i = 0
#img = cv2.imread('mon_child.jpg')
while i<100*n:
	[r1,r2,r3,r4,r5,r6] = random.sample(range(1, 102), 6)
	[p1,p2,p3] = random.sample(range(0,255),3)
	p4 = random.random()
	if i == 0:
		array = [[ (r1,r2), (r3,r4), (r5,r6)]]
		colorArray = [(p1,p2,p3,p4)]
		polys = np.array(array)
		colors = np.array(colorArray)
	else:
		x = [ (r1,r2), (r3,r4), (r5,r6)]
		y = (p1,p2,p3,p4)
		array.append(x)
		colorArray.append(y)
		polys = np.array(array)
		colors = np.array(colorArray)
	polyIm = draw.renderPolyImage(imHeight, imWidth,polys, colors)
	cv2.imshow('image',polyIm)
	cv2.waitKey(1)
	i = i+1

cv2.waitKey(300)
cv2.destroyAllWindows()
#img = cv2.imread('gril.jpg')
originScore = draw.score(img,polyIm)
#print originScore
j = 0
originArray = copy.deepcopy(array)
originColors = copy.deepcopy(colors)
colors = np.array(colorArray)
kid_counter = 0;

while j<=(e - n)*1.0/k:
	while(kid_counter<k):
		rm = random.randint(1,5)
		if rm == 1:
			replace(array)
			polys = np.array(array)
		elif rm == 2:
			shuffle(array)
			polys = np.array(array)
		elif rm == 3 or rm == 4:
			colorShuffle(colors)
		elif rm == 5:
			changeVortex(array)
			polys = np.array(array)
		kid_counter +=1;
	kid_counter = 0
	try:
		polyIm = draw.renderPolyImage(imHeight, imWidth,polys, colors)
	except TypeError:
		print 'TypeError!!!!!'
		print polys
	newScore = draw.score(img,polyIm)

	if newScore < originScore:
		array = copy.deepcopy(originArray)
		colors = copy.deepcopy(originColors)
		#print originScore
	else:
		originArray = copy.deepcopy(array)
		originColors = copy.deepcopy(colors)
		originScore = newScore
	#print originScore
	polys = np.array(array)
	try:
		polyIm = draw.renderPolyImage(imHeight, imWidth,polys, colors)
	except TypeError:
		print 'TypeError!!!!!'
	cv2.imshow('image',polyIm)
	#if j%1000 == 0:
		#vout.write(polyIm)
	cv2.waitKey(1)
	print originScore,j
	j = j+1


cv2.waitKey(100)
#vout.release()
cv2.destroyAllWindows()