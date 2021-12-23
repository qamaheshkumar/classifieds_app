from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='E:\\Django_React\\adsfrontend\\src\\adsImages\\')
def upload_to(instance, filename):
  return 'E:\\Django_React\\classifieds_app\\ads\\ads\\{filename}'.format(filename=filename)


class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

class Category(models.Model):
  category = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.category


class Status(models.Model):
  status = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.status


class Users(models.Model):
  user_name = models.CharField(max_length=20)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  user_password = models.CharField(max_length=20)
  user_email = models.CharField(max_length=40)
  user_number = models.CharField(max_length=10)
  is_admin = models.IntegerField()
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user_name


class State(models.Model):
  state = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now=True)
      
  def __str__(self):
    return self.state


class District(models.Model):
  district = models.CharField(max_length=200)
  state_id = models.ForeignKey(State, null=True, to_field='id', related_name='District', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key  
  created_at = models.DateTimeField(auto_now=True)

      
  def __str__(self):
    return self.district    


class Classified(models.Model):
  title = models.CharField(max_length=100)
  category_id = models.ForeignKey(Category, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
  # category_id = models.IntegerField()
  status_id = models.ForeignKey(Status, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
  # status_id = models.IntegerField()
  description = models.TextField()
  # images = models.CharField(max_length=250)
  images = models.ImageField(upload_to='post_images', null=True)
  state_id = models.ForeignKey(State, null=True, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
  # state = models.CharField(max_length=30)
  district_id = models.ForeignKey(District, null=True, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
  # district = models.CharField(max_length=30)
  # zip_code = models.IntegerField()
  zip_code = models.CharField(max_length=6, null=True)
  is_hide = models.IntegerField(default=0)
  users_id = models.ForeignKey(Users, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
  # users_id = models.IntegerField()
  phone_number = models.CharField(max_length=10, null=True)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

  def __str__(self):
    return self.title

