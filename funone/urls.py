from django.urls import path

from . import views


urlpatterns = [ 
				path('', views.index, name='index'), # <= this one is the 1st resource to be hit in the app corresponding to http://HOST/fun/funone/
				path('digicon/<str:dealid>/', views.digicon, name='digicon'), # <= this one is [http://HOST/fun/funone/] (index) + [digicon/myinput/] (the thing in <> is the input)
				path('ecoreorgcreate/', views.ecoreorgcreate, name='ecoreorgcreate'),
]