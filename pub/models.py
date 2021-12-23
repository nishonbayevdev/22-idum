from django.db import models

# Create your models here.
#####################################
class Employes(models.Model):
    img = models.ImageField(upload_to='media/imgs/')
    fullName = models.TextField(max_length=200,verbose_name="Ism Familiya")
    proffession = models.TextField(max_length=200,verbose_name='Fan turi')
    telegram = models.TextField(max_length=1024)
    instagram = models.TextField(max_length=1024)
    facebook = models.TextField(max_length=1024)
    class Meta:
        verbose_name_plural='Ishchilar'
    def __str__(self):
        return self.fullName

########################################
class ThingCounts(models.Model):
    students = models.CharField(max_length=100000,verbose_name='O\'quvchilar soni')
    teachers = models.CharField(max_length=100000,verbose_name='O\'qituvchilar soni')
    rooms = models.CharField(max_length=100000,verbose_name='Xonalar soni')
    class Meta:
        verbose_name_plural = 'Hisoblari'

#########################################
class News(models.Model):
    imgs = models.ImageField(upload_to='media/newsimg')
    title = models.CharField(max_length=1024,verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Bayonat')
    class Meta:
        verbose_name_plural = 'Yangiliklar'
    def __str__(self):
        return self.title

#########################################
class Message(models.Model):
    email = models.EmailField(max_length=1024,verbose_name='Email')
    name = models.CharField(max_length=1024,verbose_name='Ism Familiya')
    text = models.TextField(verbose_name='Xabar')
    class Meta:
        verbose_name_plural ='Xabarlar'
    def __str__(self):
        return self.email

##########################################
class VideoMessageNews(models.Model):
    descriptio = models.TextField(verbose_name='Izoh')
    shortDescription = models.TextField(verbose_name='Qisqa Izoh')
    video = models.FileField(upload_to='media/video' , verbose_name='media')
    class Meta:
        verbose_name_plural ='Video Yangiliklar'
    def __str__(self):
        return self.shortDescription
class AboutUs(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    def __repr__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Biz haqimizda'