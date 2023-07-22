from django.db import models
from datetime import datetime
# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    permission = models.CharField(max_length=12)
    # navicat中时间格式会报错
    # addtime = models.DateTimeField(default=datatime.now)
    def __str__(self):
        return self.username
    class Meta:
        db_table = "users_message"

class Station(models.Model):
    # station_id = models.IntegerField()
    station_name = models.CharField(max_length=6)
    station_id = models.IntegerField()
    # id = station_id
    def __str__(self):
        return self.station_name
    class Meta:
        db_table = "station_message"

class UAV_message (models.Model):
    battery = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    # Bat = models.FloatField()
    altitude = models.FloatField()
    # UAViffly = models.SmallIntegerField()
    # ifin = models.SmallIntegerField()
    # staOK = models.SmallIntegerField()
    # conmuOK = models.SmallIntegerField()
    # station_name= models.CharField(max_length=12)
    station_id = models.IntegerField()
    # condition = models.SmallIntegerField()
    time = models.DateTimeField(default=datetime.now)
    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'uav_message'

class mission(models.Model):
    station_id = models.IntegerField()
    Chang = models.IntegerField()
    Wei = models.IntegerField()
    Path = models.IntegerField()
    # time = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'mission'

class info_muchao(models.Model):
    station_id = models.IntegerField()
    wendu = models.FloatField()
    shidu = models.FloatField()
    fengsu = models.FloatField()
    yuliang = models.FloatField()
    state = models.IntegerField()
    # time = models.DateTimeField(default=datetime.now)

    def __int__(self):
        return self.station_id
    class Meta:
        db_table = 'muchao'