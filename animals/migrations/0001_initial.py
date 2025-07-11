# Generated by Django 4.2.16 on 2025-06-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.CharField(max_length=255)),
                ('intake_date', models.DateField()),
                ('location', models.CharField(max_length=255)),
                ('intake_condition', models.CharField(max_length=255)),
                ('animal_type', models.CharField(choices=[('PUPPY', 'Puppy'), ('KITTEN', 'Kitten'), ('DOG', 'Dog'), ('CAT', 'Cat')], max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=2)),
                ('spayed', models.BooleanField(default=False, verbose_name='Spayed or Neutered')),
                ('age', models.IntegerField(verbose_name='Age in Days')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('intake_total', models.IntegerField()),
                ('outcome_type', models.CharField(blank=True, max_length=255, null=True)),
                ('outcome_date', models.DateField(blank=True, null=True)),
                ('transferred_to', models.CharField(blank=True, max_length=255, null=True)),
                ('photo_updated', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='straymapper/photos')),
                ('geometry', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
