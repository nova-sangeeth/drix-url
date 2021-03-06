# Generated by Django 3.0.7 on 2020-09-01 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_user_created_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='short_urls',
            name='created_time',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='short_urls',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
