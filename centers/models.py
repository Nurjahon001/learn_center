import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Center(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(default='center_image/default_center_image.png',upload_to='center_image')
    teaching_format=models.CharField(max_length=50,blank=True,null=True)
    courses=models.CharField(max_length=50,blank=True,null=True)
    contact=models.CharField(max_length=50,blank=True,null=True)
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='centers_table'

class Author(models.Model):
    name=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    email=models.EmailField()
    description=models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table='center_author_table'
class CenterAuthor(models.Model):
    center=models.ForeignKey(Center,on_delete=models.CASCADE)
    author=models.ForeignKey(Author,on_delete=models.SET_DEFAULT,default='delated author')

    def __str__(self):
        return  f'{self.center.name}  {self.author.name}'

    def get_info(self):
        return  f'{self.center.name}  {self.author.name}'

    class Meta:
        db_table='author_table'

class CenterReview(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    center=models.ForeignKey(Center,on_delete=models.CASCADE,related_name='center_review')
    comment=models.TextField()
    star_given=models.PositiveIntegerField(default=0,validators=[MinValueValidator(1),MaxValueValidator(5)])
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        db_table='review_table'

    def __str__(self):
        return self.center.name