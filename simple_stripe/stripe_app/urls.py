from django.urls import path

from stripe_app.views import (CancelledView, CreateCheckoutSession,
                              ItemDetailView, StripeConfig, SuccessView)

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSession.as_view(), name='buy'),
    path('config/', StripeConfig.as_view(), name='config'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancelled/', CancelledView.as_view(), name='cancelled'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
]
