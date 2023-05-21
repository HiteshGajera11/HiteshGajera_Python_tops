# Generated by Django 4.1.7 on 2023-04-05 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('contact_no', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=20)),
                ('git_url', models.CharField(max_length=100)),
                ('linked_in', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_pic', models.FileField(default='default.png', upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_login', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Jobskeer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(blank=True, null=True)),
                ('current_position', models.CharField(blank=True, max_length=50, null=True)),
                ('experiance', models.CharField(blank=True, max_length=50, null=True)),
                ('qualification', models.CharField(blank=True, max_length=50, null=True)),
                ('last_company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('college_name', models.CharField(blank=True, max_length=50, null=True)),
                ('jobseeker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.jobseeker')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.user'),
        ),
        migrations.CreateModel(
            name='Jobprovider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('linked_in', models.CharField(blank=True, max_length=50, null=True)),
                ('job_specification', models.CharField(max_length=60)),
                ('profile_pic', models.FileField(default='default.png', upload_to='media/images/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Jobpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=80)),
                ('job_description', models.TextField()),
                ('job_type', models.CharField(max_length=50)),
                ('job_category', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('jobprovider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.jobprovider')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobzilla_app.user')),
            ],
        ),
    ]