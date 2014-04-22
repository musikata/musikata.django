# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0004_userpathnode_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pathnode',
            old_name='node_xpath',
            new_name='xpath',
        ),
    ]
