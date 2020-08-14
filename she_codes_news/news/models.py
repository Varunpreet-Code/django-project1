from django.contrib.auth import get_user_model
from django.db import models



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        
    )
    image_url = models.URLField(default ="https://www.britannica.com/story/why-do-cats-sleep-so-much")
    
