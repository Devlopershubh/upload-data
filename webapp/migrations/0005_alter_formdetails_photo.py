# Generated by Django 4.2.7 on 2024-02-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_formdetails_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetails',
            name='photo',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]