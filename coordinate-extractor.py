import cv2

'''
Get coordinate on image after mouse callback
'''
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Coordinates: ({}, {})".format(x, y))

# Read image file
filename = "uss-map.jpg"
img = cv2.imread(filename)

# Define width and height of the image
height, width = img.shape[:2]

# Define the new dimensions
new_width = 1600
new_height = int(new_width * height / width)

# Resize the image while maintaining aspect ratio
resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Image", resized_img)
cv2.setMouseCallback("Resized Image", get_coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()
