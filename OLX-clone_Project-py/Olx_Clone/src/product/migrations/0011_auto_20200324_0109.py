# Generated by Django 3.0.4 on 2020-03-23 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20200324_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'product image', 'verbose_name_plural': 'product images'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category'),
        ),
    ]
