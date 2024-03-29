# Generated by Django 4.2.7 on 2023-12-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'اطلاعات', 'verbose_name_plural': 'صفحه اصلی'},
        ),
        migrations.RemoveField(
            model_name='home',
            name='image_symbol',
        ),
        migrations.AddField(
            model_name='home',
            name='attributes',
            field=models.TextField(blank=True, null=True, verbose_name='ویژگی ها'),
        ),
        migrations.AddField(
            model_name='home',
            name='image_symbol1',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='تصویر نماد1'),
        ),
        migrations.AddField(
            model_name='home',
            name='image_symbol2',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='تصویر نماد2'),
        ),
        migrations.AddField(
            model_name='home',
            name='image_symbol3',
            field=models.ImageField(blank=True, null=True, upload_to='image', verbose_name='تصویر نماد3'),
        ),
        migrations.AddField(
            model_name='home',
            name='production',
            field=models.TextField(blank=True, null=True, verbose_name='تولید'),
        ),
    ]
