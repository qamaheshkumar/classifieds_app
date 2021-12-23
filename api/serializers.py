from rest_framework import serializers
from .models import Task,Classified,Category,Status,Users,State,District

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

# class AdsSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Ads
# 		fields ='__all__'		

class ClassifiedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classified
		fields ='__all__'

class ClassifiedViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classified
		fields ='__all__'
		depth = 2

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields ='__all__'

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields ='__all__'	

class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields ='__all__'	

class DistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields ='__all__'		

class DistrictViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields ='__all__'
		depth = 1					

