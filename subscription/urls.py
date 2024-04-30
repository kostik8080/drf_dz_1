from django.urls import path

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionView

app_name = SubscriptionConfig.name

urlpatterns = [
    path('subscriptions/', SubscriptionView.as_view(), name='subscriptions')
]
