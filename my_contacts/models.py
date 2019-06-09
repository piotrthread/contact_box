from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=64)

class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    description = models.TextField()
    group = models.ManyToManyField(Group)


class Adress(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    street_no = models.CharField(max_length=64)
    apartament_no = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=32)
    number_type = models.CharField(max_length=32)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

class Email(models.Model):
    email = models.CharField(max_length=32)
    email_type = models.CharField(max_length=32)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)


