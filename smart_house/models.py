from django.db import models


class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Outlet(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='outlets')
    name = models.CharField(max_length=100)
    power = models.IntegerField()
    electricity_consumption = models.IntegerField() #ват в час

    def __str__(self):
        return self.name
