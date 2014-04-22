# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0003_auto_20140422_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpathnode',
            name='status',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
