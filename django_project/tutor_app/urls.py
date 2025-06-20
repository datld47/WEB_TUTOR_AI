from django.urls import path
from . import views # Import views từ ứng dụng hiện tại

app_name = 'tutor_app' # <-- Bạn khai báo ở đây

urlpatterns = [
    # Định nghĩa một URL cho trang "Hello World"
    # Khi truy cập đường dẫn '/hello/', nó sẽ gọi hàm views.hello_world
    path('login/', views.user_login, name='user_login'), 
    # Nếu bạn có các Views khác (như message_list từ bài trước) thì có thể thêm vào đây:
    # path('', views.message_list, name='message_list'), 
]