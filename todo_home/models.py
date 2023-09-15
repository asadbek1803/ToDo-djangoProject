from django.db import models

# Create your models here.

class Do(models.Model):
    do = (
        ('bajarilmoqda','Bajarilmoqda'),
        ('kutilmoqda','Kutilmoqda'),
        ('tugatildi','Tugatildi')
    )

    title = models.CharField(max_length=95)
    time = models.DateTimeField()
    docs = models.TextField()
    status = models.CharField(max_length=17, choices=do)


    def __str__(self):
        return self.title