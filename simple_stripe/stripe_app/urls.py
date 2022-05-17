from django.urls import path

from stripe_app.views import HomePageView, CreateCheckoutSession

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('create-chekout-session/', CreateCheckoutSession.as_view()),
]
