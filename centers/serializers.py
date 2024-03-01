from rest_framework import serializers
from users.serializers import CustomUserSerializer
from .models import Center,CenterAuthor,CenterReview

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'




class CenterReviewSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer(read_only=True)
    center=CenterSerializer(read_only=True)
    user_id=serializers.IntegerField(write_only=True)
    center_id=serializers.IntegerField(write_only=True)
    class Meta:
        model = CenterReview
        fields = ['comment','star_given','user','centers','user_id','center_id']

    def validate(self,data):
        comment=data.get('comment')
        if len(comment)>10:
            raise ValueError(
                {
                    'status':False,
                    'message':"Comment uzunligi oshib ketdi"
                }
            )
        return data