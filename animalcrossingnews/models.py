from django.db import models


class Heading(models.Model):
    heading_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.heading_text


class Story(models.Model):
    heading = models.ForeignKey(Heading, on_delete=models.CASCADE)
    story_text = models.CharField(max_length=500)

    def __str__(self):
        return self.story_text
