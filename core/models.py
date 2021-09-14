from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_DEFAULT
from django.db.models.expressions import OrderBy
from django.utils import timezone

class IncomeCategory(models.Model):
    income_category_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(default= timezone.now)
    updated_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now
        super(IncomeCategory,self).save(*args,**kwargs)

    def __str__(self):
        return self.description + str(self.amount)


    class Meta:
        db_table = 'income_category'
        ordering = ['-created_on']

class Income(models.Model):
    user_id = models.IntegerField()
    income_category_id = models.ForeignKey(IncomeCategory,on_delete=CASCADE)
    account_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=11,decimal_places=3)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now
        super(Income,self).save(*args,**kwargs)
    def __str__(self):
        return self.description + str(self.amount)


    class Meta:
        db_table = 'income'

    
