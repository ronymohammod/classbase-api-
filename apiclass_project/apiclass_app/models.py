from django.db import models




class BlogModel(models.Model):
    TYPES ={

    }



    blog_title=models.TextField(max_length=100,null=True)
    content=models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.blog_title}'
