# Generated by Django 4.1.2 on 2022-11-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_teacher_detail_teacher_profile_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
