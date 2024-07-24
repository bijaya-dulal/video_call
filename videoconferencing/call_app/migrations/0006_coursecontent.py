# Generated by Django 4.2.7 on 2024-06-15 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('call_app', '0005_teacher_videochat'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call_app.course')),
            ],
        ),
    ]
