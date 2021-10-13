from django.db import models

# Create your models here.
class Snp500(models.Model):
    
    date = models.DateField("Date", max_length=10, null=False, unique=True)
    open = models.FloatField("Open", null=True)
    high = models.FloatField("High", null=True)
    low = models.FloatField("Low", null=True)
    close = models.FloatField("Close", null=True)
    adj_close = models.FloatField("Adj_close", null=True)
    volume = models.FloatField("Volume", null=True)




