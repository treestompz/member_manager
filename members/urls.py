from django.urls import path

from .views import MemberCreateView, MemberDeleteView, MemberListView, MemberUpdateView

urlpatterns = [
    path("", MemberListView.as_view(), name="member-list"),
    path("add/", MemberCreateView.as_view(), name="member-add"),
    path("edit/<int:pk>/", MemberUpdateView.as_view(), name="member-edit"),
    path("delete/<int:pk>/", MemberDeleteView.as_view(), name="member-delete"),
]
