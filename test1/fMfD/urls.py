# fMfD/urls.py
from django.urls import path
from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib import staticfiles
#app_name='fMfD'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('addComments/', views.addComments, name='addComments'),
    path('delComments/<int:comments_id>', views.delComments, name='delComments'),

]
#urlpatterns += staticfiles_urlpatterns()
#path(route,view,kwargs,name) route是匹配url的准则，viewroute对应匹配的试图函数，name urls
#的名字
