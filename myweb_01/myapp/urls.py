from django.urls import path, include
from . import views

urlpatterns = [
    # path('',views.def后面跟的函数定义的名称,name)
    path('', views.login, name='login'),
    path('login/register', views.register, name='register'),
    path('regist_sql', views.regist_sql, name='regist_sql'),
    path('login/login_judge', views.login_judge, name='login_judge'),
    path('flash/', views.flash, name='flash'),
    path('muchao/<int:station_id>/<int:rightnum>', views.muchao, name='muchao'),
    path('station/<int:station_id>/<int:rightnum>',
         views.station, name='station'),
    path('mission_go/<int:station_id>/<int:rightnum>',
         views.mission_go, name='mission_go'),
    path('pictures/<int:station_id>', views.picture, name='picture'),
    path('select', views.select, name='select'),
    path('station/add', views.add, name='add'),
    path('station/delete', views.delete, name='delete'),
    path('add_sql', views.add_to_sql, name='add_to_sql'),
    path('delete_sql', views.delete_to_sql, name='delete_to_sql'),

]
