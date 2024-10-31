from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="index"),
    #path('data/', views.data),
    #path('login/', views.login),
    #path('form/', views.form),
    #path('form_view/', views.form_view),
    #path('success/', views.success, name="success"),
    #path('upload/', views.upload_file, name='upload_file'),
    #path('uploadList/', views.uploadList, name='upload_list'),
    #path('calendar/', views.HomeView.as_view(), name='home'),
    path('register/', views.register_view ,name='register'),
    path('login/', views.login_view ,name='login'),
    path('logout/', views.logout_view ,name='logout'),
    path('dashboard/', views.dashboard_view ,name='dashboard'),
    path("dashboard/update/<int:id>/",views.updateProfile,name="updateProfile"),
    path("dashboard/update/uprec/<int:id>/",views.uprecProfile,name="uprecProfile"),

    path('adminDashboard/', views.adminDashboard_view ,name='adminDashboard'),
    

    path('add/',views.add,name="addUser"),
    path('adminEditUser/',views.adminDash,name="adminDashUser"),
    path("adminEditUser/addrec/",views.addrec,name="addrecUser"),
    path('adminEditUser/delete/<int:id>/',views.delete,name="deleteUser"),
    path('adminEditUser/update/<int:id>/',views.update,name="updateUser"),
    path('adminEditUser/update/uprec/<int:id>/',views.uprec,name="uprecUser"),

    path('addCar/',views.addCar,name="addCar"),
    path('adminEditCar/',views.adminDashCar,name="adminDashCar"),
    path("adminEditCar/addrec/",views.addrecCar,name="addrecCar"),
    path('adminEditCar/delete/<int:id>/',views.deleteCar,name="deleteCar"),
    path('adminEditCar/update/<int:id>/',views.updateCar,name="updateCar"),
    path('adminEditCar/update/uprec/<int:id>/',views.uprecCar,name="uprecCar"),

    path('calendar/', views.HomeView.as_view(), name='home'),
    path('selectcar/', views.carList ,name='selectcar'),
    path('selectcar/selectedCar/<int:id>',views.selectedCarList,name="carListSelected"),
    path('upload/', views.upload_pdf, name='upload_file'),
    path('adminBookingRequest/', views.adminBooking, name='adminBookingRequest'),
    path('adminBookingRequest/<int:id>', views.updateApprove, name='updateApproveAdmin'),
    path('adminBookingRequest/update/<int:id>', views.updateRequest, name='updateRequest'),
    path('adminBookingRequest/delete/<int:id>', views.deleteRequest, name='delteRequest'),
    path('adminBookingRequest/update/updateRe/<int:id>', views.updateRe, name='updateRe'),
    #path('selectcar/', views.carList ,name='selectcar'),
    #path('selected/', views.upload_pdf ,name='upload_pdf'),
]