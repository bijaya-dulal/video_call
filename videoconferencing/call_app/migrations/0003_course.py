# Generated by Django 4.2.7 on 2024-06-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call_app', '0002_coursecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('teacher_id', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]