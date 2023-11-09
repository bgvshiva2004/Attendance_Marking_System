from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login ,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import ClassImage,Attendance_record
from django.conf import settings,os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from typing import List
import logging
import numpy as np
import cv2
from PIL import Image
from mtcnn import MTCNN
import insightface
import math
import pickle
import json
import os
import csv
from django.contrib import messages

BASE_DIR = settings.BASE_DIR

model = insightface.app.FaceAnalysis(name="buffalo_l")
model.prepare(ctx_id=-1)

import face_recognition
import pickle
# Create your views here.

from sklearn.metrics.pairwise import cosine_similarity


def compare(address1,address2):
    img1 = cv2.imread(address1)
    img2 = cv2.imread(address2)
    e1 = model.get(img1)[0]['embedding']
    e1 = e1/np.linalg.norm(e1)
    e2 = model.get(img2)[0]['embedding']
    e2 = e2/np.linalg.norm(e2)
    return cosine_similarity([e1], [e2])[0][0]

def compareEmbedding(e1,e2):
    e1 = e1/np.linalg.norm(e1)
    e2 = e2/np.linalg.norm(e2)
    return cosine_similarity([e1], [e2])[0][0]

@login_required
def index(request):
    if request.method == "POST":
        course = request.POST.get('course')
        date = request.POST.get('date')
        image = request.FILES.get('image')
        
        ClassImage.objects.create(date=date,image=image)

        uploaded_image = request.FILES['image']
        image_path = os.path.join(os.path.join(settings.BASE_DIR,'media'),f"uploads/{uploaded_image}")
        output = set()
        pkl_file_path = "individual_embeddings.pkl"
        with open(pkl_file_path, 'rb') as file:
            base_embeddings = pickle.load(file)

        c=0
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if img is not None:
                faces = model.get(img)

        # print(len(faces))

        final = []

        for face in faces:
            max_score=0.35
            max_roll=0
            for roll in base_embeddings:
                for e1 in base_embeddings[roll]:
                    score = compareEmbedding(e1,face['embedding'])
                    if max_score<score:
                        max_score = score
                        max_roll = roll
            if(max_roll!=0):
                c+=1
                final.append(max_roll)


        final = set(final)
        # print(type(final))

        output=set(output)
        # print(type(output))
        output = output.union(final)
        output = list(output)
        output.sort()

        # print(c)
        # for person in output:
        #     print(person) 
        referenced_data = []
        with open('reference.csv','r') as reference_file:
            reader= csv.reader(reference_file)
            for row in reader:
                referenced_data.append(row)
        
        combined_data = []
        for student in referenced_data:
            ROLL_NO = student[0]
            STUDENT_NAME = student[1]
            if ROLL_NO in output:
                ATTENDANCE = '1'
                DATE = str(date)
            else:
                ATTENDANCE = '0'
                DATE = str(date)
            combined_data.append([ROLL_NO,STUDENT_NAME,DATE,ATTENDANCE])
        try:
            with open(f"{course}_{date}.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerows(combined_data)

            messages.success(request,"Processing Done !")

        except Exception as e:
            messages.error(request,"ERROR !!")
        
        return render(request,'index.html',{'variable':f'Total Students:{c}','students_present':output})
    
    return render(request,'index.html')

def home(request):
    if request.method == "POST":
        return render(request,'home.html')
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth_login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'message':'Invalid Credentials !!'})
    return render(request,'login.html')

@login_required
def review(request):
    if request.method == 'POST':
        year = request.POST.get('year', 'None')
        department = request.POST.get('department', 'None')
        course = request.POST.get('course', 'None')
        date = request.POST.get('date', None)
        
        csv_path = os.path.join(BASE_DIR,f"{course}_{date}.csv")

        response = HttpResponse(open(csv_path,'rb').read(),content_type='')
        response['Content-Disposition']=f'attachment;filename="marked_attendance.csv"'
        return response       
                             
    return render(request,'review.html')

def logout(request):
    auth_logout(request)
    return render(request,'home.html')

@login_required
def register(request):
    return render(request,'register.html')