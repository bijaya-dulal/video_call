# Generated by Django 4.2.7 on 2024-06-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('video', models.FileField(upload_to='videos/')),
                ('course_id', models.IntegerField()),
            ],
        ),
    ]
