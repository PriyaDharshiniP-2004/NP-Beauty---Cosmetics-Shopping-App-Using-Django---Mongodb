# Generated by Django 3.2 on 2024-12-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(default='67503151ad964d621702c6f8', editable=False, max_length=24, primary_key=True, serialize=False),
        ),
    ]
