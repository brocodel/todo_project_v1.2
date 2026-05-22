from django.db import models
import datetime

# Create your models here.


class Dealer(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.login


class Deals(models.Model):
    text = models.CharField('Text', max_length=50)
    priority = models.IntegerField('Priority')
    date = models.DateField('Date', default=datetime.date.today)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, blank=False, null=True)
    
    @property
    def color(self):
        hue = 120 * (self.priority / 10)
        return f'hsl({int(hue)}, 80%, 50%)'

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'




