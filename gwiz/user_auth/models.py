from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlquote
from django.utils import timezone
from django.db import models


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        now = timezone.now()
        if not email:
            raise ValueError('The given user must have an email address')
        # email = self.normalize_email(email)
        user = self.model(
            email = self.normalize_email(email),
            # email=email,
                          is_staff=is_staff,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True,
                              primary_key=True,
                              )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'),
                                   default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'),
                                    default=True,
                                    help_text=_('Designates whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/{}/".format(urlquote(self.email))

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name
