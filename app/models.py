from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
GENDER_CHOICES = (
                  ('M', 'Male'),
                  ('F', 'Female'),
                  )
TOPIC_CHOICES = (
                ('Science & Technology',),
                ('Politics',),
                ('Local Science & Business',),
                ('Race & Demographics',),
                ('Education',),
                ('Consumer Protection',),
                ('Employment Issues',),
                ('Media Accountability',),
                ('Criminal Justice',),
                ('Wealth & Poverty',),
                ('Cultural Diversity',),
                ('Public Health',),
                ('Environment',),
                ('Infrastructure',),
                ('Public Media',),
                ('Culture',),
                )

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    website =  models.URLField(blank=True)
    email = models.EmailField()
    # interest_areas = models.CharField(max_length=10 , choices = TOPIC_CHOICES)
    about = models.TextField(blank=True, verbose_name='About-Yourself')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Pitch(models.Model):
    heading = models.CharField(max_length=80)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    about_you = models.TextField()
    # topics = models.CharField(max_length=10 , choices = TOPIC_CHOICES)
    requested_amount = models.BigIntegerField()
    proposed_deliverable = models.TextField()
    editorial_deadline = models.DateField()

    def __unicode__(self):
        return self.slug
