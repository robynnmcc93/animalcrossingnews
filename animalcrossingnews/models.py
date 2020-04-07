from django.db import models


class Heading(models.Model):
    heading_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.heading_text

class TheStory(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    thestory_text = models.CharField(max_length=500)

    def __str__(self):
        return self.thestory_text
