from django.conf.urls import include, url

from views import HomePageView, FixedRoadsView, NotFixedRoadsView, desa_datasets, brokenroadunfixed_datasets, brokenroadfixed_datasets, DataInput

urlpatterns=[
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^fixedroads$', FixedRoadsView.as_view(), name = 'fixed'),
    url(r'^roadsinfo$', NotFixedRoadsView.as_view(), name = 'notfixed'),
    url(r'^add/$', DataInput.as_view(), name = 'add'),
    url(r'^desa_data/$', desa_datasets, name = 'desa'),
    url(r'^jalanrusakfixed_data/$', brokenroadfixed_datasets, name = 'brokenroadfixed'),
    url(r'^jalanrusakunfixed_data/$', brokenroadunfixed_datasets, name = 'brokenroadunfixed'),

]
