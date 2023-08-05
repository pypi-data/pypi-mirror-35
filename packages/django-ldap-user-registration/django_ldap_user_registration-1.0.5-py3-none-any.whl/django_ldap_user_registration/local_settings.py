# Site
SITE_BASE_URL = 'http://localhost:8000' # No trailing slash

TIME_ZONE = 'Africa/Nairobi'

# IDP Details
IDP_NAME = 'IDP Y'
IDP_LOGO = 'https://www.kenet.or.ke/sites/default/files/kenelogomedium.png' # Width of 200px at least

# Test service provider
SERVICE_PROVIDER = 'Test service provider'
SERVICE_PROVIDER_URL = 'https://test-service.kenet.or.ke'

# This setting enables capturing of a users institution and country details
IDP_CATCH_ALL = False

# LDAP Settings

LDAP_PROTO = 'ldap'
LDAP_HOST = '197.136.2.230'
LDAP_PORT = '389' # must be str
LDAP_BASE_DN = 'ou=users,dc=zion,dc=ac,dc=ke'
LDAP_BIND_DN = 'cn=admin,dc=zion,dc=ac,dc=ke'
LDAP_BIND_DN_CREDENTIAL = 'Trenchtown'
LDAP_GID = "500"
LDAP_BASE_UID = 1000 # Integer

# Password Reset

PASSWORD_RESET_TOKEN_EXPIRY = 2 #Hours

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

ANYMAIL = {
        "MAILGUN_API_KEY": "9f68cf8b76822f8df19902a6d5bfe2c41cb82133",
}

DEFAULT_FROM_EMAIL = IDP_NAME + ' <support@kenet.or.ke>'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
