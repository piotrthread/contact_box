# Generated by Django 2.2.1 on 2019-05-30 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_contacts', '0007_email_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_contacts.Person'),
        ),
    ]