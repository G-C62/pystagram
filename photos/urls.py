from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'photos'

urlpatterns = [
    url(r'^list/$',     #list
    views.list_photos,
    name="list_photos"),

    url(r'^create_photo/$',    #사진생성
    login_required(views.PhotoCreate.as_view()),    #decorator를 url 전체에 걸어줌
    name="create_photo"),

    url(r'^delete_photo/(?P<pk>[0-9]+)$',     #사진삭제
    login_required(views.delete_photo),
    name="delete_photo"),

    url(r'^view_photo/(?P<pk>[0-9]+)/$',      #특정사진 보기
    views.view_photo,
    name="view_photo"),

#    url(r'^create_comment/(?P<pk>[0-9]+)/$',      #특정사진에 댓글달기
#    login_required(views.create_comment),
#    name="create_comment"),

#    url(r'^delete_comment/(?P<pk>[0-9]+)/$',      #특정사진에 댓글삭제
#    login_required(views.delete_comment),
#    name="delete_comment"),

]
