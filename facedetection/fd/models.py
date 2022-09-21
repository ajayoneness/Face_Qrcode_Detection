from django.db import models


class faceAtt(models.Model):
    name = models.TextField(max_length=50)
    datetime=models.DateTimeField(auto_now_add=True)


class registation(models.Model):
    st_name = models.TextField(max_length=50)
    st_enrollment = models.TextField(max_length=20)
    st_img = models.ImageField(blank=True, upload_to='')


