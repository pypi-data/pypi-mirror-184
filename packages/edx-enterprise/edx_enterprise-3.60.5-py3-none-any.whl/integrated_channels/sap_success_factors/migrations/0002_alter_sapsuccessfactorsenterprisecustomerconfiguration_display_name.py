# Generated by Django 3.2.12 on 2022-03-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap_success_factors', '0001_squashed_0022_auto_20200206_1046_squashed_0011_alter_sapsuccessfactorslearnerdatatransmissionaudit_enterprise_course_enrollment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='display_name',
            field=models.CharField(blank=True, default='', help_text='A configuration nickname.', max_length=255),
        ),
    ]
