from django.urls import path
from Courses import views

urlpatterns = [
    path('courses/recently-added/', views.recently_added_courses, name='recently_added_courses'),
    path('courses/featured/', views.featured_courses, name='featured_courses'),
    path('courses/', views.course_api, name='course_api_create'),
    path('courses/<str:id>/', views.course_api, name='course_api_read_delete'),
    path('courses/by-instructor/<str:instructor_name>/', views.courses_by_instructor, name='courses_by_instructor'),
    path('courses/by-category/<str:category>/', views.courses_by_category, name='courses_by_category'),
    path('courses/comments/<str:id>/', views.update_course_comments, name='update_course_comments'),
    path('courses/by-key-word/<str:key_word>/', views.get_courses, name='courses_by_key_word'),
]