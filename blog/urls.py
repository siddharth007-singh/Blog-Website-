from django.contrib import admin
from django.urls import path
from datawork import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('detail/<int:post_id>', views.detail, name="detailpage"),
    path('meet_author', views.meet_author, name="meet_author"),
    path('searchbar', views.searchbar, name="searchbar"),
    path('category_filter/<int:cat_id>', views.category_filter, name="category_filter"),
    path('login', views.login, name="login"),
    path('signin', views.signin, name='signin'),
    path('user_dashboard', views.user_dashboard, name="user_dashboard"),
    path('user_insert_cat', views.user_insert_cat, name="insert_category"),
    path('user_insert_topic', views.user_insert_topic, name="insert_topic"),
    path('user_insert_post', views.user_insert_post, name="insert_post"),
    path('user_manage_post', views.user_manage_post, name="manage_post"),
    path('user_report', views.user_report, name="report"),
    path('user_profile', views.user_profile, name="profile"),
    path('user_edit_image/<int:nu_id>', views.user_edit_image, name="user_edit_image"),
    path('user_edit_info/<int:nu_id>', views.user_edit_info, name="user_edit_info"),
    path('user_view_post/<int:post_id>', views.user_view_post, name="user_view_post"),
    path('user_edit_post/<int:post_id>', views.user_edit_post, name="user_edit_post"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('secure_dashboard', views.secure_dashboard, name="secure_dashboard"),
    path('secure_manage_post', views.secure_manage_post, name="secure_manage_post"),
    path('secure_viewpost/<int:post_id>', views.secure_viewpost, name="secure_viewpost"),
    path('secure_edit/<int:post_id>', views.secure_edit, name="secure_edit"),
    path('secure_manage_user', views.secure_manage_user, name="secure_manage_user"),
    path('secure_manage_report', views.secure_manage_report, name="secure_manage_report"),
    path('secure_manage_profile', views.secure_manage_profile, name="secure_manage_profile"),
    path('like_deslike/<int:id>', views.like_dislike, name="like_deslike"),
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post"),
    path('logout', views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
