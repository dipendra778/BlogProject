
from django.contrib.auth.views import LoginView

from django.urls import path
from BlogApp import views


urlpatterns = [
    path('',views.displaypost,name='home'),
    path('account/login', LoginView.as_view(template_name='login.html'), name="login"),
    path('account/logout',views.logout_view,name="logout"),
    path('about',views.about_view,name='about'),
    path('post',views.createpost,name='post'),
    path('crud',views.crud_view,name='crud'),
    path('delete/<int:id>', views.deleteView, name='post_delete'),
    path('update/<int:pk>',views.UpdatePostArticle.as_view(),name='post_update'),
    path('detail/<int:pk>',views.DetailPostArticles.as_view(),name='post-details')


]
