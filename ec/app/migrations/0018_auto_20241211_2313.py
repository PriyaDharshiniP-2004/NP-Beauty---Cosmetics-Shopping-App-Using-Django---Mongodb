# Generated by Django 3.2 on 2024-12-11 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_auto_20241211_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(default='6759cf2a96287ba0bb7108ec', editable=False, max_length=24, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
