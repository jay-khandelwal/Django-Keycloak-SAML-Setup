SAML_CONFIG = {
    "sp": {
        "entityId": "http://localhost:8000/metadata/",
        "assertionConsumerService": {
            "url": "http://localhost:8000/saml/acs/",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST",
        },
        "singleLogoutService": {
            "url": "http://localhost:8000/saml/logout/",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect",
        },
        "NameIDFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
        "x509cert": "",
        "privateKey": "",
    },
    "idp": {
        "entityId": "http://localhost:8080/realms/django_keycloak_realm",
        "singleSignOnService": {
            "url": "http://localhost:8080/realms/django_keycloak_realm/protocol/saml",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect",
        },
        "singleLogoutService": {
            "url": "http://localhost:8080/realms/django_keycloak_realm/protocol/saml",
            "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect",
        },
        "x509cert": "MIICuTCCAaECBgGRCZbo0zANBgkqhkiG9w0BAQsFADAgMR4wHAYDVQQDDBVkamFuZ29fa2V5Y2xvYWtfcmVhbG0wHhcNMjQwNzMxMTYxNzUwWhcNMzQwNzMxMTYxOTMwWjAgMR4wHAYDVQQDDBVkamFuZ29fa2V5Y2xvYWtfcmVhbG0wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDG52dDqNY0ZrLtVBRttsJdekUuibD25vrYcQ8cwaRZS0En28F3ggvgYEkBlnWPBQy+vCIeb05KyXET8jZp3ThugvHQO3tyBAUOQH8KHRAuDZIYzil7Bsm1iCEhXo4UvTCy0AM55OY0zWbgmkE5VsSIcPUD6S1AgHFj4JdIoUplbePNM3Ha4kZIDUyANRBq3LIG8x/mbzQNgRffH/mfU2ZBGx6nTjRinhaXHxByHApFRj1syNj7g7Vwmd59+SWipokOGYXSu0Y/PYRN7KWDbr9I8/zoTufK6xSSLIJ/xgMonxFQGvt+oeR8770r1oJq+bV9aNcSXxN1u1HW87QK0bTrAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAEhcN/SfScS8wc9u/AfDoEWwEAnesHGSi9bPPSIn0JrCGYTvOqgcgDZin5hckj4hk1K+X88nXTWZnzW+j0QL1Sztbt1ZQL3425vH2VB7Eg3Gdn7z+5fcIF1CVos3iYh9yx6YbmSapj6Y+t2XEeYZK3BliBK6jIKLJSw7/fRpbkglTF7KF+ArzbGApyJep7aBpZRIVau5bxQqmlka/K+r3xBqfQIUpWOntQ4OOf8MJf5czimrsrqCEyc5cofVsSlbZKBV1AZXI18/oulMUsQ0VyDGUMwfSMqjk/NA6DCCyKL1Q0CCiMxItt0NJsWy5ynzEhbc4I37yVGg5e+NC9DzLPA=",
    },
    "security": {
        "authnRequestsSigned": False,
        "logoutRequestSigned": False,
        "logoutResponseSigned": False,
        "signatureAlgorithm": "rsa-sha256",
        "digestAlgorithm": "sha256",
        "wantAssertionsSigned": False,
        "wantMessagesSigned": False,
        "wantAssertionsEncrypted": False,
    },
    "debug": True,
}