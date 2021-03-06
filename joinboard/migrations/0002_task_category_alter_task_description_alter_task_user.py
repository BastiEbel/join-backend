# Generated by Django 4.0.4 on 2022-05-12 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joinboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Do_Today', 'DoToday'), ('Progress', 'Progress'), ('Done', 'Done')], default='Todo', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
