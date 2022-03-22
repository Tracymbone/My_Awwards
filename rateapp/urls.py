# from django.conf.urls import url
from django.urls import path
from rateapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
   path('',views.login_view, name='login'),
  path('register/',views.register_view, name='register'),
  path('index/',views.index,name = 'index'),
  path('search/', views.search_results, name='search_results'),
  path('new/project$', views.new_project, name='new-project'),
  path('user/(?P<username>\w+)', views.profile, name='profile'),
  path('accounts/edit/', views.edit_profile, name='edit_profile'),
]

# if settings.DEBUG:
#   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)