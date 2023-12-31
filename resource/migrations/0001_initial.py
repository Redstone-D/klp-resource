# Generated by Django 4.2.7 on 2023-12-02 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='PT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt', models.CharField(max_length=16)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='resource.board')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('title', models.CharField(max_length=64)),
                ('postType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classification', to='resource.pt')),
                ('stamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='resource.quality')),
            ],
        ),
    ]
