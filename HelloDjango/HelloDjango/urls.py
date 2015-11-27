from django.conf.urls import patterns, include, url
from django.contrib import admin
from HelloDjango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HelloDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', views.hello), # 정규 표현식, URL이 'hello'로 시작하면 views 객체의 hello 메서드로 응답.
    url(r'^merong/', views.merong),
    url(r"^sample/", views.sample),
    url(r'^sample2/', views.sample2),
    url(r'^time/', views.currentTime),
    url(r'^friends/', views.friendList),
    url(r'^members/', views.memberList)
)