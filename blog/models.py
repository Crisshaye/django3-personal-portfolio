from django.db import models

class Post(models.Model):

	title = models.CharField(max_length=100)
	post = models.TextField()
	date = models.DateField(auto_now = True)
	image = models.ImageField(upload_to = 'blog/images/', default = 'blog/images/default.jpg')
#	image = models.ImageField(upload_to = 'portfolio/images/')
#	url = models.URLField(blank = True)
	def __str__(self):
		return self.title

		
