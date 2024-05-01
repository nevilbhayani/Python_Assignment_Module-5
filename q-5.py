# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

python manage.py makemigrations
python manage.py migrate


# create_post.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()


from blog.models import Post


def create_post():
    title = "Sample Post"
    content = "This is a sample post content."
    post = Post.objects.create(title=title, content=content)
    print("Post created successfully:", post)

if __name__ == "__main__":
    create_post()



