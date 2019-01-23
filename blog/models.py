from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(default='文章标题', max_length=50)
	date = models.DateField()
	image = models.ImageField(default='default.png', upload_to='images/')
	text = models.TextField(default='正文')

	def __str__(self):
		return self.title

	def short_text(self):
		j=100
		for i in range(100,0,-1):
			if self.text[i] !=' ':
				continue
			else:
				j=i
				break
		return self.text[:j] +'...'