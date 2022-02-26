# Generated by Django 3.2.3 on 2021-06-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(default='', max_length=200)),
                ('com_em', models.EmailField(default='', max_length=200)),
                ('com_cn', models.PositiveIntegerField(default='', max_length=200)),
                ('com_add', models.TextField(default='')),
                ('join_date', models.DateField(auto_now=True, null=True)),
                ('profile', models.ImageField(blank=True, default='', max_length=300, null=True, upload_to='Comp_Profile/')),
                ('com_pass', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
