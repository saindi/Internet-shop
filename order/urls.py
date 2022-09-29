from django.urls import path
from order import views

app_name = "order"

urlpatterns = [
    path('order/create/', views.order_create_view, name='create'),
    path('order/cancellations/', views.cancellation_list_view, name='cancellations_list'),
    path('order/cancellation/create/<int:order_id>', views.cancellation_create_view, name='cancellation_create'),
    path('order/cancellation/confirm/<int:cancellation_id>', views.cancellation_confirm_view, name='cancellation_confirm'),
    path('order/cancellation/cancel/<int:cancellation_id>', views.cancellation_cancel_view, name='cancellation_cancel'),


    path('api/order-item/',
         views.OrderItemViewSet.as_view(
             {
                 'get': 'list',
                 'post': 'create'
             }),
         name="api_order-items"),

    path('api/order-item/<int:pk>/',
         views.OrderItemViewSet.as_view(
             {
                 'get': 'retrieve',
                 'put': 'update',
                 'delete': 'destroy'
             }),
         name="api_order-item"),


    path('api/order/',
         views.OrderViewSet.as_view(
             {
                 'get': 'list',
                 'post': 'create'
             }),
         name="api_orders"),

    path('api/order/<int:pk>/',
         views.OrderViewSet.as_view(
             {
                 'get': 'retrieve',
                 'put': 'update',
                 'delete': 'destroy'
             }),
         name="api_order"),


    path('api/cancellation/',
         views.CancellationViewSet.as_view(
             {
                 'get': 'list',
                 'post': 'create'
             }),
         name="api_cancellations"),

    path('api/cancellation/<int:pk>/',
         views.CancellationViewSet.as_view(
             {
                 'get': 'retrieve',
                 'put': 'update',
                 'delete': 'destroy'
             }),
         name="api_cancellation"),
]