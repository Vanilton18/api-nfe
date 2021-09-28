# Generated by Django 3.1.7 on 2021-04-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(db_column='id_pais', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='tx_nome', max_length=104)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_cadastro')),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_ultima_alteracao')),
            ],
            options={
                'db_table': 'pais',
                'managed': True,
            },
        ),
    ]