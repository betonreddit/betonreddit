"""betonreddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .views import home, home_files, instructions

from redditData.api import redApi


urlpatterns = [
    
    
    url(r'^accounts/', include('allauth.urls'), name="google-login"),
    
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
        
    url(r'^accounts/logout', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
    url(r'i18n/', include('django.conf.urls.i18n')),

    url(r'^admin/', admin.site.urls),
    url(r'^subreddit/(?P<sub>[-\w]+)/$', redApi().getSub, name="subreddit"), # the first parameter is classed as the subreddit name
    url(r'^post/(?P<url>.*)/$', redApi().getPost, name="post"), # This is to allow parameters with /'s in
    
    url(r'^history/', include('history.urls')),
    url(r'highscore/', include('highscore.urls')),
    url(r'live/', include('live.urls')),

    url(r'^instructions/', instructions, name="instructions"),
    
    url(r'^$', home, name="home")#Home page. I think order matters, and this should be at the end. Probably.
]


