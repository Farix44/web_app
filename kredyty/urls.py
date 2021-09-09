from django.urls import path
from kredyty.views import loan_list, new_loan, edit_loan, delete_loan

# REST_FRAMEWORK:
from rest_framework import routers
from django.conf.urls import include
from kredyty.views import UserViewSet, LoansViewSet, ClientsViewSet

router = routers.DefaultRouter()
router.register(r'loans', LoansViewSet, basename='loans')
router.register(r'clients', ClientsViewSet, basename='clients')

urlpatterns = [
    path('list/', loan_list, name="loan_list"),
    path('new/', new_loan, name="new_loan"),
    path('edit/<int:id>/', edit_loan, name="edit_loan"),
    path('delete/<int:id>/', delete_loan, name="delete_loan"),
    path('', include(router.urls)),
]
