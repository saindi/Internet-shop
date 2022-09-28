from django.urls import path
from order import views

app_name = "order"

urlpatterns = [
    path('order/create/', views.order_create_view, name='create'),
    path('order/cancellations/', views.cancellation_list_view, name='cancellations_list'),
    path('order/cancellation/create/<int:order_id>', views.cancellation_create_view, name='cancellation_create'),
    path('order/cancellation/confirm/<int:cancellation_id>', views.cancellation_confirm_view, name='cancellation_confirm'),
    path('order/cancellation/cancel/<int:cancellation_id>', views.cancellation_cancel_view, name='cancellation_cancel'),

    path('api/order-item/', views.OrderItemListCreateAPIView.as_view(), name="api_order-items"),
    path('api/order-item/<int:pk>/', views.OrderItemRetrieveUpdateDestroyAPIView.as_view(), name="api_order-item"),

    path('api/order/', views.OrderListCreateAPIView.as_view(), name="api_orders"),
    path('api/order/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view(), name="api_order"),

    path('api/cancellation/', views.CancellationListCreateAPIView.as_view(), name="api_cancellations"),
    path('api/cancellation/<int:pk>/', views.CancellationRetrieveUpdateDestroyAPIView.as_view(), name="api_cancellation"),
]