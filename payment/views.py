from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import stripe
from django.conf import settings
from stadions.models import Stadion, OrderStadion
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateStripeCheckoutSession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, stadion_id):
        stadion = Stadion.objects.get(id=stadion_id)

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': stadion.name,
                    },
                    'unit_amount': int(stadion.price * 100),  # Stripe = cent
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )

        # Order yaratish
        order = OrderStadion.objects.create(
            stadion=stadion,
            user=request.user,
            stripe_session_id=session.id
        )

        return Response({'checkout_url': session.url})


# @method_decorator(csrf_exempt, name='dispatch')
# class StripeWebhookView(APIView):
#     def post(self, request, *args, **kwargs):
#         payload = request.body
#         sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
#         endpoint_secret = settings.STRIPE_WEBHOOK_SECRET  # CLI orqali beriladi
#
#         try:
#             event = stripe.Webhook.construct_event(
#                 payload, sig_header, endpoint_secret
#             )
#         except ValueError as e:
#             # Invalid payload
#             return Response({"error": str(e)}, status=400)
#         except stripe.error.SignatureVerificationError as e:
#             # Invalid signature
#             return Response({"error": str(e)}, status=400)
#
#         # Test eventlar bilan ishlash:
#         if event['type'] == 'checkout.session.completed':
#             session = event['data']['object']
#             print("Payment success:", session)
#
#         return Response({'status': 'success'})

