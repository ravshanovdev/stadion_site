# Generated by Django 5.2 on 2025-04-05 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stadion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('size', models.IntegerField(default=0, help_text="Input Stadion's Size(m²)")),
                ('price', models.DecimalField(decimal_places=2, help_text='input price in USA per hour', max_digits=10)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_brone', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Manager_Boy', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
