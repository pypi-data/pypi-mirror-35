from django.contrib.auth.models import AbstractUser
from django.db import models
from generic.helpers import get_uuid1


class User(AbstractUser):
    """
    Overrides the default Django User, uuid is changed from an auto incremental
    integer field to a uuidv1 field
    """
    id = models.UUIDField(default=get_uuid1, primary_key=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    validated_email = models.BooleanField(default=False, blank=False, null=False)

    def __unicode__(self):
        return "{0}".format(self.id)

    def __str__(self):
        return "{0}".format(self.id)
