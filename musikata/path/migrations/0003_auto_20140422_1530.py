# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0002_userpathnode'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathnode',
            name='node_xpath',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pathnode',
            name='path_id',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
    ]
