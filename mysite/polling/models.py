from django.db import models

STATUS_CHOICES = {
    'd': "Draft",
    'p': "Published",
    'w': "Withdrawn",
}


# Create your models here.

class Poll(models.Model):
    author = models.CharField(default='EMAIL',max_length=100)
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)
    status = models.CharField(default='Draft',max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Poll, through="Membership")



class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    num_polls = models.ForeignKey(Poll, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
