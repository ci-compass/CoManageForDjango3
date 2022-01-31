from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    given_name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    idp = models.CharField(max_length=200)
    idp_name = models.CharField(max_length=200)
    sub = models.CharField(max_length=200)
    aud = models.CharField(max_length=200)
    cert_subject_dn = models.CharField(max_length=200)
    iss = models.CharField(max_length=200)
    oidc = models.CharField(max_length=200)
    eppn = models.CharField(max_length=200)
    eptid = models.CharField(max_length=200)
    acr = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class IsMemberOf(models.Model):
    attribute = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    members = models.ManyToManyField(User, through="MembershipIsMemberOf")

    def __str__(self):
        return self.value


class MembershipIsMemberOf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ismemberof = models.ForeignKey(IsMemberOf, on_delete=models.CASCADE)


class LdapOther(models.Model):
    attribute = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    members = models.ManyToManyField(User, through="MembershipLdapOther")

    def __str__(self):
        return self.value


class MembershipLdapOther(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ldapother = models.ForeignKey(LdapOther, on_delete=models.CASCADE)
