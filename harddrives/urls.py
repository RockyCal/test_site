from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from harddrives.models import File, Harddrive, Box, Employee

urlpatterns = patterns('harddrives.views',


# Homepage
    url(r'^$', 'homepage',{
        'template_name' : 'harddrives/homepage.html'},
         name='testsite_homepage'),

# Checkout
    url(r'^checkout/$', 'checkout', {
         'template_name' : 'harddrives/checkout.html'},
         name='testsite_checkout'),

# File details
    url(r'^detailfile/(?P<new_name>\w+)/$', 'detailfile', {
         'template_name' : 'harddrives/detailfile.html'},
         name='testsite_detailfile'),
    url(r'^historyfile/(?P<name>\w+)/$', 'historyfile', {
         'template_name' : 'harddrives/historyfile.html'},
         name='testsite_historyfile'),
    url(r'^(allfiles)/$', ListView.as_view(
        model=File,), name='testsite_allfiles'),

    url(r'^addfile/$', 'addfile',{},
         name='testsite_addfile'),
    url(r'^findfile/$', 'findfile',{}, 
         name='testsite_findfile'),
# Owner details
    url(r'^detailowner/(?P<name>\w+)/$', 'detailowner', {
         'template_name' : 'harddrives/detailowner.html'},
         name='testsite_detailowner'),
    url(r'^historyowner/(?P<name>\w+)/$', 'historyowner', {
         'template_name' : 'harddrives/historyowner.html'},
         name='testsite_historyowner'),

    url(r'^allemployees/$', ListView.as_view(
        model=Employee,), name='testsite_allemployees'),
    url(r'^allboxes/$', ListView.as_view(
        model=Box,), name ='testsite_allboxes'),

# Harddrive details
    url(r'^detailharddrive/(?P<serial_num>\w+)/$', 'detailharddrive', {
         'template_name' : 'harddrives/detailharddrive.html'},
         name='testsite_detailharddrive'),
#    url(r'^historyharddrive/(?<serial_num>\w+)/$', 'historyharddrive', {
#         'template_name' : 'harddrives/historyharddrive.html'},
#         name='testsite_historyharddrive'),
    url(r'^allharddrives/$', ListView.as_view(
        model=Harddrive,), name='testsite_allharddrives'),

#    url(r'^addharddrive/(?P<file_name>\w+)/$', 'addharddrive', {},
#         name='testsite_addharddrive'),

)

