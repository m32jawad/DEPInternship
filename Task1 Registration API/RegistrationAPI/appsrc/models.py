from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.

class Application(models.Model):
    #Personal
    role = models.CharField(max_length=100, null = False)
    fullname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    whatsapp = models.CharField(max_length=30, null = False)
    gender = models.CharField(max_length=20, null=False, default="Male")
    
    # Education
    institute = models.CharField(max_length=200, null=True)
    field_of_study = models.CharField(max_length=200, null=True)
    years_education = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    region =  models.CharField(max_length=200, null=True)
    
    #Social
    facebook =  models.CharField(max_length=300, null=True)
    instagram =  models.CharField(max_length=300, null=True)
    linkedin =  models.CharField(max_length=300, null=True)
    
    #Experience
    experience = models.CharField(max_length=2000, null=True)
    
    application_datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.fullname} | {self.role}"
    
    def to_json(self):
        model_dict = {
            "role": self.role,
            "fullname": self.fullname,
            "email": self.email,
            "whatsapp": self.whatsapp,
            "gender": self.gender,
            "institute": self.institute,
            "field_of_study": self.field_of_study,
            "years_education": str(self.years_education) if self.years_education is not None else None,
            "region": self.region,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "linkedin": self.linkedin,
            "experience": self.experience,
            "application_datetime": self.application_datetime.isoformat() if self.application_datetime else None,
        }
        
        return json.dumps(model_dict, cls=DjangoJSONEncoder)
        
    
class Skill(models.Model):
    application = models.ForeignKey(Application, related_name='skills', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return f"{self.title} - {self.application.fullname}"
    