from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]



# import requests

# url = "https://g.payx.ph/payment_request"

# payload={'x-public-key': 'pk_4770154a3e272ee2c24b611291015b2c',
# 'amount': '100',
# 'description': 'Payment for services rendered',
# }


# response = requests.request("POST", url, data=payload)

# print(response.text)


# curl --location --request POST 'https://g.payx.ph/payment_request' \
# --form 'x-public-key="pk_4770154a3e272ee2c24b611291015b2c"' \
# --form 'amount="100"' \
# --form 'description="Payment for services rendered"'