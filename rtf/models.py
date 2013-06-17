from django.db import models

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
	confirmed = models.BooleanField(default=False)
	state = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	date = models.DateField()
	contact_info_status = models.CharField(max_length=50,
						choices=REQUEST_STATUSES,
						default=UNREQUESTED)
	time= models.CharField('Time', max_length=100)
	organizer = models.CharField(max_length=100)
	permit_status = models.CharField(max_length=100)
	reddit_page = models.CharField(max_length=255)
	fb_page = models.CharField(max_length=255)
	twitter = models.CharField(max_length=255)
	other = models.TextField(max_length=2000)
