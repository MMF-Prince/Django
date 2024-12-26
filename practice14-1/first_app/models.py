from django.db import models

# Create your models here.

class MyModel(models.Model):
    auto_field=models.AutoField(primary_key=True)
    # big_auto_field=models.BigAutoField(primary_key=True)
    big_integer_field=models.BigIntegerField()
    binary_field=models.BinaryField()
    boolean_field=models.BooleanField()
    # comma_separated_field=models.CharField(
    #     validators=[comma_separated_validator],
    #     max_length=255
    # )
    date_field=models.DateField()
    date_time_field=models.DateTimeField()
    decimal_field=models.DecimalField(max_digits=5, decimal_places=2)
    duration_field=models.DurationField()
    email_field=models.EmailField()
    file_field=models.FileField(upload_to='templates/')
    float_field=models.FloatField()

    # foreign_key=models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    # many_to_many_field=models.ManyToManyField("app.Model", verbose_name=_(""))

    generic_ip_adresses=models.GenericIPAddressField()
    # null_boolean_field=models.NullBooleanField(null=True, blank=True)
    url_field=models.URLField()





