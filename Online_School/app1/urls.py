from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('profile/<slug:profile_slug>/', views.show_profile, name='show_profile'),
    path('', views.show_courses,name='home'),
    path('login_done/category/<slug:category_slug>/', views.show_courses, name='Course_filter'),
    path('course_details/<int:id>', views.CourseDetailView.as_view(), name = 'course_details'),
    path('course_upload/', views.ChourseForm, name="store_course"),
    path('course_upload/<int:pk>', views.CourseUpdateView.as_view(), name = "edit_course"),
    path('delete_book/<int:pk>', views.DeleteCourseView.as_view(), name= "delete_course"),
    path('search/', views.search_feature, name='search-view'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.User_login, name='login'),
    path('login_done/', views.login_home , name='login_home'),
    path('profile/', views.profile , name='profile'),
    path('logout/', views.user_logout , name='logout'),
    path('changeuserdata/', views.ChangeUserData , name='changeuserdata'),
    path('changepass/', views.pass_change , name='passchange'),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
