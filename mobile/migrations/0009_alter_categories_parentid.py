# Generated by Django 4.0.1 on 2022-01-23 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0008_alter_categories_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='parentId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobile.categories'),
        ),
    ]
