# -*- coding: utf-8 -*-
import settings
import os
import sys
import tkinter
import shutil

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient
from tkinter import filedialog

SMILE_BOUND = 0.8
SMILE_RATE_BOUND = 1

KEY = settings.CSK
ENDPOINT = settings.CSE
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

rt = tkinter.Tk()
rt.withdraw()
msg = '写真のフォルダーを選択してください!'
photo_dir_path = filedialog.askdirectory(title=msg)

try:
  if not photo_dir_path:
    print('フォルダーを選んでください!!')
    sys.exit()
    
  msg = '移動先のフォルダーを選択してください!!!'
  output_dir_path = filedialog.askdirectory(title=msg)
  if not output_dir_path:
    print('フォルダーを選んでください!!!!')
    sys.exit()
    
  print('target dir:', photo_dir_path)
  for f in os.listdir(photo_dir_path):
    smile_num = 0
    file_path = os.path.join(photo_dir_path, f)
    img = open(file_path, 'rb')
    
    detected_faces = face_client.face.detect_with_stream(
      img,
      return_face_attributes=['emotion']
    )
    
    img.close()
    
    print('target file:', file_path)
    face_num = len(detected_faces)
    if face_num == 0:
      continue
    
    for face in detected_faces:
      if face.face_attributes.emotion.happiness >= SMILE_BOUND:
        smile_num += 1
        
    smile_rate = smile_num / face_num
    print('smile rate:', smile_rate)
    
    if smile_rate >= SMILE_RATE_BOUND:
      shutil.move(file_path, output_dir_path)
      print('moved!')
        
except Exception as e:
  print('error:', e)
    

print('finished!')