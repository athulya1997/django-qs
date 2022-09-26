"""batch1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from student.views import *

urlpatterns = [
    
    # path('start/<int:data>',startpage),
    path('sample/',sample,name='sample'),
    path('startpage/<data>',startPage,name='start'),
    path('reg/',viewreg,name='reg'),
    path('stat/',statview,name='stati'),
    path('large/<int:data1>/<int:data2>/<int:data3>/',large,name='large'),
    path('viewdata/',viewdata,name='viewdata'),
    path('editdata/<id>',editdata,name='editdata'),
    path('deletedata/<id>',deletedata,name='deletedata'),
    path('regformview/',RegFormView,name="regformview"),
    path('viewmodelform/',viewmodelform,name='viewmodelform'),
    path('employee/',employee,name='employee'),
    path('viewemp/',viewemp,name='viewemp'),
    path('uploadfile/',uploadfile,name='uploadfile'),
    path('uploadimage/',uploadimage,name='uploadimage'),
    path('flist/',UploadFileListView.as_view(),name='filelist'),
    path('fcreate/',CreateFileView.as_view(),name='fcreate'),
    path('fc/',CreateFileModelView.as_view(),name="fc"),
    path('cook/',cookcreate,name="c"),
    path('rcook/',readcook,name="r"),
    path('cookieform/',cookie_form,name='cookieform'),
    path('sesscreate/',sess_create,name='ses'),
    path('sessread/',readsess,name='rses'),
    path('logoutcook/',logoutuser,name='logoutcook'),
    path('ses_reg/',ses_reg,name='ses_reg'),
    path('loginuser/',loginuser,name='loginuser'),
    path('logoutses/',logout,name='logoutses'),
    path('details/',details,name='details'),
    path('viewjsontable/<user>',viewjsontable,name='jsontable'),
]
