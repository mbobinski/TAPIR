from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager



#create users methods
class JadeBusemUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


#JadeBusem user profile
class JadeBusemUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(_('user_id'), max_length=200, blank=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    message = models.CharField(_('message'), max_length=300)
    points = models.CharField(_('points'), max_length=200, blank=True, default="0")
    link = models.CharField(_('link'), max_length=500, blank=True)
    is_rules_accepted = models.BooleanField(_('rule accepted'), default=False,
                                   help_text=_('Designates whether the user accept the rules '))
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    is_recruter = models.BooleanField(_('recruter'), default=False,
                                   help_text=_('Designates whether the user can manage recruitment.'))
    is_tactic = models.BooleanField(_('tactic'), default=False,
                                   help_text=_('Designates whether the user can manage compnanion.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = JadeBusemUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)


    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])