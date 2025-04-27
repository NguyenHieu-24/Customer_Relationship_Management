# đường dẫn đến các chức năng của website
    # vd: path('record/<int:pk>', views.customer_record, name='record'), có đường dẫn: http://localhost:8000/record/1

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    #tạo trang Login riêng biệt nên bỏ dòng trên

    # logout/, register/, record/, delete_record/, add_record/, update_record/: tương thích với các files html
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),

]
