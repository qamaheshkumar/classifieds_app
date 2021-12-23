from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

	path('classified-list/', views.classifiedList, name="classified-list"),
	path('classified-edit/<str:pk>/', views.classifiedDetail, name="classified-edit"),
	path('classified-view/<str:pk>/', views.classifiedDetail, name="classified-view"),
	path('classified-detail-byuser/<str:pk>/', views.classifiedDetailByUserId, name="classified_by_user"),
	path('classified-list-bydistrict/<str:pk>/', views.classifiedDetailByDistrictId, name="classified_by_district"),
	path('classified-create/', views.classifiedCreate, name="classified-create"),
	path('classified-update/<str:pk>/', views.classifiedUpdate, name="classified-update"),
	path('classified-delete/<str:pk>/', views.classifiedDelete, name="classified-delete"),

	path('user-list/', views.userList, name="user-list"),
	path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
	path('user-create/', views.userCreate, name="user-create"),
	path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
	path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
	path('user-login/<str:pk>/', views.userLoginUserName, name="classified-user-login"),	

	path('category-list/', views.categoryList, name="category-list"),
	path('category-detail/<str:pk>/', views.categoryDetail, name="category-detail"),
	path('category-create/', views.categoryCreate, name="category-create"),
	path('category-update/<str:pk>/', views.categoryUpdate, name="category-update"),
	path('category-delete/<str:pk>/', views.categoryDelete, name="categoryser-delete"),
	path('category-view/<str:pk>/', views.categoryClassifiedView, name="categoryser-view"),

	path('status-list/', views.statusList, name="status-list"),
	path('status-detail/<str:pk>/', views.statusDetail, name="status-detail"),
	path('status-create/', views.statusCreate, name="status-create"),
	path('status-update/<str:pk>/', views.statusUpdate, name="status-update"),
	path('status-delete/<str:pk>/', views.statusDelete, name="status-delete"),

	path('district-list/', views.districtList, name="district-list"),
	path('district-detail/<str:pk>/', views.districtDetail, name="district-detail"),
	path('state_dist-detail/<str:pk>/', views.statedistDetail, name="state-district-detail"),
	path('district-create/', views.districtCreate, name="district-create"),
	path('district-update/<str:pk>/', views.districtUpdate, name="district-update"),
	path('district-delete/<str:pk>/', views.districtDelete, name="district-delete"),

	path('state-list/', views.stateList, name="state-list"),
	path('state-detail/<str:pk>/', views.stateDetail, name="state-detail"),
	path('state-create/', views.stateCreate, name="state-create"),
	path('state-update/<str:pk>/', views.stateUpdate, name="state-update"),
	path('state-delete/<str:pk>/', views.stateDelete, name="state-delete"),		
]
