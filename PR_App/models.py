from django.db import models
from django.contrib.auth.models import User

class PR_Documents(models.Model):
    nomor_pr = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    acknowledged_date = models.DateField(blank=True, null=True)
    acknowledged_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    director_apprv_date = models.DateField(blank=True, null=True)
    director_apprv_by = models.ForeignKey(User, on_delete=models.CASCADE)
    received_date = models.DateField(blank=True, null=True)
    
class

class PR_Documents_Detail(models.Model):
    line_number = models.IntegerField()
    part_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    usage = models.CharField(max_length=160)
    due = models.DateField(blank=True, null=True)
