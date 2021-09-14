# Generated by Django 3.2.7 on 2021-09-14 11:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_category_name', models.CharField(max_length=100)),
                ('income_category_owner', models.IntegerField()),
                ('active_status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'income_category',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=3, max_digits=11)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(null=True)),
                ('income_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.incomecategory')),
            ],
            options={
                'db_table': 'income',
            },
        ),
    ]
