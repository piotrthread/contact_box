# Generated by Django 2.2.1 on 2019-05-28 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='person_id',
        ),
        migrations.AddField(
            model_name='person',
            name='email_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Email'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_contacts.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='person',
            name='adress_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Adress'),
        ),
    ]
