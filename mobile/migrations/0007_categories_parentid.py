# Generated by Django 4.0.1 on 2022-01-23 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0006_alter_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='parentId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mobile.categories'),
            preserve_default=False,
        ),
    ]