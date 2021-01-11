# Generated by Django 3.1 on 2021-01-08 10:09

from django.db import migrations


def initial_remote_app_type(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    remote_app_type_model = apps.get_model("applications", "RemoteAppType")
    remote_app_types = [
        {
            'name': 'chrome',
            'display_name': 'Chrome',
            'description': 'Chrome remote app',
            'author': 'Orange',
            'company': 'FIT2CLOUD',
            'license': 'MIT',
            'tags': [
                'Browser',
                '浏览器',
            ],
            'fs_path': ''
        },
    ]
    k8s_apps = remote_app_type_model.objects.using(db_alias).all()


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_remoteapptype'),
    ]

    operations = [
    ]