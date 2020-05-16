"""packingkings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addadmin', addadmin),
    path('addadmin1', addadmin1),
    path('viewadmin', viewadmin),
    path('editadmin', editadmin),
    path('updateadmin', updateadmin),
    path('removeadmin', removeadmin),
    path('adminlogin', adminlogin),
    path('adminlogin1', adminlogin1),
    path('admindashboard', admindashboard),
    path('home', home),
    path('adminchangepassword', adminchangepassword),
    path('adminforgetpassword', adminforgetpassword),
    path('addnews', addnews),
    path('addnews1', addnews1),
    path('viewnews', viewnews),
    path('deletenews', deletenews),
    path('addpackages', addpackages),
    path('addpackages1', addpackages1),
    path('viewpackages', viewpackages),
    path('getlistofpackages',getlistofpackages),
    path('editpackages', editpackages),
    path('updatepackages', updatepackages),
    path('deletepackages', deletepackages),
    path('servicingstations', servicingstations),
    path('servicingstations1', servicingstations1),
    path('choosestate',choosestate),
    path('viewservicingstations',viewservicingstations),
    path('editservicestations',editservicestations),
    path('updateservicestations',updateservicestations),
    path('deleteservicingstations',deleteservicingstations),
    path('showcity', showcity),
    path('usersignup', usersignup),
    path('sendotp', sendotp),
    path('verifyotp', verifyotp),
    path('usersignup1', usersignup1),
    path('usersignup2', usersignup2),
    path('userlogin', userlogin),
    path('userlogin1', userlogin1),
    path('forgetpassword', forgetpassword),
    path('userchangepassword', userchangepassword),
    path('logout', logout),
    path('booking', booking),
    path('userbooking1', userbooking1),
    # path('bookingaction',bookingaction),
    # index temp urls
    path("", index),
    path("about", about),
    # path('sendmessage',sendmessage),
    path("contact", contact),
    path("login", login),
    path("userlogout", userlogout),
    path("register", register),
    path('searchpackages',searchpackages),
    path('getdescription',getdescription),
    path('thankspage',thankspage),
    path('viewbookings',viewbookings),
    path('viewbookingdetails',viewbookingdetails),
    # path('updatestatus',updatestatus),
    path('acceptbooking',acceptbooking),
    path('rejectbooking',rejectbooking),
    path('dispatch',dispatch),
    path('userviewbookingdetails',userviewbookindetails),
    path('reviews',reviews),
    path('addreviews',addreviews),
    path('sendratingmsgandemail',sendratingmsgandemail),
    path('updatetracking',updatetracking),
    path('trackbooking',trackbooking),
    path('searchforpackages',searchforpackages),
    path('searchforpackages1',searchforpackages1),
    path('viewschedulevisit',viewschedulevisit),
    path('findaveragerating',findaveragerating),
    # path('fetchquestions',fetchquestions)
]

