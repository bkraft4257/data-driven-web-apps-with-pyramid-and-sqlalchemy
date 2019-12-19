from pyramid.view import view_config


@view_config(route_name='account',
             renderer='pypi:templates/account/index.pt',
             request_method='GET')
def index(request):
    return {}


# LOGIN ###################################################################
@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='GET')
def login_get(request):
    return {}


@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='POST')
def login_post(request):
    return {}


# REGISTER ###################################################################
@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='GET')
def register_get(request):
    return {}


@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='POST')
def register_post(request):
    return {}


# LOGOUT ###################################################################

@view_config(route_name='logout',
             renderer='pypi:templates/account/login.pt',
             request_method='GET')
def logout(request):
    return {}
