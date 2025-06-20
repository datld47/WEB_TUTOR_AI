from django.shortcuts import render
from django.http import HttpResponse,JsonResponse  # <--- THÊM DÒNG NÀY
import uuid
# Bạn có thể có các dòng code khác ở đây (như Models, hoặc các View cũ nếu có)
# Hãy giữ nguyên chúng và chỉ thêm hàm hello_world này vào cuối file.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == '1':
            # return redirect('tutor_ai_app:dashboard') # Chuyển hướng đến trang quản lý
            session_id = str(uuid.uuid4())
            
            # Store the session ID in Django's session
            request.session['session_id'] = session_id
            request.session['role'] = 'admin' # Store role in session as well
           
            response_data = {
                "message": "Trang Admin",
                "role":"admin",
                "status": "success",
                "api_version": "1.0",
                "session_id": session_id 
            }
            return  JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
        elif username == 'dat' and password == '1':
            response_data = {
                "message": "Trang User",
                "role":"user",
                "status": "success",
                "api_version": "1.0"
            }
            return  JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
        else:
            return render(request, 'tutor_app/login_form.html', {'error_message': 'Sai tên đăng nhập hoặc mật khẩu.'})

    else: # request.method == 'GET'
        # Đây là lần đầu tiên người dùng truy cập trang đăng nhập
        # hoặc khi trình duyệt yêu cầu hiển thị form trống
        print('render login_form.html')
        return render(request, 'tutor_app/login_form.html')