# Generated by Django 3.0.3 on 2021-10-28 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_district_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='state_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='District', to='api.State'),
        ),
    ]
