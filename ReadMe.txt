This text file contains the details of the json file and the parameters it contains.
Optional fields can be removed if necessary

############################################################################################################################################################################################
See below for further explanation

1. 'Label' : This is the content displayed in the QR Code
2. 'Inputs' : These are the inputs that can be changed to control the output image
3. 'Outputs' : This is the directory where the images are stored

#############################################################################################################################################################################################
Information of 'Label'

1.1. 'firetype'(optional) : Denote the firetype of the extinguisher. No impact on the program.
1.2. 'weight'(optional) : Denote the weight of the extinguisher. No impact on the program.
1.3. 'volume'(optional) : Denote the volume of the extinguisher. No impact on the program.
1.4. 'snum_prefix'(compulsary) : WILL COMBINE WITH 'SNUM'. Write any repeating characters in serial number. Eg. write 'FireSoda' for serial numbers 'FireSoda10231'
1.5. 'snum'(compulsary) : ONLY NUMBERS, NO SPACES. Write the serial numbers. Accept both single and range. Eg. '1201' or '1200-1302'
1.6. 'contact'(optional) : Denote the contact number written on fire extinguisher. No impact on the program.
1.7. 'company'(optional) : Denote the name of the company on fire extinguisher. No impact on the program.

#############################################################################################################################################################################################
Information of 'Inputs'

2.1. 'img_type'(compulsary) : Denote the image type of the final image. A not supported extension may result in an error. (jpg,png,tiff,bmp,dib,sr)
2.2. 'qr_size'(compulsary) : ONLY NUMBER. Denote the size of QR Code in pixel value.
2.3. 'x_offset'(compulsary) : ONLY NUMBER. Denote the X coordinate of the QR Code w.r.t label. Make sure the QR Code is within the size of the label for stable result.
2.4. 'y_offset'(compulsary) : ONLY NUMBER. Denote the Y coordinate of the QR Code w.r.t label. Make sure the QR Code is within the size of the label for stable result.
2.5. 'sno_x'(compulsary) : ONLY NUMBER. Denote the X coordinate of the text with Serial Number w.r.t label. Make sure the text is within the size of the label for stable result.
2.6. 'sno_y'(compulsary) : ONLY NUMBER. Denote the Y coordinate of the text with Serial Number w.r.t label. Make sure the text is within the size of the label for stable result.
2.7. 'sno_size'(compulsary) : ONLY NUMBER. Denote the size of the text.
2.8. 'label_name'(compulsary) : Denote the name of the base label to paste QR Code on. Mention the extension and path of the image. Eg. 'fireLabel.jpg' or 'sample/images/fireLabel.png'.
2.9. 'sheet_type'(compulsary) : Denotes the type of sheet for output. Supported sheets are A0, A1, A2, A3 and A4.
2.10. 'background'(compulsary) : ONLY 0 AND 1. If 0 then background will BLACK be in color. If 1 then background will be WHITE in color.

#############################################################################################################################################################################################
Information on 'Outputs'

3.1. 'outdir'(compulsary) : The directory where the QR Code and seperate labels are stored. Eg. 'sample/images/'
3.2. 'final_out'(compulsary) : The directory where the final Label Sheet is produced. Eg. 'anyDirectory/final/sheet/'