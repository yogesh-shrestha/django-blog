from django.db import models
from django.conf import settings
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from . import customs
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.fields import GenericRelation
from tags.models import TaggedItem, Tag
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType 
from . import signal_receivers



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category' , args=(str(self.id))) 




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header_image_url = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,
                                on_delete=models.PROTECT,
                                default=1,
                                related_name='posts')
    tag = models.CharField(max_length=200, blank=True, null=True)
    tags = GenericRelation(TaggedItem, related_query_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')
    approved = models.BooleanField(default=False)

    objects = customs.PostManager()

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/post/%s" %self.slug
        # return reverse('blog:post' , args=str(self.slug))

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-post_date']


post_save.connect(receiver=signal_receivers.create_tags, sender=Post)

class Comment(models.Model):
    post = models.ForeignKey(Post, 
                            on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    content = models.TextField(max_length=1024)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content





class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE, 
                        )
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True,
                                    blank=True,
                                    upload_to="images/profile")
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twiiter_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)
    linkedin_url = models.CharField(max_length=200, null=True, blank=True)
    pinterest_url = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)