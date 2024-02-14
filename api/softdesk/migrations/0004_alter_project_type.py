# Generated by Django 5.0.1 on 2024-02-13 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0003_remove_project_author_remove_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('ALL', 'ALL'), ('BACK', 'BACK-END'), ('FRONT', 'FRONT-END'), ('IOS', 'IOS'), ('AND', 'ANDROID')], default=('ALL', 'ALL'), max_length=9),
        ),
    ]