# Generated by Django 4.0 on 2022-01-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_task_create_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'new_'), ('in_progress', 'in progress_'), ('done', 'done_')], default='new', max_length=15),
        ),
    ]