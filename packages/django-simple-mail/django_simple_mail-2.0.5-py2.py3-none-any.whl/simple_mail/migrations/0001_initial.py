# Generated by Django 2.1 on 2018-08-10 11:02

from django.db import migrations, models
import simple_mail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(editable=False, max_length=20, unique=True, verbose_name='Email Key')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('body', simple_mail.fields.SimpleMailRichTextField(verbose_name='Content')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='simple_mail', verbose_name='Banner')),
                ('button_label', models.CharField(blank=True, max_length=80, verbose_name='Button label')),
                ('button_link', models.CharField(blank=True, max_length=255, verbose_name='Button Link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='SimpleMailConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.URLField(default='http://localhost:8000', max_length=255, verbose_name='Base url')),
                ('from_email', models.EmailField(default='webmaster@localhost', max_length=255, verbose_name='From Email')),
                ('from_name', models.CharField(default='Company Inc', max_length=255, verbose_name='From Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='simple_mail', verbose_name='Logo')),
                ('footer_content', simple_mail.fields.SimpleMailRichTextField(blank=True, verbose_name='Footer')),
                ('facebook_url', models.URLField(blank=True, max_length=255, verbose_name='Facebook Url')),
                ('twitter_url', models.URLField(blank=True, max_length=255, verbose_name='Twitter Url')),
                ('instagram_url', models.URLField(blank=True, max_length=255, verbose_name='Instagram Url')),
                ('website_url', models.URLField(blank=True, max_length=255, verbose_name='Website Url')),
                ('color_header_bg', models.CharField(default='#F7F7F7', max_length=7, verbose_name='Header background')),
                ('color_title', models.CharField(default='#222222', max_length=7, verbose_name='Body title')),
                ('title_size', models.CharField(choices=[('h1', 'h1'), ('h2', 'h2'), ('h3', 'h3')], default='h1', max_length=2, verbose_name='Title size')),
                ('color_body_bg', models.CharField(default='#FFFFFF', max_length=7, verbose_name='Body background')),
                ('color_body', models.CharField(default='#808080', max_length=7, verbose_name='Body content')),
                ('color_body_link', models.CharField(default='#007E9E', max_length=7, verbose_name='Body links')),
                ('color_button', models.CharField(default='#FFFFFF', max_length=7, verbose_name='Button content')),
                ('color_button_bg', models.CharField(default='#00ADD8', max_length=7, verbose_name='Button background')),
                ('border_radius_button', models.PositiveSmallIntegerField(default=3, verbose_name='Button border radius')),
                ('color_footer', models.CharField(default='#FFFFFF', max_length=7, verbose_name='Footer content')),
                ('color_footer_link', models.CharField(default='#FFFFFF', max_length=7, verbose_name='Footer Link')),
                ('color_footer_bg', models.CharField(default='#333333', max_length=7, verbose_name='Footer background')),
                ('color_footer_divider', models.CharField(default='#505050', max_length=7, verbose_name='Footer divider')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configuration',
            },
        ),
    ]
