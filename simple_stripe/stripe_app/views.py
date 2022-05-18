import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, DetailView

from simple_stripe import settings
from stripe_app.models import Item

domain_url = 'http://localhost:8000/'
stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'stripe_app/success.html'


class CancelledView(TemplateView):
    template_name = 'stripe_app/cancelled.html'


class CreateCheckoutSession(View):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': item.name},
                        'unit_amount': item.price
                    },
                    'quantity': 1
                }],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as ex:
            return JsonResponse({'error': str(ex)})


class StripeConfig(View):
    def get(self, request):
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class ItemDetailView(DetailView):
    model = Item
    template_name = 'stripe_app/item_detail.html'
