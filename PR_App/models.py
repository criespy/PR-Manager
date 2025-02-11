from django.db import models
from django.contrib.auth.models import User

class PR_Document(models.Model):
    nomor_pr = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    acknowledged_date = models.DateField(blank=True, null=True)
    acknowledged_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_acknowledger')
    approved_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_approver')
    director_apprv_date = models.DateField(blank=True, null=True)
    director_apprv_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_director')
    received_date = models.DateField(blank=True, null=True)
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receiver')
    

class UoM(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symbol = models.CharField(max_length=4, unique=True)
    unit_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Product(models.Model):
    part_number = models.CharField(max_length=20)
    description = models.CharField(max_length=32)
    pur_own_unit_conversion = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    purchase_uom = models.ForeignKey(UoM, on_delete=models.CASCADE, related_name='pur_uom')
    use_own_unit_conversion = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    usage_uom = models.ForeignKey(UoM, on_delete=models.CASCADE, related_name='use_uom')

    def __str__(self):
        return f"{self.part_number} ({self.description})"

    
class UoM_conversion(models.Model):
    from_uom = models.ForeignKey(UoM, on_delete=models.CASCADE, related_name='fr_uom')
    to_uom = models.ForeignKey(UoM, on_delete=models.CASCADE, related_name='to_uom')
    conversion_factor = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        unique_together = ('from_uom', 'to_uom')

    def __str__(self):
        return f"{self.from_uom.symbol} to {self.to_uom.symbol}: {self.conversion_factor}"

class PR_Document_Detail(models.Model):
    pr_document = models.ForeignKey(PR_Document, on_delete=models.CASCADE)
    line_number = models.IntegerField()
    part_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    usage = models.CharField(max_length=160)
    due = models.DateField(blank=True, null=True)
