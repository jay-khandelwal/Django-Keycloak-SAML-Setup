from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from onelogin.saml2.auth import OneLogin_Saml2_Auth
from onelogin.saml2.errors import OneLogin_Saml2_ValidationError
from django.conf import settings


def prepare_django_request(request):
    return {
        'http_host': request.get_host(),
        'script_name': request.get_full_path(),
        'server_port': request.get_port(),
        'get_data': request.GET.copy(),
        'post_data': request.POST.copy()
    }

def saml_login(request):
    auth = OneLogin_Saml2_Auth(prepare_django_request(request), settings.SAML_CONFIG)
    return redirect(auth.login())

@csrf_exempt
def saml_acs(request):
    """ Handle SAML response from Keycloak and perform authentication. """
    auth = OneLogin_Saml2_Auth(prepare_django_request(request), settings.SAML_CONFIG)
    try:
        auth.process_response()
    except OneLogin_Saml2_ValidationError as e:
        return HttpResponse(f'SAML Validation Error: {e}', status=400)
    
    errors = auth.get_errors()

    # saml_response = auth.get_last_response_xml()
    # print('Full SAML Response:', saml_response)

    if errors:
        return HttpResponse(f'Error: {errors}', status=500)
    
    if not auth.is_authenticated():
        return HttpResponse('Not authenticated', status=401)

    user_data = auth.get_attributes()
    print('user_data: ', user_data)

    return redirect('/')

def saml_logout(request):
    auth = OneLogin_Saml2_Auth(prepare_django_request(request), SAML_CONFIG)
    return redirect(auth.logout())
