# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_big_one', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorvisit',
            name='price',
            field=models.DecimalField(verbose_name='Price', max_digits=9, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='doctorvisit',
            name='procedure',
            field=models.CharField(verbose_name='Procedure', max_length=250),
        ),
        migrations.AlterField(
            model_name='doctorvisit',
            name='visit_date',
            field=models.DateTimeField(verbose_name='Date of Visit'),
        ),
    ]
