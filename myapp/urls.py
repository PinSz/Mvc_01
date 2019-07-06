from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/$', views.testform, name='form'),
    url(r'^exam-form/$', views.exam_detail, name='exam-form'),
    url(r'^Employee-form/$', views.Employee_form, name='Employee-form'),
    url(r'^edit-form/$', views.my_edit, name='edit-form'),
    url(r'^view-form/$', views.view_form, name='view-form'),
]