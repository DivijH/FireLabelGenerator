########################################### READ THIS ##############################################
## 1. Open ReadMe.txt file for knowing the parameters of json file 								  ##
## 2. QR Code will be generated only in png format.												  ##												  ##
## 3. Read requirements.txt to install necessary packages to run this program					  ##
## 4. All images are in 300 dpi																	  ##
## 5. Make sure that label has a border for easy differentiation of the labels on final sheet 	  ##
####################################################################################################

############################## Generating the QR Codes from json file ##############################

## Converting the json data into key-value pairs
import json
with open('jpegJSON.json') as json_file:
	data = json.load(json_file)

## Extracting the necessary information from the json files
# 1. Exrtacting the serial numbers
snos = data['label']['snum'].split('-')
for i in range(len(snos)):
	snos[i] = int(snos[i])
if len(snos)==2:
	snos = range(snos[0], snos[1]+1)
else:
	snos = range(snos[0], snos[0]+1)

# 2. Extracting the directory where we want to store the QR Codes
output_dir = data['outputs']['outdir']

# 3. Extracting dpi and size of QR Code
dpi = data['inputs']['dpi']

## Making sure that the ouput directory exists.
import os
if not os.path.exists(output_dir):
	os.makedirs(output_dir)

## Generating the qr code images
import segno
# Generating a seperate QR Code for each serial number
for i in snos:
	content = ''
	for key, value in data['label'].items():
		if key == 'snum':
			content += key + " : " + data['label']['snum_prefix'] + str(i) + '\n'
		elif key == 'snum_prefix':
			pass
		else:
			content += key + " : " + value + "\n"
	qr = segno.make(content)
	qr.save(output_dir+str(i)+'.png')


############################## Generating Label with QR Code ##############################

import cv2
import numpy as np

## Opening the label
label_name = data['inputs']['label_name']
x_offset = int(data['inputs']['x_offset'])
y_offset = int(data['inputs']['y_offset'])
size = int(data['inputs']['qrsize'])

## Generating a seperate label for each QR code
for i in snos:
	label = cv2.imread(label_name)
	qr_code = cv2.imread(output_dir+str(i)+'.png')
	# Resizing QR Code to the required size
	scale = (size)/(qr_code.shape[0])
	qr_code = cv2.resize(qr_code,None,fx=scale,fy=scale)
	cv2.imwrite(output_dir+str(i)+'.png', qr_code)
	# Combining the label and QR Code
	label[y_offset:y_offset+qr_code.shape[0] , x_offset:x_offset+qr_code.shape[1]] = qr_code
	cv2.putText(label, "Serial Number : "+data['label']['snum_prefix']+str(i), (int(data['inputs']['sno_x']), int(data['inputs']['sno_y'])), cv2.FONT_HERSHEY_SIMPLEX, float(data['inputs']['sno_size']), 0)
	cv2.imwrite(output_dir+'label'+str(i)+'.png', label)

cv2.imshow('Added Image', label)
cv2.waitKey(0)
cv2.destroyAllWindows()

############################## Generating Labels on given sheet ##############################

sheet = data['inputs']['sheet_type'].upper()

if sheet=='A0':
	width = 9933
	height = 14043
elif sheet=='A1':
	width = 7016
	height = 9933
elif sheet=='A2':
	width = 4961
	height = 7016
elif sheet=='A3':
	width = 3508
	height = 4961
elif sheet=='A4':
	width = 2480
	height = 3508

## Calculating number of labels in the sheet
no_in_row = width//label.shape[1]  # Number of labels in a row
no_in_col = height//label.shape[0] # Number of labels in a column

## Calculating number of sheets required
no_of_sheets = len(snos)//(no_in_col*no_in_row) + 1

## Concatenating images for the sheet
if not os.path.exists(data['outputs']['final_out']):
	os.makedirs(data['outputs']['final_out'])

img_type = data['inputs']['img_type']
if len(snos)==1:
	cv2.imwrite(data['outputs']['final_out']+'finalLabels_1.'+img_type, label)
else:
	def addLabelToCanvas(label, canvas, x, y):
		canvas[y:y+label.shape[0] , x:x+label.shape[1]] = label
		return canvas
	for i in range(no_of_sheets):
		if int(data['inputs']['background']):
			canvas = np.full((height,width,3),255)
		else:
			canvas = np.zeros((height,width,3))
		labels = snos[i*no_in_col*no_in_row : (i+1)*no_in_col*no_in_row]
		x = y = 0
		for label in labels:
			img = cv2.imread(output_dir+'label'+str(label)+'.png')
			canvas = addLabelToCanvas(img, canvas, x, y)
			if x < (no_in_row-1)*img.shape[1]:
				x+=img.shape[1]
			else:
				x=0
				y+=img.shape[0]
		cv2.imwrite(data['outputs']['final_out']+'finalLabels_'+str(i)+'.'+img_type, canvas)