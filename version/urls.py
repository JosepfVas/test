from django.urls import path
from version.views import VersionListView, VersionDetailView, VersionCreateView, VersionUpdateView, VersionDeleteView

urlpatterns = [
    path('', VersionListView.as_view(), name='version_list'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
    path('version/create/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),

]
