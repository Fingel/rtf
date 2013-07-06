from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from geopy import geocoders
from time import sleep

class Protest(models.Model):

    WE_HAVE_IT = 'We have it'
    REQUESTED = 'Requested'
    UNREQUESTED = 'Unrequested'
    REQUEST_STATUSES = (
        (WE_HAVE_IT, 'We have it'),
        (REQUESTED, 'Requested'),
        (UNREQUESTED, 'Unrequested'),
    )

    confirmed = models.BooleanField(default=False,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    date = models.DateField(default=timezone.now,editable=True, null=True,blank=True)
    contact_info_status = models.CharField(max_length=50,
                        choices=REQUEST_STATUSES,
                        default=UNREQUESTED, null=True,blank=True)
    time= models.CharField('Time', max_length=255,null=True,blank=True)
    organizer = models.CharField(max_length=255,null=True,blank=True)
    permit_status = models.CharField(max_length=255,null=True,blank=True)
    reddit_page = models.CharField(max_length=255,null=True,blank=True)
    fb_page = models.CharField(max_length=255,null=True,blank=True)
    twitter = models.CharField(max_length=255,null=True,blank=True)
    other = models.TextField(max_length=2000,null=True,blank=True)
    latitude = models.FloatField(editable=False,default=0.0)
    longitude = models.FloatField(editable=False,default=0.0)
    state_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)
    city_slug = models.CharField(max_length=255, default=None, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.state is not None:
            self.state_slug = slugify(self.state)
        if self.city is not None:
            self.city_slug = slugify(self.city)
        super(Protest, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0}, {1}".format(self.state, self.city)

    def generateLatLong(self):
        if self.latitude == 0.0 or self.longitude == 0.0:
            g = geocoders.GoogleV3()
            if self.city == None:
                place, (lat, lng) = g.geocode("{0}".format(self.state), exactly_one=False)[0]
            else:
                place, (lat, lng) = g.geocode("{0} {1}".format(self.state, self.city), exactly_one=False)[0]
            self.latitude = lat
            self.longitude = lng
            sleep(.5)

    def get_absolute_url(self):
        if self.city is None:
            return "/protests/%s/" % slugify(self.state)
        return "/protests/%s/%s/" % (slugify(self.state), slugify(self.city))

    def to_json(self):
        return {
            'state': self.state,
            'city': self.city or 'N/A',
            'date': self.date.strftime("%Y-%m-%d") if self.date else 'TBA',
            'url': self.get_absolute_url(),
            'latitude': self.latitude,
            'longitude': self.longitude
        }

@receiver(pre_save, sender=Protest)
def pop_latlong(sender, instance, *args, **kwargs):
    instance.generateLatLong()

