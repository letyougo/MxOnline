#_*_encoding:utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'城市名字')
    desc = models.CharField(max_length=200,verbose_name=u'')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'机构名字')
    desc = models.TextField(verbose_name=u'机构描述')

    image = models.ImageField(upload_to='org/%Y/%m',default=u"image/default.png",max_length=100)
    address = models.CharField(max_length=150,verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    click_num = models.IntegerField(default=0, verbose_name=u'机构点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'机构收藏数')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教室名字')
    work_years = models.IntegerField(default=0,verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50,verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50,verbose_name=u'公司职位')
    points = models.CharField(max_length=50,verbose_name=u'教学特点')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    click_num = models.IntegerField(default=0, verbose_name=u'教师点击数')
    fav_num = models.IntegerField(default=0, verbose_name=u'教师收藏数')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

