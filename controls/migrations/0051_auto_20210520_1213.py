# Generated by Django 3.1.8 on 2021-05-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0050_auto_20210518_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='component_state',
            field=models.CharField(blank=True, choices=[('UNDER_DEVELOPMENT', 'under-development'), ('OPERATIONAL', 'operational'), ('DISPOSITION', 'disposition'), ('OTHER', 'other')], default='operational', help_text='OSCAL Component State.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='component_type',
            field=models.CharField(blank=True, choices=[('HARDWARE', 'hardware'), ('SOFTWARE', 'software'), ('SERVICE', 'service'), ('POLICY', 'policy'), ('PROCESS', 'process'), ('PROCEDURE', 'procedure')], default='software', help_text='OSCAL Component Type.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.TextField(default='Description needed', help_text='Description of the Element'),
        ),
    ]
