from django.db import models
from django.utils.text import slugify
from django.conf import settings
# Create your models here.


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="certificates_img", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField(default=False)           
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    issued_month_year = models.CharField(max_length=100, blank=True, null=True)
    issued_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            while Certificate.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the certificate instance to the database with the unique slug
        super().save(*args, **kwargs)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    work_location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            while Experience.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the experience instance to the database with the unique slug
        super().save(*args, **kwargs)

class Technology(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to="technology_img", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Technology.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the technology instance to the database with the unique slug
        super().save(*args, **kwargs)

class Education(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            while Education.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the education instance to the database with the unique slug
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects_img", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField(default=False)
    technologies = models.ManyToManyField(Technology, related_name="projects", blank=True) #because a project can have multiple technologies
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            unique_slug = self.slug
            counter = 1
            while Project.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the project instance to the database with the unique slug
        super().save(*args, **kwargs)


class Skill(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            while Skill.objects.filter(slug=unique_slug).exists():
                # If the slug already exists, append a counter to make it unique
                unique_slug = f"{self.slug}-{counter}"
                counter += 1
            self.slug = unique_slug

        # Save the skill instance to the database with the unique slug
        super().save(*args, **kwargs)

