from ast import Pass
import pyfirmata
import time
import numpy as np
import cv2
import os
import face_recognition
import pathlib
import glob
images_folder = glob.glob("images/*.jpg")
vehicles_folder_count = []

# from pathlib import Path
# fold_dir=  r'C:\Users\Mayuree Deori\Downloads\source code\source code\images'
# images= Path(fold_dir).glob('*.png')
  
# IMAGE_FILES = []
# dir_path = r'C:\Users\Mayuree Deori\Downloads\source code\source code\images'     
# for image in os.listdir(dir_path):
#     img_path =os.path.join(dir_path, image)
#     img_path = face_recognition.load_image_file(img_path)  # reading image and append to list
#     IMAGE_FILES.append(img_path)
    
         
   
# indices=np.array([])
# Image_files=np.array(IMAGE_FILES)[ indices.astype(int)] 
#Image_files=np.array(IMAGE_FILES)   

# dir_path = r'C:\Users\Mayuree Deori\Downloads\source code\source code\images'
# Load images from a folder
# 
# path=r'C:\Users\Mayuree Deori\Downloads\source code\source code\images'
# images=os.listdir(path)
# img_data=[]
# for image in images:
#      img_arr=cv2.imread(path + '/' + image)
#      img_data.append(img_arr)

comport='COM5'
board = pyfirmata.Arduino(comport)
#if we draw the arduino board we need to write_pin number input (high or low)
#lane1
red_1=board.get_pin('d:13:o')
yellow_1=board.get_pin('d:12:o')
green_1=board.get_pin('d:11:o')
#lane 2
red_2=board.get_pin('d:10:o')
green_2=board.get_pin('d:9:o')
yellow_2=board.get_pin('d:8:o')
#lane 3
# red_3=board.get_pin('d:13:o')
# green_3=board.get_pin('d:12:o')
# yellow_3=board.get_pin('d:11:o')
# #lane 4
# red_4=board.get_pin('d:13:o')
# green_4=board.get_pin('d:12:o')
# yellow_4=board.get_pin('d:11:o')
#for img in IMAGE_FILES:

# 



def led(vehicle_count, ind) -> int:
  

   
     if(ind %2==0):
       if(vehicle_count==4):
              green_1.write(1)
              time.sleep(5)
       elif(vehicle_count==5):
              green_1.write(1)
              time.sleep(6)
       elif(vehicle_count==8):
              green_1.write(1)
              time.sleep(4)
       green_1.write(0)       
       yellow_1.write(1), yellow_2.write(2)
       time.sleep(5)
       yellow_1.write(0),yellow_2.write(0)
       time.sleep(5)
      
     elif((ind-1)%2==0):
       if(vehicle_count==4):
              green_2.write(1)
              time.sleep(10)
       elif(vehicle_count==5):
              green_2.write(1)
              time.sleep(2)
       elif(vehicle_count==8):
              green_2.write(1)
              time.sleep(5)

       green_2.write(0)       
       yellow_1.write(1)
       yellow_2.write(1)
       time.sleep(5)
       yellow_1.write(0)
       yellow_1.write(0)
       red_1.write(1)
       time.sleep(5)
       return 1
#     elif((i-1)%4==0):
#        red_1.write(1)    
    #green_1.write(0)
    # red_2.write(0)
    # red_3.write(0)
    # red_4.write(0)
    #time.sleep(2)

#lane 4       
    #red_1.write(1)
    # red_2.write(1)
    # red_3.write(1)
    # green_4.write(1) 
    # if vehicle_count==4:
    #    time.sleep(10)
    # elif vehicle_count==6:
    #    time.sleep(20)
    # elif vehicle_count==8:
    #    time.sleep(25)
    # yellow_4.write(1)
    #yellow_1.write(1)
    # green_4.write(1)
    # red_2.write(1)
    #red_1.write(1)
    # red_3.write(1)
    #time.sleep(5)
     