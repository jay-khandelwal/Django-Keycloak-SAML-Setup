from django.urls import path
from .views import saml_login, saml_acs, saml_logout

urlpatterns = [
    path('saml/login/', saml_login, name='saml_login'),
    path('saml/acs/', saml_acs, name='saml_acs'),
    path('saml/logout/', saml_logout, name='saml_logout'),
]
