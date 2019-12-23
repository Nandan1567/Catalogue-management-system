# Generated by Django 3.0.1 on 2019-12-23 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='When brand was created')),
                ('last_modified', models.DateField(auto_now=True, help_text='When brand was last modified')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the field should be unique', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='When category was created')),
                ('last_modified', models.DateField(auto_now=True, help_text='When category was last modified')),
                ('parent_category', models.ForeignKey(help_text='This can be null', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the product which is unique', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='When product was created')),
                ('last_modified', models.DateField(auto_now=True, help_text='When product was last modified')),
                ('brand', models.ForeignKey(help_text='The brand the product belongs to', on_delete=django.db.models.deletion.CASCADE, to='cms_app.Brand')),
                ('category', models.ForeignKey(help_text='The category the product belongs to', on_delete=django.db.models.deletion.CASCADE, to='cms_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='The key for the specifications. eg. Length', max_length=250)),
                ('value', models.CharField(help_text='The value for the specifications. eg. 50', max_length=250)),
                ('unit', models.CharField(blank=True, help_text='The units for the specifications. eg. cm', max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='When specification was created')),
                ('last_modified', models.DateField(auto_now=True, help_text='When specification was last modified')),
                ('product', models.ForeignKey(help_text='The product the specification belongs to', on_delete=django.db.models.deletion.CASCADE, to='cms_app.Product')),
            ],
        ),
    ]