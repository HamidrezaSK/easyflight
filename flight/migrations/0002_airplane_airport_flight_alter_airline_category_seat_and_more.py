# Generated by Django 4.1.4 on 2022-12-27 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airplane')),
            ],
            options={
                'ordering': ['-departure'],
            },
        ),
        migrations.AlterField(
            model_name='airline',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classType', models.CharField(choices=[('ECO', 'Economy'), ('BUI', 'Business')], default='ECO', max_length=3)),
                ('status', models.BooleanField(default=False)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=6)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField()),
                ('altitude', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_destination', to='flight.airport')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_source', to='flight.airport')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.route'),
        ),
        migrations.AddField(
            model_name='airplane',
            name='airline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airline'),
        ),
    ]
