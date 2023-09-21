from django.http import HttpResponse

class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __init__(serlf, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpecte webhook event
        """

        return HttpRespnse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)
        
    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment_intent.succeeded webhook from Stripe
        """

        return HttpRespnse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle a payment_intent.payment_failed webhook from Stripe
        """

        return HttpRespnse(
            content=f'Webhook received: {event["type"]}',
            status=200)
        