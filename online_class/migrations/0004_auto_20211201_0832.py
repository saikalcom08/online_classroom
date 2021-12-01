# Generated by Django 3.2.9 on 2021-12-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_class', '0003_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='topic_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='topic_image',
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads'),
        ),
    ]
