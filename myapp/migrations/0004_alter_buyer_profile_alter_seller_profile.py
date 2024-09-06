# Generated by Django 5.0.6 on 2024-08-19 12:37

import django.db.models.deletion
from django.db import migrations, models

def create_missing_profiles(apps, schema_editor):
    Profile = apps.get_model('myapp', 'Profile')
    Buyer = apps.get_model('myapp', 'Buyer')
    Seller = apps.get_model('myapp', 'Seller')

    # Create a profile for each buyer without one
    for buyer in Buyer.objects.filter(profile__isnull=True):
        profile = Profile.objects.create(user=buyer.user, mobile_number='0000000000')
        buyer.profile = profile
        buyer.save()

    # Create a profile for each seller without one
    for seller in Seller.objects.filter(profile__isnull=True):
        profile = Profile.objects.create(user=seller.user, mobile_number='0000000000')
        seller.profile = profile
        seller.save()


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_remove_buyer_contact_number_and_more"),
    ]

    operations = [
        migrations.RunPython(create_missing_profiles),
        migrations.AlterField(
            model_name="buyer",
            name="profile",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.profile"
            ),
        ),
        migrations.AlterField(
            model_name="seller",
            name="profile",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.profile"
            ),
        ),
    ]
