# Generated by Django 5.1.4 on 2024-12-15 11:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irereroapp', '0002_remove_attendancesummary_child_remove_child_guardian_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='child',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('Dob', models.DateField()),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='media/')),
                ('guardian', models.ForeignKey(limit_choices_to={'role': 'Parent'}, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='irereroapp.user')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='irereroapp.class')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_present', models.PositiveIntegerField(default=0, verbose_name='Total Days Present')),
                ('total_absent', models.PositiveIntegerField(default=0, verbose_name='Total Days Absent')),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_summary', to='irereroapp.child')),
            ],
        ),
        migrations.CreateModel(
            name='HealthMetricRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('date_recorded', models.DateField(auto_now_add=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='health_metrics', to='irereroapp.child')),
                ('metric_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='irereroapp.healthmetrictype')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Attendance Date')),
                ('is_present', models.BooleanField(default=True)),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='irereroapp.child')),
            ],
            options={
                'verbose_name': 'Attendance Record',
                'verbose_name_plural': 'Attendance Records',
                'ordering': ['-date'],
                'unique_together': {('child', 'date')},
            },
        ),
    ]
