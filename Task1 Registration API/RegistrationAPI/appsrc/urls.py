from django.urls import path
from . import views

urlpatterns = [
    path("add_record/", views.add_record, name="add_record"),
    path("get_record/<str:id>", views.get_record, name="get_record"),
    path("get_all_records/", views.get_records, name="get_records"),
    path("get_csv/", views.add_record, name="get_csv"),
]