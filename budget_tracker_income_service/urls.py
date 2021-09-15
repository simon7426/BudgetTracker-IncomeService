from django.contrib import admin
from django.urls import path
from core.views import IncomeCategoryList, IncomeCategoryDetail, IncomeList, IncomeDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('income/category/',IncomeCategoryList.as_view()),
    path('income/category/<int:pk>',IncomeCategoryDetail.as_view()),
    path('income/',IncomeList.as_view()),
    path('income/<int:pk>',IncomeDetail.as_view()),
]
