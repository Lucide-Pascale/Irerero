# Generated by Django 5.1.4 on 2024-12-12 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irereroapp', '0002_school_user_teacherdetails_parentsdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]