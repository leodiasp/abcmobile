from django.conf.urls import url, include


from . import views

urlpatterns = [
    #url(r'^api/$', views.UserList.as_view(), name='user-list'),
    url(r'^usuario/$', views.UsuarioList, name='usuario-list'),
    #url(r'^api/users/$', views.UserList2.as_view(), name='user-list'),
    #url(r'^usuario/(?P<pk>[0-9]+)/$', views.UsuarioDetail.asview(), name='usuario-detail'),
    #url(r'^login/$', views.login_form, name='login'),
    #url(r'^auth/', include('rest_auth.urls')),
    #url(r'^responsavel/$',views.ResponsavelList.as_view(), name='responsavel-list'),
    url(r'^responsavel/$',views.ResponsavelList, name='responsavel-list'),

]