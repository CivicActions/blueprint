# Generated by Django 2.2.4 on 2019-10-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsystems', '0005_auto_20191021_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_service',
            field=models.ForeignKey(help_text='The AgentService to which this Agent belonts.', on_delete=models.CASCADE, related_name='agents', to='itsystems.AgentService'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='host_instance',
            field=models.ForeignKey(blank=True, help_text='The HostInstance on which the Agent is installed and monitoring.', null=True, on_delete=models.deletion.SET_NULL, related_name='agents', to='itsystems.HostInstance'),
        ),
    ]