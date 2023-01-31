# Generated by Django 4.1.5 on 2023-01-30 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=30)),
                ('Author_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_Phone', models.BigIntegerField()),
                ('Stud_Semester', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('Stud_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issued_Date', models.DateField()),
                ('Valid_Till', models.DateField()),
                ('Book_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
                ('Student_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Course_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course'),
        ),
    ]
