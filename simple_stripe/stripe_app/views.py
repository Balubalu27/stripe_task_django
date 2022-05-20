import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, TemplateView

from simple_stripe import settings
from stripe_app.constants import domain_url, success_url, cancel_url, currency
from stripe_app.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    """ Страница успешной оплаты """

    template_name = 'stripe_app/success.html'


class CancelledView(TemplateView):
    """ Страница при отмене оплаты """

    template_name = 'stripe_app/cancelled.html'


class CreateCheckoutSession(View):
    def get(self, request, pk):
        """ Получает объект item из БД и подставляет его в созданную сессию"""

        try:
            item = Item.objects.get(pk=pk)
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + success_url,
                cancel_url=domain_url + cancel_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    'price_data': {
                        'currency': currency,
                        'product_data': {'name': item.name},
                        'unit_amount': item.price
                    },
                    'quantity': 1
                }]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as ex:
            return JsonResponse({'error': str(ex)})


class StripeConfig(View):
    def get(self, request):
        """ Задаем stripe public key """

        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class ItemDetailView(DetailView):
    """ Отображение информации о объекте Item """

    model = Item
    template_name = 'stripe_app/item_detail.html'
