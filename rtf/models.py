from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from geopy import geocoders

class Protest(models.Model):
	def __str__(self):
		return self.city
		
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
	
	def generateLatLong(self):
		print("Trying {0}, {1}...".format(self.city, self.state))
		if self.latitude == 0.0 or self.longitude == 0.0:
				g = geocoders.GoogleV3()
				if self.city == None:
					place, (lat, lng) = g.geocode("{0}".format(self.state), exactly_one=False)[0]
				else:
					place, (lat, lng) = g.geocode("{0} {1}".format(self.state, self.city), exactly_one=False)[0]
				self.latitude = lat
				self.longitude = lng
				print("Stored for city {0} lat {1} long {2}".format(self.city, self.latitude, self.longitude))
	
@receiver(pre_save, sender=Protest)
def pop_latlong(sender, instance, *args, **kwargs):
	instance.generateLatLong()
	
