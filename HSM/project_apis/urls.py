from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.ListHsmUserSerializer.as_view()),
    path('users/<int:pk>/', views.DetailHsmUserSerializer.as_view()),
    path('society/', views.ListHsmSocietySerializer.as_view()),
    path('society/<int:pk>/', views.DetailHsmSocietySerializer.as_view()),
    path('flat/', views.ListHsmFlatSerializer.as_view()),
    path('flat/<int:pk>/', views.DetailHsmFlatSerializer.as_view()),
    path('notice/', views.ListHsmNoticeSerializer.as_view()),
    path('notice/<int:pk>/', views.DetailHsmNoticeSerializer.as_view()),
    path('member/', views.ListHsmMemberSerializer.as_view()),
    path('member/<int:pk>/', views.DetailHsmMemberSerializer.as_view()),
    path('maintenance/', views.ListHsmMaintenanceSerializer.as_view()),
    path('maintenance/<int:pk>/', views.DetailHsmMaintenanceSerializer.as_view()),
    path('maintenance_line/', views.ListHsmMaintenanceLineSerializer.as_view()),
    path('maintenance_line/<int:pk>/', views.DetailHsmMaintenanceLineSerializer.as_view()),
    path('helpdesk/', views.ListHsmHelpdeskSerializer.as_view()),
    path('helpdesk/<int:pk>/', views.DetailHsmHelpdeskSerializer.as_view()),
    path('product/', views.ListHsmProductDetailSerializer.as_view()),
    path('product/<int:pk>/', views.DetailHsmProductDetailSerializer.as_view()),
    path('vendor/', views.ListHsmVendorDetailSerializer.as_view()),
    path('vendor/<int:pk>/', views.DetailHsmVendorDetailSerializer.as_view()),
    path('purchase_order/', views.ListHsmPurchaseOrderSerializer.as_view()),
    path('purchase_order/<int:pk>/', views.DetailHsmPurchaseOrderSerializer.as_view()),
    path('purchase_order_line/', views.ListHsmPurchaseOrderLineSerializer.as_view()),
    path('purchase_order_line/<int:pk>/', views.DetailHsmPurchaseOrderLineSerializer.as_view()),
    path('country/', views.ListHsmResCountrySerializer.as_view()),
    path('country/<int:pk>/', views.DetailHsmResCountrySerializer.as_view()),
    path('state/', views.ListHsmResStateSerializer.as_view()),
    path('state/<int:pk>/', views.DetailHsmResStateSerializer.as_view()),
    path('partner_type/', views.ListHsmResPartnerTypeSerializer.as_view()),
    path('partner_type/<int:pk>/', views.DetailHsmResPartnerTypeSerializer.as_view()),
    path('post/', views.ListHsmResPostSerializer.as_view()),
    path('post/<int:pk>/', views.DetailHsmResPostSerializer.as_view()),
    path('wing/', views.ListHsmResWingSerializer.as_view()),
    path('wing/<int:pk>/', views.DetailHsmResWingSerializer.as_view()),
    path('service/', views.ListHsmServiceSerializer.as_view()),
    path('service/<int:pk>/', views.DetailHsmServiceSerializer.as_view()),
    path('service_line/', views.ListHsmSocietyServiceLineSerializer.as_view()),
    path('service_line/<int:pk>/', views.DetailHsmSocietyServiceLineSerializer.as_view()),
    path('complaint/', views.ListHsmComplaintCategorySerializer.as_view()),
    path('complaint/<int:pk>/', views.DetailHsmComplaintCategorySerializer.as_view()),
    path('product_category/', views.ListHsmResProductCategorySerializer.as_view()),
    path('product_category/<int:pk>/', views.DetailHsmResProductCategorySerializer.as_view()),
    path('user_token/', views.ListHsmUserTokenSerializer.as_view()),
]