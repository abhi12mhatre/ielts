from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)

    class Meta:
        abstract = True


class Record(models.Model):
    status = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(Profile, Record):
    TYPE_CHOICES = (
        (0, 'Admin'),
        (1, 'Teacher'),
        (2, 'Student'),
        (3, 'Staff'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=2)

    def __str__(self):
        return self.username


class Product(Record):
    TYPE_CHOICES = (
        (0, 'Course'),
        (1, 'Test'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    category = models.IntegerField(default=0)
    cost = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class Question(Record):
    test = models.ManyToManyField(Product)
    updated_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=255)
    option = models.JSONField(null=True, blank=True)


class Invoice(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    updated_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL, related_name='invoice_updated_by')


class InvoiceItems(Record):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    cgst = models.FloatField(default=0.0)
    sgst = models.FloatField(default=0.0)
    igst = models.FloatField(default=0.0)


class Result(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    response = models.JSONField()
    date = models.DateField()
    score = models.FloatField()


class Subscription(Record):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    updated_by = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL,
                                   related_name='subscription_updated_by')


class Permission(Record):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50)


class UserPermission(Record):
    permission = models.JSONField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

