from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


# 7. The benefit to using a generic view instead of "the hard way" is because it abstracts a lot of the necessry code to display data.
# So displaying data is easier with generic views. However they should not be used if you will be manipulating data in the view.

# 8. It's a good idea to write unit tests to ensure your classes are durable and accurate for all potential use cases.
# Test cases also allow you to test certain situations which would be hard to manually test.