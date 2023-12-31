# Generated by Django 4.2.7 on 2023-12-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_delete_originality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Originality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOri', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=16)),
                ('number', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='ori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='resource.originality'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag', to='resource.tags'),
        ),
        migrations.AddField(
            model_name='post',
            name='ver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mcver', to='resource.version'),
        ),
    ]
