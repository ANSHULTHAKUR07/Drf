from django.db import models

class EmpolyeData(models.Model):
    firstName = models.CharField(max_length=25, null=False)
    lastName = models.CharField(max_length=25, null=False)
    phoneNumber = models.IntegerField()
    eMail = models.EmailField()
    cpassword = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName

    class Meta:
        verbose_name = 'employedata'
        db_table = 'employedata'

