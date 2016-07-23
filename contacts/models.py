from django.db import models


class Contact(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    def __str__(self):
        return ' '.join([
            self.first_name,
            self.last_name,
        ])


class Student(models.Model):
    fio = models.CharField(max_length=255)
    isp = models.CharField(max_length=100)
    points = models.CharField(max_length=100)
    math_p = models.CharField(max_length=100)
    inf_p = models.CharField(max_length=100)
    rus_p = models.CharField(max_length=100)
    dost_p = models.CharField(max_length=100)
    docs = models.CharField(max_length=100)

    def __repr__(self):
        return 'ФИО: ' + str(self.fio) + " " + str(self.points)

    def __str__(self):
        return  str(self.fio) + " " + str(self.points)

    class Meta:
        ordering = ["-points"]


class StudentOne(models.Model):
    fio = models.CharField(max_length=255)
    isp = models.CharField(max_length=100)
    points = models.CharField(max_length=100)
    math_p = models.CharField(max_length=100)
    inf_p = models.CharField(max_length=100)
    rus_p = models.CharField(max_length=100)
    dost_p = models.CharField(max_length=100)
    docs = models.CharField(max_length=100)

    def __repr__(self):
        return 'ФИО: ' + str(self.fio) + " " + str(self.points)

    def __str__(self):
        return  str(self.fio) + " " + str(self.points)

    class Meta:
        ordering = ["-points"]