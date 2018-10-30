from django.conf.urls import url, include


from . import views

urlpatterns = [
    #url(r'^api/$', views.UserList.as_view(), name='user-list'),
    #url(r'^api/users/$', views.UserList2.as_view(), name='user-list'),
    #url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserList.as_view(), name='user-list'),
    url(r'^login/$', views.login_form, name='login'),
    #url(r'^auth/', include('rest_auth.urls')),
    #url(r'^responsavel/$',views.ResponsavelList.as_view(), name='responsavel-list'),
    url(r'^responsavel/$',views.ResponsavelList, name='responsavel-list'),

]