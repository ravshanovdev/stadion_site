from django.urls import path
from .views import CreateStripeCheckoutSession  # StripeWebhookView

urlpatterns = [
    path('create-checkout/<int:stadion_id>/', CreateStripeCheckoutSession.as_view()),
    # path('webhook/', StripeWebhookView.as_view(), name="stripe-webhook"),
]
