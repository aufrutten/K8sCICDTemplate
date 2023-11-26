from os import environ

AUTHENTICATION_BACKENDS = (
    # 'backend.components.OAuth2.backends.AppleIdAuth',
    # 'backend.components.OAuth2.backends.FacebookOAuth2',
    'backend.components.OAuth2.backends.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
)

# URL NAMESPACES
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:me'
LOGOUT_URL = 'accounts:logout'
LOGOUT_REDIRECT_URL = 'accounts:login'
SOCIAL_AUTH_URL_NAMESPACE = 'social'


AUTH_USER_MODEL = 'accounts.User'
AUTH_PROFILE_MODULE = 'accounts.User'
SOCIAL_AUTH_USER_MODEL = 'accounts.User'


# Allow to create user by social django
SOCIAL_AUTH_CREATE_USERS = True
SOCIAL_AUTH_EMAIL_AS_USERNAME = True
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_USER_FIELDS = ['first_name', 'last_name', 'email', 'photo', 'birthday', 'sex', 'is_active']


# =================================================================================================== #
# ===============                       CONFIGURATION                   ============================= #
# =================================================================================================== #


# AppleID TODO: Finish the apple configuration
# SOCIAL_AUTH_APPLE_ID_CLIENT = ''
# SOCIAL_AUTH_APPLE_ID_TEAM = ''
# SOCIAL_AUTH_APPLE_ID_KEY = ''
# SOCIAL_AUTH_APPLE_ID_SECRET = ''

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = environ.get('GOOGLE_CLIENT_ID', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = environ.get('GOOGLE_CLIENT_SECRET', '')

# Facebook
# SOCIAL_AUTH_FACEBOOK_KEY = ''
# SOCIAL_AUTH_FACEBOOK_SECRET = ''
