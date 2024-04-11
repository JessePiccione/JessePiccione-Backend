from django.urls import path
from .views import *
urlpatterns = [
    path('award', AwardListView.as_view()),
    path('award/<int:pk>', AwardDetailsView.as_view()),
    path('education', EducationListView.as_view()),
    path('education/<int:pk>',EducationDetailsView.as_view()),
    path('work-experience', WorkExperienceListView.as_view()),
    path('work-experience/<int:pk>', WorkExperienceDetailsView.as_view()),
    path('message', MessageListView.as_view()),
    path('message', MessageCreateView.as_view()),
    path('message/<int:pk>', MessageDetailsView.as_view()),
    path('skill', SkillListView.as_view()),
    path('skill/<int:pk>', SkillDetailsView.as_view()),
    path('skill-category', SkillCategoryListView.as_view()),
    path('skill-category/<int:pk>', SkillCategoryDetailsView.as_view()),
    path('projects', ProjectListView.as_view()),
    path('projects/<int:pk>', ProjectDetailsView.as_view())
]