from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email
    
def title_image_upload_path(instance, filename):
    return f"posts/{instance.slug}/title_image/{filename}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    title_image = models.ImageField(upload_to=title_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', '-updated_at']
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)



def section_image_upload_path(instance, filename):
    return f"posts/{instance.post.slug}/sections_img/{filename}"

class PostSection(models.Model):
    SECTION_TYPE_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
    )

    post = models.ForeignKey(Post, related_name="sections", on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    section_type = models.CharField(max_length=10, choices=SECTION_TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=section_image_upload_path, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.post.title} - {self.section_type}"
    
    #auto update order field
    def save(self, *args, **kwargs):
        if not self.order:
            last_section = PostSection.objects.filter(post=self.post).order_by('-order').first()
            if last_section:
                self.order = last_section.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)
    
   
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['post', 'user']
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.title} Post"
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']

    def __str__(self):
        return f"{self.user.email} liked {self.post.title} Post"
    
    
