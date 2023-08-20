# Generated by Django 4.2.4 on 2023-08-18 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80, verbose_name='Category Name')),
                ('category_desc', models.CharField(max_length=150, verbose_name='Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_first_name', models.CharField(max_length=80, verbose_name='Client Name')),
                ('client_last_name', models.CharField(max_length=80, verbose_name='Client Last Name')),
                ('client_document_identity', models.CharField(max_length=15, verbose_name='Document of Identity')),
                ('client_birth_date', models.DateField()),
                ('client_address', models.TextField(null=True)),
                ('client_status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'Client',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(max_length=80, verbose_name='Gender Name')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'db_table': 'Gender',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=80, verbose_name='Product Name')),
                ('product_image', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('producto_pvp', models.TextField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'Product',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_sub_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sale_tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sale_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sale_created_add', models.DateTimeField()),
                ('sale_client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.client')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
                'db_table': 'Sale',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SaleByProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_by_product_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('sale_by_product_quantity', models.PositiveIntegerField(default=0)),
                ('sale_by_product_subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.sale')),
            ],
            options={
                'verbose_name': 'SaleByProduct',
                'verbose_name_plural': 'SalesByProducts',
                'db_table': 'SaleByProduct',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_product',
            field=models.ManyToManyField(blank=True, through='erp.SaleByProduct', to='erp.product'),
        ),
        migrations.AddField(
            model_name='client',
            name='client_gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='erp.gender'),
        ),
    ]
