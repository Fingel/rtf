from django.db import models
from django.utils import timezone

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
