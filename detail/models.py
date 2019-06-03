from django.db import models

class Detail(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    hashtags = models.ManyToManyField('Hashtag',blank=True)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title

    def __str__(self):
        return self.content[:100]

class Comment(models.Model):
    post = models.ForeignKey(Detail, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.comment_text

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


