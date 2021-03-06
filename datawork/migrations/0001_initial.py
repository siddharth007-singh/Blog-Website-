# Generated by Django 3.0.8 on 2020-08-24 08:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_title', models.CharField(max_length=200)),
                ('cat_doc', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('nu_id', models.AutoField(primary_key=True, serialize=False)),
                ('nu_name', models.CharField(max_length=200)),
                ('nu_city', models.CharField(max_length=200, null=True)),
                ('nu_state', models.CharField(max_length=200, null=True)),
                ('nu_image', models.ImageField(upload_to='media')),
                ('nu_doc', models.DateField()),
                ('nu_address', models.TextField()),
                ('nu_phone', models.CharField(max_length=200)),
                ('nu_email', models.EmailField(max_length=254)),
                ('nu_password', models.CharField(max_length=200)),
                ('nu_myself', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('top_id', models.AutoField(primary_key=True, serialize=False)),
                ('top_title', models.CharField(max_length=200)),
                ('top_doc', models.DateTimeField(default=django.utils.timezone.now)),
                ('top_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_name', models.CharField(max_length=200, null=True)),
                ('post_image', models.ImageField(upload_to='media')),
                ('post_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post_doc', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_status', models.CharField(choices=[('0', 'Approved'), ('1', 'Pending')], default='1', max_length=30)),
                ('post_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Category')),
                ('post_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Topic')),
                ('post_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.NewUser')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Posts')),
                ('user_like', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.NewUser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_description', models.TextField()),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Posts')),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datawork.NewUser')),
            ],
        ),
    ]
