from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.HomePage, name='home_page'),
	url(r'^login', views.login_page, name='login'),
	url(r'^requestlogin', views.login_request, name='reqlogin'),
	url(r'^logout', views.logout_page, name='logout'),
	url(r'^dashboard', views.dash, name='dashboard'),
	url(r'^403', views.denied_acc, name='403'),
	url(r'^404', views.no_res, name='404'),
	url(r'^register', views.register_page, name='register'),
	url(r'^addedu', views.edu_page, name='register'),
	url(r'^addexp', views.exp_page, name='register'),
	url(r'^addskill', views.skill_page, name='register'),
	url(r'^validate', views.register_val, name='register_val'),
	url(r'^expvalidate', views.add_exp, name='exp_val'),
	url(r'^skillvalidate', views.add_skill, name='skill_val'),
	url(r'^people', views.people, name='people'),
	url(r'^editprofile/main/submit', views.submitmainfields, name='submitmainfields'),
	url(r'^editprofile/main', views.editmainfields, name='editmainfields'),
	url(r'^editprofile/education/submit', views.edufieldsubmit, name='edufieldsubmit'),
	url(r'^editprofile/education/delete', views.edufielddelete, name='edufielddelete'),
	url(r'^editprofile/education/add', views.add_edu, name='edufieldcreate'),
	url(r'^editprofile/education', views.editedufields, name='editedufields'),
	url(r'^editprofile/experience/submit', views.expfieldsubmit, name='expfieldsubmit'),
	url(r'^editprofile/experience/delete', views.expfielddelete, name='expfielddelete'),
	url(r'^editprofile/experience/add', views.add_exp, name='expfieldcreate'),
	url(r'^editprofile/experience', views.editexpfields, name='editexpfields'),
	url(r'^editprofile/skills/submit', views.skillfieldsubmit, name='skillfieldsubmit'),
	url(r'^editprofile/skills/delete', views.skillfielddelete, name='skillfielddelete'),
	url(r'^editprofile/skills/add', views.add_skill, name='skillfieldcreate'),
	url(r'^editprofile/skills', views.editskillfields, name='editskillfields'),
	url(r'^test/(?P<string>[\w\-]+)/$', views.test, name='test'),
	url(r'^temp1/(?P<string>[\w\-]+)/$', views.temp1, name='temp1'),
	url(r'^dtemp1/(?P<string>[\w\-]+)/$', views.dtemp1, name='dtemp1'),
	url(r'^temp2/(?P<string>[\w\-]+)/$', views.temp2, name='temp2'),
	url(r'^dtemp2/(?P<string>[\w\-]+)/$', views.dtemp2, name='dtemp2'),
	url(r'^temp3/(?P<string>[\w\-]+)/$', views.temp3, name='temp3'),
	url(r'^dtemp3/(?P<string>[\w\-]+)/$', views.dtemp3, name='dtemp3'),
	url(r'^temp4/(?P<string>[\w\-]+)/$', views.temp4, name='temp4'),
	url(r'^dtemp4/(?P<string>[\w\-]+)/$', views.dtemp4, name='dtemp4')
]

