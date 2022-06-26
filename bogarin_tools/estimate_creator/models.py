from site import venv
from django.db import models
from datetime import date, datetime

# Create your models here.
class Estimates(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100, null=False)
    file_date = models.DateField(default=datetime.now, blank=True)



