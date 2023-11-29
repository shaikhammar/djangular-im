from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    user_company = models.CharField(_("Company"), max_length=100, default='')
    user_address_1 = models.CharField(_("Address Line 1"), max_length=100, default='')
    user_address_2 = models.CharField(_("Address Line 2"), max_length=100, default='')
    user_city = models.CharField(_("City"), max_length=50, default='')
    user_state = models.CharField(_("State"), max_length=50, default='')
    user_zip = models.CharField(_("Zip"), max_length=50, default='')
    user_country = models.CharField(_("Country"), max_length=50, default='')
    user_phone = models.CharField(_("Phone"), max_length=50, default='')
    user_fax = models.CharField(_("Fax"), max_length=50, default='')
    user_mobile = models.CharField(_("Mobile"), max_length=50, default='')
