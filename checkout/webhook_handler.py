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
            content=f'Webhook received: {event["type"]}',
            status=200)
        