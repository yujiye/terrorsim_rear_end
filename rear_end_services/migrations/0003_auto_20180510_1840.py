# Generated by Django 2.0.4 on 2018-05-10 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rear_end_services', '0002_auto_20180510_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='attack_type_id',
            new_name='attackTypeId',
        ),
        migrations.RenameField(
            model_name='attack',
            old_name='attack_type_name',
            new_name='attackTypeName',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country_id',
            new_name='countryId',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country_name',
            new_name='countryName',
        ),
        migrations.RenameField(
            model_name='keyword',
            old_name='word_id',
            new_name='wordId',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region_id',
            new_name='regionId',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='target_type_id',
            new_name='targetTypeId',
        ),
        migrations.RenameField(
            model_name='target',
            old_name='target_type_name',
            new_name='targetTypeName',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='attack_type',
            new_name='attackType',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='group_name',
            new_name='groupName',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='num_kill',
            new_name='numKill',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='num_wound',
            new_name='numWound',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='prop_comment',
            new_name='propComment',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='prop_value',
            new_name='propValue',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='target_type',
            new_name='targetType',
        ),
        migrations.RenameField(
            model_name='terrorismdata',
            old_name='weapon_type',
            new_name='weaponType',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='weapon_type_id',
            new_name='weaponTypeId',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='weapon_type_name',
            new_name='weaponTypeName',
        ),
        migrations.RemoveField(
            model_name='country',
            name='region_id',
        ),
        migrations.RemoveField(
            model_name='country',
            name='region_name',
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='countryRegion', to='rear_end_services.Region', verbose_name='地区'),
        ),
        migrations.AddField(
            model_name='region',
            name='regionName',
            field=models.CharField(max_length=100, null=True, verbose_name='地区名'),
        ),
    ]
