# Generated by Django 4.2.19 on 2025-02-11 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UoM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('symbol', models.CharField(max_length=4, unique=True)),
                ('unit_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=32)),
                ('pur_own_unit_conversion', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('use_own_unit_conversion', models.DecimalField(decimal_places=4, max_digits=20, null=True)),
                ('purchase_uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_uom', to='PR_App.uom')),
                ('usage_uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='use_uom', to='PR_App.uom')),
            ],
        ),
        migrations.CreateModel(
            name='PR_Documents_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('usage', models.CharField(max_length=160)),
                ('due', models.DateField(blank=True, null=True)),
                ('part_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PR_App.product')),
            ],
        ),
        migrations.CreateModel(
            name='PR_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_pr', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('acknowledged_date', models.DateField(blank=True, null=True)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('director_apprv_date', models.DateField(blank=True, null=True)),
                ('received_date', models.DateField(blank=True, null=True)),
                ('acknowledged_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_acknowledger', to=settings.AUTH_USER_MODEL)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_approver', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('director_apprv_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_director', to=settings.AUTH_USER_MODEL)),
                ('received_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UoM_conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversion_factor', models.DecimalField(decimal_places=4, max_digits=20)),
                ('from_uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr_uom', to='PR_App.uom')),
                ('to_uom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_uom', to='PR_App.uom')),
            ],
            options={
                'unique_together': {('from_uom', 'to_uom')},
            },
        ),
    ]
