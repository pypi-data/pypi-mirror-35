from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.shortcuts import render_to_response
from dispatch.admin import views
import dispatch

def admin(request):
    """Render HTML entry point for manager app."""
    context = {
        'api_url': settings.API_URL,
        'app_js_bundle': 'manager-%s.js' % dispatch.__version__,
        'app_css_bundle': 'manager-%s.css' % dispatch.__version__
    }
    
    return render_to_response('manager/index.html', context)

urlpatterns = [
    url(r'signup/(?P<uuid>[0-9a-f-]+)/', views.signup, name='dispatch-signup'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'reset/done', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'.*', admin, name='dispatch-admin')
]
