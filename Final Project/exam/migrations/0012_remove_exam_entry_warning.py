# Generated by Django 3.1.2 on 2021-03-22 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_exam_entry_warning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_entry',
            name='warning',
        ),
    ]
