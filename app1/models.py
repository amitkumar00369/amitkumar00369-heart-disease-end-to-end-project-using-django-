from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class SqlTable(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    def save(self, *args, **kwargs):
        # Hash the password before saving
        user=SqlTable.objects.filter(email=self.email).first()
        if not user:
            
            self.password = make_password(self.password)
        
        super().save(*args, **kwargs)
class SQLToken(models.Model):
    userId=models.IntegerField()
    email=models.EmailField()
    token=models.CharField(max_length=128)
    
class HealthRecord(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()  # Chest pain type
    trestbps = models.IntegerField()  # Resting blood pressure
    chol = models.IntegerField()  # Serum cholesterol
    fbs = models.IntegerField()  # Fasting blood sugar
    restecg = models.IntegerField()  # Resting electrocardiographic results
    thalach = models.IntegerField()  # Maximum heart rate achieved
    exang = models.IntegerField()  # Exercise induced angina
    slope = models.IntegerField()  # Slope of the peak exercise ST segment
    ca = models.IntegerField()  # Number of major vessels colored by fluoroscopy
    thal = models.IntegerField()  # Thalassemia
    new_oldpeak = models.IntegerField()
    result=models.IntegerField(blank=True,null=True)# Depression induced by exercise relative to rest
