from django.urls import path
from .views import BookmarkList, BookmarkCreate, BookmarkDelete, BookmarkDetail, BookmarkUpdate

urlpatterns = [
    path('',BookmarkList.as_view(), name='bookmark_list'),
    path('create/',BookmarkCreate.as_view(), name='bookmark_create'),
    path('update/<int:pk>/',BookmarkUpdate.as_view(), name='bookmark_update'),
    path('detail/<int:pk>/',BookmarkDetail.as_view(), name='bookmark_detail'),
    path('delete/<int:pk>/',BookmarkDelete.as_view(), name='bookmark_delete'),

]