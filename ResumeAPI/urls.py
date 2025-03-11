from django.urls import path
from .views import *
urlpatterns = [
    path('award/', AwardListView.as_view()),
    path('award/<int:pk>/', AwardDetailsView.as_view()),
    path('award/category/', AwardCategoryListView.as_view()),
    path('award/category/<int:pk>/', AwardCategoryDetailsView.as_view()),
    path('education/', EducationListView.as_view()),
    path('education/<int:pk>/',EducationDetailsView.as_view()),
    path('work/experience/', WorkExperienceListView.as_view()),
    path('work/experience/<int:pk>/', WorkExperienceDetailsView.as_view()),
    path('message/', MessageCreateView.as_view()),
    path('skill/', SkillListView.as_view()),
    path('skill/<int:pk>/', SkillDetailsView.as_view()),
    path('skill/category/', SkillCategoryListView.as_view()),
    path('skill/category/<int:pk>/', SkillCategoryDetailsView.as_view()),
    path('project/', ProjectListView.as_view()),
    path('project/<int:pk>/', ProjectDetailsView.as_view()),
    path('home/',HomePageEntryListView.as_view()),
    path('home/<int:pk>/', HomePageEntryDetailsView.as_view()),
    path('technology/', TechnologyListView.as_view()),
    path('technology/<int:pk>/', TechnologyDetailsView.as_view())
]
