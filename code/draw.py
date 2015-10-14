import cv2
import numpy as np

# imHeight - An integer specifying the height of the image
# imWidth - An integer specifying the width of the image
# polys - A numpy array of polygons, where each polygon is an array of tuples representing its vertices
#   Example: polys = np.array([ [ (0,0), (1,2), (3,2)], [(4,4), (17,8), (3,9)] ])
# colors - An array of 4-tuples specifying color and opacity, in the form (B, G, R, alpha)
#   Example: colors = np.array([ (255,0,0,0.5), (0,200,34,0.7) ])

# Returns: a numpy array of size (imHeight, imWidth, 3) that is an image of all the drawn polygons

def renderPolyImage(imHeight, imWidth, polygons, colors):
    polyIm = np.zeros((imHeight, imWidth, 3), np.uint8) ## Create a black background image
    for i in range(len(polygons)):
        tempClone = np.copy(polyIm)
        cv2.fillConvexPoly(tempClone, polygons[i], colors[i])
        alpha = colors[i][3]
        polyIm = cv2.addWeighted(tempClone, alpha, polyIm, 1-alpha, 0)

    return polyIm

def score(im1, im2):
	return -np.log10(cv2.norm(im1,im2)/(cv2.norm(im1)+cv2.norm(im2)))