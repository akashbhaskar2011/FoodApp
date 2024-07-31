# Generated by Django 4.2.6 on 2024-07-31 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
        migrations.AddField(
            model_name='item',
            name='user_nam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]