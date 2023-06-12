from django.db import models


class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):
    # id = models.AutoField(primary_key=False)
    name = models.CharField(max_length=200)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} in {self.house.name}"


class Outlet(models.Model):
    name = models.CharField(max_length=100)
    electricity_consumption = models.IntegerField()
    outlet = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
