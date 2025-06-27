# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    company name = models.CharField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Employee(models.Model):

    #__Employee_FIELDS__
    full name = models.CharField(max_length=255, null=True, blank=True)
    id = models.DateTimeField(blank=True, null=True, default=timezone.now)
    companyid = models.ForeignKey(company, on_delete=models.CASCADE)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Task(models.Model):

    #__Task_FIELDS__
    taskname = models.CharField(max_length=255, null=True, blank=True)
    taskid = models.IntegerField(null=True, blank=True)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")


class Workprogess(models.Model):

    #__Workprogess_FIELDS__
    wordid = models.IntegerField(null=True, blank=True)
    task = models.ForeignKey(task, on_delete=models.CASCADE)
    progess = models.IntegerField(null=True, blank=True)

    #__Workprogess_FIELDS__END

    class Meta:
        verbose_name        = _("Workprogess")
        verbose_name_plural = _("Workprogess")



#__MODELS__END
