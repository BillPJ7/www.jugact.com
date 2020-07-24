from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    winner = models.BooleanField(default=0)
    score = models.IntegerField(default=0)
    R1 = models.IntegerField(default=0)
    R2 = models.IntegerField(default=0)
    R3 = models.IntegerField(default=0)
    R4 = models.IntegerField(default=0)
    R5 = models.IntegerField(default=0)
    R6 = models.IntegerField(default=0)
    R7 = models.IntegerField(default=0)
    R8 = models.IntegerField(default=0)
    R9 = models.IntegerField(default=0)
    R10 = models.IntegerField(default=0)
    R11 = models.IntegerField(default=0)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name
    
    def get_model_fields(model):    #might work for getting list of fields
        return model._meta.fields   #maybe use it in view, try getattr(instance, field.name)
                                    #to get value