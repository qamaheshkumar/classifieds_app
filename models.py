# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'category'


class Classified(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
    # category_id = models.IntegerField()
    status_id = models.ForeignKey(Status, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
    # status_id = models.IntegerField()
    description = models.TextField()
    images = models.CharField(max_length=250)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    zip_code = models.IntegerField()
    ad_expire_day = models.IntegerField()
    users_id = models.ForeignKey(Users, to_field='id', related_name='Classified', on_delete=models.CASCADE) # Important : custom mapping of primary key to foreign key
    # users_id = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classified'


class Status(models.Model):
    status = models.CharField(max_length=20)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'status'


class Users(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=40)
    user_number = models.CharField(max_length=10)
    is_admin = models.IntegerField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'users'
