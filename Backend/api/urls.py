from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('group/', GroupListAPIView.as_view()),
    path('group/<int:group_id>/', GroupDetailAPIView.as_view()),
    path('user/', UserListAPIView.as_view()),
    path('tutors/', TutorListAPIView.as_view()),
    path('students/', StudentListAPIView.as_view()),
    path('user/<int:user_id>', UserDetailAPIView.as_view()),
    path('room/', RoomListAPIView.as_view()),
    path('room/<int:room_id>', RoomDetailAPIView.as_view()),
    path('event/', EventListAPIView.as_view()),
    path('event/<int:event_id>', EventDetailAPIView.as_view()),
    path('available_rooms/', get_available_rooms),
    path('get_user_events/', get_users_events),
    path('get_tutor_events/', get_tutor_events),
    path('roles/', get_roles)
    # comment to check
]
