import numpy as np
import cv2
import os


logoName = input("Enter which logo you want to use:")
logoName = logoName+'.png'

fileNames = os.listdir('Phone-Camera Photos') #Listing out files in the directory which has non watermarked photos

l_fileNames = len(fileNames) #Number of files in the directory which has photos that are not watermarked

numFiles = len(os.listdir('Phone-Camera Photos'))

if numFiles == 0:
    print("NO FILES IN DIRECTORY")
    

else:
    for i in range(0,numFiles):
        print('='*65)
        
        files = os.listdir('Phone-Camera Photos')

        edited_files = os.listdir('Edits with watermark')
        new_fileName = str(len(edited_files)+1)+'.png'
        
        logo = cv2.imread(logoName)
        h_logo, w_logo = logo.shape[:2]

        requiredFile = files[0]

        print('CURRENT FILE : ', requiredFile)
        
        img = cv2.imread('Phone-Camera Photos/'+requiredFile)
        h_img, w_img = img.shape[:2]

        if w_img<h_img:
            scale_percent = (w_img/h_img)/2
        elif w_img>h_img:
            scale_percent = (h_img/w_img)/2

        print('WIDTH OF ORIGINAL IMAGE : ', w_img)
        print('HEIGHT OF ORIGINAL IMAGE : ', h_img)
        print('SCALE PERCENTAGE OF LOGO : ', scale_percent)
        
        w_logo = int(logo.shape[1]*scale_percent)
        h_logo = int(logo.shape[0]*scale_percent)
        dimension = (w_logo,h_logo)

        logo = cv2.resize(logo, dimension, interpolation=cv2.INTER_AREA)

        center_x = int(w_img/2)
        left_x = center_x - int(w_logo/2)
        bottom_y = 2+h_logo
        right_x = left_x+w_logo

        roi = img[2: bottom_y, left_x:right_x]

        result = cv2.addWeighted(roi, 1, logo, 1, 0)

        img[2: bottom_y, left_x:right_x] = result

        cv2.imwrite('Edits with watermark/'+new_fileName, img)

        cv2.waitKey(0)

        print('WATERMARKED FILE : ',new_fileName)
        print('='*65)
        print('\n')
        
        os.remove('Phone-Camera Photos/'+requiredFile)



input('PRESS ANY KEY TO EXIT')



