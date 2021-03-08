# Generated by Django 3.1.4 on 2021-03-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='admin_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items'),
        ),
    ]