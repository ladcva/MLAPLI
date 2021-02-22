# Generated by Django 3.1.6 on 2021-02-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('dependants', models.IntegerField(default=0)),
                ('applicantincome', models.IntegerField(default=0)),
                ('coapplicatincome', models.IntegerField(default=0)),
                ('loanamt', models.IntegerField(default=0)),
                ('loanterm', models.IntegerField(default=0)),
                ('credithistory', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=15)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('graduatededucation', models.CharField(choices=[('Graduate', 'Graduated'), ('Not_Graduate', 'Not_Graduate')], max_length=15)),
                ('selfemployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=15)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')], max_length=15)),
            ],
        ),
    ]
