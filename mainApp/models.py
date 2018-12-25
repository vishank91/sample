from django.db import models
class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    dsg=models.CharField(max_length=20)
    salary=models.IntegerField()

    def __str__(self):
        return "Id = "+str(self.id)+" Name = "+self.name