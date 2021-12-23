from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import (TaskSerializer,ClassifiedSerializer,ClassifiedViewSerializer,
CategorySerializer,StatusSerializer,UsersSerializer,DistrictSerializer,StateSerializer,DistrictViewSerializer)

from .models import Task,Classified,Category,Status,Users,State,District
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Task_List':'/task-list/',
		'Task_Detail_View':'/task-detail/<str:pk>/',
		'Task_Create':'/task-create/',
		'Task_Update':'/task-update/<str:pk>/',
		'Task_Delete':'/task-delete/<str:pk>/',

		'Classified_List':'/classified-list/',
		'Classified_Detail_Edit':'/classified-edit/<str:pk>/',
		'Classified_Detail_View':'/classified-view/<str:pk>/',
		'Classified_By_User':'/classified-detail-byuser/<str:pk>/',
		'Classified_By_District':'/classified-list-bydistrict/<str:pk>/',
		'Classified_Create':'/classified-create/',
		'Classified_Update':'/classified-update/<str:pk>/',
		'Classified_Delete':'/classified-delete/<str:pk>/',

		'User_List':'/user-list/',
		'User_Detail_View':'/user-detail/<str:pk>/',
		'User_Create':'/user-create/',
		'User_Update':'/user-update/<str:pk>/',
		'User_Delete':'/user-delete/<str:pk>/',
		'User_UserName' : '/user-login/<str:pk>/',


		'Category_List':'/category-list/',
		'Category_Detail_View':'/category-detail/<str:pk>/',
		'Category_Create':'/category-create/',
		'Category_Update':'/category-update/<str:pk>/',
		'Category_Delete':'/category-delete/<str:pk>/',
		'Category_View':'/category-view/<str:pk>/',

		'Status_List':'/status-list/',
		'Status_Detail_View':'/status-detail/<str:pk>/',
		'Status_Create':'/status-create/',
		'Status_Update':'/status-update/<str:pk>/',
		'Status_Delete':'/status-delete/<str:pk>/',				

		'District_List':'/district-list/',
		'District_Detail_View':'/district-detail/<str:pk>/',
		'State_District_Detail_View':'/state_dist-detail/<str:pk>/',
		'District_Create':'/district-create/',
		'District_Update':'/district-update/<str:pk>/',
		'District_Delete':'/district-delete/<str:pk>/',

		'State_List':'/state-list/',
		'State_Detail_View':'/state-detail/<str:pk>/',
		'State_Create':'/state-create/',
		'State_Update':'/state-update/<str:pk>/',
		'State_Delete':'/state-delete/<str:pk>/',				
	}

	return Response(api_urls)

# =========	 Tasks

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

# # =========	 Ads	

# @api_view(['GET'])
# def adsList(request):
# 	ads = Ads.objects.all().order_by('-id')
# 	serializer = AdsSerializer(ads, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def adsDetail(request, pk):
# 	ads = Ads.objects.get(id=pk)
# 	serializer = AdsSerializer(ads, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# def adsCreate(request):
# 	serializer = AdsSerializer(data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)

# @api_view(['POST'])
# def adsUpdate(request, pk):
# 	ads = Ads.objects.get(id=pk)
# 	serializer = AdsSerializer(instance=ads, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def adsDelete(request, pk):
# 	ads = Ads.objects.get(id=pk)
# 	ads.delete()

# 	return Response('Ads succsesfully delete!')


# =========	 Classified	

@api_view(['GET'])
def classifiedList(request):
	classified = Classified.objects.all().order_by('-id')
	serializer = ClassifiedViewSerializer(classified, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def classifiedDetail(request, pk):
	classified = Classified.objects.get(id=pk)
	serializer = ClassifiedViewSerializer(classified, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def classifiedDetailByUserId(request, pk):
	classified = Classified.objects.filter(users_id=pk).order_by('-id')
	serializer = ClassifiedViewSerializer(classified, many=True)
	return Response(serializer.data)	

@api_view(['GET'])
def classifiedDetailByDistrictId(request, pk):
	classified = Classified.objects.filter(district_id=pk)
	serializer = ClassifiedViewSerializer(classified, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def classifiedCreate(request):
	parser_classes = [MultiPartParser, FormParser]	
	serializer = ClassifiedSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def classifiedUpdate(request, pk):
	classified = Classified.objects.get(id=pk)
	serializer = ClassifiedSerializer(instance=classified, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def classifiedDelete(request, pk):
	classified = Classified.objects.get(id=pk)
	classified.delete()

	return Response('Classified succsesfully delete!')

@api_view(['GET'])
def categoryClassifiedView(request, pk):
	classified = Classified.objects.filter(category_id=pk).order_by('-id')
	serializer = ClassifiedViewSerializer(classified, many=True)
	return Response(serializer.data)


# =========	 Category	

@api_view(['GET'])
def categoryList(request):
	category = Category.objects.all().order_by('-id')
	serializer = CategorySerializer(category, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def categoryDetail(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(category, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
	serializer = CategorySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def categoryUpdate(request, pk):
	category = Category.objects.get(id=pk)
	serializer = CategorySerializer(instance=category, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
	category = Category.objects.get(id=pk)
	category.delete()

	return Response('Category succsesfully delete!')



# =========	 Status	

@api_view(['GET'])
def statusList(request):
	status = Status.objects.all().order_by('-id')
	serializer = StatusSerializer(status, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def statusDetail(request, pk):
	status = Status.objects.get(id=pk)
	serializer = StatusSerializer(status, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def statusCreate(request):
	serializer = StatusSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def statusUpdate(request, pk):
	status = Status.objects.get(id=pk)
	serializer = StatusSerializer(instance=status, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def statusDelete(request, pk):
	status = Status.objects.get(id=pk)
	status.delete()

	return Response('Status succsesfully delete!')		


# =========	 User	

@api_view(['GET'])
def userList(request):
	user = Users.objects.all().order_by('-id')
	serializer = UsersSerializer(user, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
	user = Users.objects.get(id=pk)
	serializer = UsersSerializer(user, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
	serializer = UsersSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def userUpdate(request, pk):
	user = Users.objects.get(id=pk)
	serializer = UsersSerializer(instance=user, data=request.data, partial=True)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	user = Users.objects.get(id=pk)
	user.delete()

	return Response('User succsesfully delete!')


@api_view(['GET'])
def userLoginUserName(request, pk):
	users = Users.objects.get(user_name=pk)
	serializer = UsersSerializer(users, many=False)
	return Response(serializer.data)



# =========	 State	

@api_view(['GET'])
def stateList(request):
	state = State.objects.all().order_by('-id')
	serializer = StateSerializer(state, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def stateDetail(request, pk):
	state = State.objects.get(id=pk)
	serializer = StateSerializer(state, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def stateCreate(request):
	serializer = StateSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def stateUpdate(request, pk):
	state = State.objects.get(id=pk)
	serializer = StateSerializer(instance=state, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def stateDelete(request, pk):
	state = State.objects.get(id=pk)
	state.delete()

	return Response('State succsesfully delete!')


# =========	 District	

@api_view(['GET'])
def districtList(request):
	district = District.objects.all().order_by('-id')
	serializer = DistrictViewSerializer(district, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def districtDetail(request, pk):
	district = District.objects.get(id=pk)
	serializer = DistrictViewSerializer(district, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def statedistDetail(request, pk):
	state_district = District.objects.filter(state_id=pk)
	serializer = DistrictSerializer(state_district, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def districtCreate(request):
	serializer = DistrictSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def districtUpdate(request, pk):
	district = District.objects.get(id=pk)
	serializer = DistrictSerializer(instance=district, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def districtDelete(request, pk):
	district = District.objects.get(id=pk)
	district.delete()

	return Response('District succsesfully delete!')	