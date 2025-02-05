# Generated by Django 5.1.1 on 2024-09-08 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_review_name_gte_0_alter_review_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='multi_image_product/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageproduct_product', to='product.product')),
            ],
            options={
                'verbose_name': 'ImageProduct',
                'verbose_name_plural': 'ImageProducts',
                'db_table': 'ImageProduct',
            },
        ),
    ]
