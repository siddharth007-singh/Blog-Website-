from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class Admin_login(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=200)
    cat_doc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cat_title


class Topic(models.Model):
    top_id = models.AutoField(primary_key=True)
    top_title = models.CharField(max_length=200)
    top_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    top_doc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.top_title


class NewUser(models.Model):
    nu_id = models.AutoField(primary_key=True)
    nu_name = models.CharField(max_length=200)
    nu_city = models.CharField(max_length=200, null=True)
    nu_state = models.CharField(max_length=200, null=True)
    nu_image = models.ImageField(upload_to="media")
    nu_doc = models.DateField()
    nu_address = models.TextField()
    nu_phone = models.CharField(max_length=200)
    nu_email = models.EmailField()
    nu_password = models.CharField(max_length=200)
    nu_myself = models.TextField()

    def __str__(self):
        return self.nu_name


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_name = models.CharField(max_length=200, null=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="media")
    post_description = RichTextField(blank=True, null=True)
    post_doc = models.DateTimeField(default=timezone.now)
    post_user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)
    STATUS = (("0", "Approved"), ("1", "Pending"))
    post_status = models.CharField(max_length=30, choices=STATUS, default="1")

    def __str__(self):
        return self.post_name


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    post_like = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_like = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id  


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_description = models.TextField()
    comment_user = models.ForeignKey(NewUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment_id
from django.db import models

# Create your models here.
