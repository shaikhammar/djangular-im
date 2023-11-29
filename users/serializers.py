from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'user_company', 'user_address_1', 'user_address_2', 
                  'user_city', 'user_state', 'user_zip', 'user_country', 
                  'user_phone', 'user_fax', 'user_mobile']