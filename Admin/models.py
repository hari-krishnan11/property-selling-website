from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

class tbl_adminreg(models.Model):
    adminReg_name=models.CharField(max_length=40)
    adminReg_Email=models.CharField(max_length=40)
    adminReg_password=models.CharField(max_length=40)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey('tbl_district',on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    Category=models.ForeignKey('tbl_category',on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=50)
    category = models.ForeignKey('tbl_category', on_delete=models.CASCADE)
