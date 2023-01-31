# Generated by Django 4.1.5 on 2023-01-30 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_remove_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue_book',
            name='Student_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]