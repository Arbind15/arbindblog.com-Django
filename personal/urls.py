from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# to load search_word in logo
search_str=views.findkey()

urlpatterns =[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('gallery/',views.gallery,name='gallery'),
    path('codesnippets/',views.codesnippets,name='codesnippets'),
    path('downloads/',views.downloads,name='downloads'),
    path('acknlg/',views.acknlg,name='acknlg'),
    path('notes/',views.notes,name='notes'),
    path('search_result/',views.search_result,name='search_result'),
    path('signup/',views.signup,name='signup'),
    path('chat_board/',views.chat_board,name='chat_board'),
    path('profile/',views.profile,name='profile'),
    path('post/',views.post,name='post'),
    path('logout/', auth_views.LogoutView.as_view(template_name='personal/blog.html',extra_context={"search_str":search_str}), name='logout'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('edit_post/',views.edit_post,name='edit_post'),
    path('create_post/',views.create_post,name='create_post'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='personal/password_reset_request.html',), name='password_reset_request'),
    path('password_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='personal/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='personal/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='personal/password_reset_complete.html'), name='password_reset_complete'),
    # path('accounts/google/login/callback/',views.about,name='about'),
    # path('accounts/facebook/login/callback/',views.blog,name='blog'),
    path('activate/<uidb64>/<token>/',views.ActivateAccount.as_view(),name='activate'),
    path('verification/',views.verification,name='verification'),
    path('activation_fails/',views.activation_fails,name='activation_fails'),
]