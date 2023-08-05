Configuration
=============

Available settings:

SITE_BASE_URL = 'http://example.com' # No trailing slash

TIME_ZONE = 'Africa/Nairobi'

# IDP Details
IDP_NAME = 'IDP Y'
IDP_LOGO = 'https://example.com/logo.jpg' # Width of 200px at least

# Test service provider
SERVICE_PROVIDER = 'Test service provider'
SERVICE_PROVIDER_URL = 'https://test-service.kenet.or.ke'

# This setting enables capturing of a users institution and country details
IDP_CATCH_ALL = False

# LDAP Settings

LDAP_PROTO = 'ldap'
LDAP_HOST = '127.0.0.1'
LDAP_PORT = '389' # must be str
LDAP_BASE_DN = 'ou=People,dc=zion,dc=ac,dc=ke'
LDAP_BIND_DN = 'cn=admin,dc=zion,dc=ac,dc=ke'
LDAP_BIND_DN_CREDENTIAL = 'admin'
LDAP_GID = "502" # group ID to add signed up users
LDAP_BASE_UID = 1000 # Integer

# Password Reset

PASSWORD_RESET_TOKEN_EXPIRY = 2 #Hours

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

ANYMAIL = {
        "MAILGUN_API_KEY": "<your key>",
}

DEFAULT_FROM_EMAIL = IDP_NAME + ' <support@example.com>'

CRISPY_TEMPLATE_PACK = 'bootstrap3