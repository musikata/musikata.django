# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPathNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('path_node', models.ForeignKey(to='path.PathNode', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
