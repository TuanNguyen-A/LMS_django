# Generated by Django 4.1.2 on 2022-11-13 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_teacher_detail_alter_chapter_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='qualification',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobile_no',
        ),
    ]
