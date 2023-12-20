from django.db import models 
from resource.models import Board 

# Create your models here.

class Type(models.Model): 
    type = models.CharField(max_length=16) 
    def __str__(self): 
        return f"{self.type}" 

class Seriousness(models.Model): 
    seriousness = models.CharField(max_length=16) 
    def __str__(self): 
        return f"{self.seriousness}" 

class VS(models.Model): 
    name = models.CharField(max_length=16) 
    uid = models.IntegerField(unique=False) 
    occurance = models.TextField() 
    tid = models.IntegerField(blank=True) 
    date = models.DateField(auto_now_add=True) 
    date_expire = models.DateField(blank=True) 
    v_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="occasion_type") 
    v_seriousness = models.ForeignKey(Seriousness, on_delete=models.CASCADE, related_name="occasion_seriousness") 
    v_board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="occasion_board") 
    ip = models.GenericIPAddressField(blank=True, null=True) 
    def __str__(self): 
        return f"{self.name}, UID:{self.uid}\t{self.occurance}, {self.date}\t{self.v_type}, {self.v_seriousness}, {self.v_board}" 
