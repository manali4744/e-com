
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import EmailValidator, RegexValidator

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,phone, email, name, password=None, password2=None):
    # def create_user(self, phone, password=None):

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            name=name

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, name, password=None):
    # def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_valid = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
   
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, unique=True, blank=True, null=True) 
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[EmailValidator]
    )
    name = models.CharField(max_length=250, validators=[RegexValidator(regex='^[A-Za-z]{2,25}$', message="invalid name")])
    otp = models.CharField(max_length=6,blank=True, null=True)
    coupon = models.CharField(null=True, blank=True,max_length=15)
    gender_choice = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    gender = models.CharField(null=True,blank=True,choices=gender_choice,max_length=7)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    def get_all_permissions(self, user=None):
        if self.is_admin:
            return set()

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class Customer(models.Model):
    Customer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Customer.email