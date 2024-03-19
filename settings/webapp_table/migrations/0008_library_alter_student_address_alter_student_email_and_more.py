# Generated by Django 5.0.3 on 2024-03-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp_table', '0007_remove_faculties_id_alter_faculties_teacher_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('book_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100, unique=True)),
                ('book_subject', models.CharField(max_length=100)),
                ('book_class', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=100)),
                ('book_status', models.CharField(max_length=50)),
                ('book_publisher', models.CharField(max_length=100)),
                ('book_issued_to', models.CharField(blank=True, max_length=100, null=True)),
                ('book_count', models.IntegerField(default=0)),
                ('book_year', models.IntegerField()),
            ],
            options={
                'db_table': 'library',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
