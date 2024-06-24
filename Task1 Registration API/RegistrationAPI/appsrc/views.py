from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
# Create your views here.


@csrf_exempt 
def add_record(request):
    record = json.loads(request.body)
    
    role = record.get('apply_for')
    fullname = record.get('fullname')
    email = record.get('email')
    whatsapp = record.get('whatsapp')
    gender = record.get('gender')
    
    institute = record.get('institute')
    field_of_study = record.get('field_of_study')
    years_education = record.get('years_education')
    region = record.get('region')
    
    facebook = record.get('facebook')
    instagram = record.get('instagram')
    linkedin = record.get('linkedin')
    
    experience = record.get("experience")
    
    skills = record.get("skills")
    
    try:
        application = Application.objects.create(
            role = role,
            fullname = fullname,
            email = email,
            whatsapp = whatsapp,
            gender = gender,
            institute = institute,
            field_of_study = field_of_study,
            years_education = float(years_education),
            region = region,
            facebook = facebook,
            instagram = instagram,
            linkedin = linkedin,
            experience = experience,
        )
    except Exception as e:
        return JsonResponse({"Message":"error while adding record"}, status=500)
        
    for skill in skills:
        Skill.objects.create(
            application = application,
            title = skill
        )
    
    
    return JsonResponse({"Message": "Data Added Successfully", "RecordID": application.id}, status=201)
    
    
def get_record(request, id):
    if Application.objects.filter(id = id):
        application = Application.objects.get(id = id)
        return JsonResponse(application.to_json())
    
    return JsonResponse({"Message": f"No record exists with id={id}"})
    

def get_records(request):
    if Application.objects.all().count() > 0:
        records = [record.to_json() for record in Application.objects.all()]
        return JsonResponse({"Records": records})
    
    return JsonResponse({"Message": f"No record exists "})