from django.db import models 

# Create your models here. 

class Quality(models.Model): 
    name = models.CharField(max_length=16) 
    def __str__(self): 
        return self.name 

class Board(models.Model): 
    board = models.CharField(max_length=16) 
    def __str__(self): 
        return self.board 

class PT(models.Model): 
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="section") 
    pt = models.CharField(max_length=16) 
    def __str__(self): 
        return f"{self.pt}" 
    
class Version(models.Model): 
    version = models.CharField(max_length=16) 
    number = models.CharField(max_length=16) 
    def __str__(self): 
        return f"{self.version} {self.number}" 
    
class Originality(models.Model): 
    isOri = models.CharField(max_length=16) 
    def __str__(self): 
        return f"{self.isOri}" 

class Tag(models.Model): 
    Tag = models.CharField(max_length=16)  
    def __str__(self): 
        return f"{self.Tag}" 

class Post(models.Model): 
    tid = models.IntegerField(unique=True) 
    title = models.CharField(max_length=64) 
    postType = models.ForeignKey(PT, on_delete=models.CASCADE, related_name="classification") 
    stamp = models.ForeignKey(Quality, on_delete=models.CASCADE, related_name="level") 
    ver = models.ManyToManyField(Version, related_name="mcver", blank=False) 
    ori = models.ForeignKey(Originality, on_delete=models.CASCADE, related_name="type") 
    tags = models.ManyToManyField(Tag, blank=True, related_name="tag") 
    def __str__(self): 
        return f"{self.tid} {self.title} {self.postType} {self.stamp}" 
