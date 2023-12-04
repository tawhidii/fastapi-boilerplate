from tortoise import fields, models

class Users(models.Model):
    id = fields.BigIntField(pk=True)
    user_name = fields.CharField(max_length=255,unique=True,null=False,index=True)
    email = fields.CharField(max_length=300,unique=True,null=False)
    password = fields.CharField(max_length=350,null=False)
    
    def __str__(self):
        return self.user_name