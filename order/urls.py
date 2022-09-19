from django.urls import path
from order.views import (
    order_create_view,
    cancellation_list_view,
    cancellation_create_view,
    cancellation_confirm_view,
    cancellation_cancel_view
)

app_name = "order"

urlpatterns = [
    path('order/create/', order_create_view, name='create'),
    path('order/cancellations/', cancellation_list_view, name='cancellations_list'),
    path('order/cancellation/create/<int:order_id>', cancellation_create_view, name='cancellation_create'),
    path('order/cancellation/confirm/<int:cancellation_id>', cancellation_confirm_view, name='cancellation_confirm'),
    path('order/cancellation/cancel/<int:cancellation_id>', cancellation_cancel_view, name='cancellation_cancel'),
]