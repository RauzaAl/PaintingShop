from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, User, BaseUserManager
from django.db import models
from django_project.utils.constants import USER_ROLES, USER_ROLE_CLIENT


class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=11, blank=True)
    role = models.IntegerField(choices=USER_ROLES, default=USER_ROLE_CLIENT)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        abstract = True

    @property
    def full_name(self):
        return ('%s %s' % (self.first_name, self.last_name)).strip()


    @classmethod
    def save_user(cls, data, password):
        """
        Save user with data and password
        """
        user = cls.objects.create_user(**data)

        user.set_password(password)

        user.save()

        return user


class MyUser(MyAbstractUser):
    pass


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
