"""owid_grapher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from grapher_admin import views as admin_views
from owid_grapher import views as owid_views
from django.contrib.auth.views import logout

urlpatterns = [

    ### Admin-only

    url(r'^grapher/$', owid_views.index, name="index"),
    url(r'^grapher/charts/$', admin_views.listcharts, name="listcharts"),
    url(r'^grapher/charts$', admin_views.storechart, name="storechart"),  # post request for storing
    url(r'^grapher/charts/create/$', admin_views.createchart, name="createchart"),
    url(r'^grapher/charts/(?P<chartid>[\w]+)/edit/$', admin_views.editchart, name="editchart"),
    url(r'^grapher/charts/(?P<chartid>[\w]+)$', admin_views.managechart, name="managechart"),  # update, destroy requests
    url(r'^grapher/charts/(?P<chartid>[\w]+)/$', admin_views.showchart, name="showchartinternal"),
    url(r'^grapher/charts/(?P<chartid>[\w]+)/star$', admin_views.starchart, name="starchart"),
    url(r'^grapher/charts/(?P<chartid>[\w]+)/unstar$', admin_views.unstarchart, name="unstarchart"),
    url(r'^grapher/import/$', admin_views.importdata, name="importdata"),
    url(r'^grapher/import/variables$', admin_views.store_import_data, name="storeimportdata"),  # data import post requests
    url(r'^grapher/datasets/$', admin_views.listdatasets, name="listdatasets"),
    url(r'^grapher/datasets/(?P<datasetid>[\w]+)/$', admin_views.showdataset, name="showdataset"),
    url(r'^grapher/datasets/(?P<datasetid>[\w]+)$', admin_views.managedataset, name="managedataset"),
    url(r'^grapher/datasets/(?P<datasetid>[\w]+)/edit/$', admin_views.editdataset, name="editdataset"),
    url(r'^grapher/datasets/(?P<datasetid>[\w]+)\.csv$', admin_views.dataset_csv, name="datasetcsv"),
    url(r'^grapher/datasets/(?P<datasetid>[\w]+)\.json$', admin_views.dataset_json, name="datasetjson"),
    url(r'^grapher/categories/$', admin_views.listcategories, name="listcategories"),
    url(r'^grapher/categories/(?P<catid>[\w]+)/$', admin_views.showcategory, name="showcategory"),
    url(r'^grapher/categories/(?P<catid>[\w]+)$', admin_views.managecategory, name="managecategory"),
    url(r'^grapher/categories/(?P<catid>[\w]+)/edit/$', admin_views.editcategory, name="editcategory"),
    url(r'^grapher/variables/$', admin_views.listvariables, name="listvariables"),
    url(r'^grapher/variables/(?P<variableid>[\w]+)/$', admin_views.showvariable, name="showvariable"),
    url(r'^grapher/variables/(?P<variableid>[\w]+)$', admin_views.managevariable, name="managevariable"),
    url(r'^grapher/variables/(?P<variableid>[\w]+)/edit/$', admin_views.editvariable, name="editvariable"),
    url(r'^grapher/licenses/$', admin_views.listlicenses, name="listlicenses"),
    url(r'^grapher/licenses/(?P<licenseid>[\w]+)/$', admin_views.showlicense, name="showlicense"),
    url(r'^grapher/licenses/(?P<licenseid>[\w]+)$', admin_views.managelicense, name="managelicense"),
    url(r'^grapher/licenses/(?P<licenseid>[\w]+)/edit/$', admin_views.editlicense, name="editlicense"),
    url(r'^grapher/logos/$', admin_views.listlogos, name="listlogos"),
    url(r'^grapher/logos$', admin_views.storelogo, name="storelogo"),
    url(r'^grapher/logos/create/$', admin_views.createlogo, name="createlogo"),
    url(r'^grapher/logos/(?P<logoid>[\w]+)/$', admin_views.showlogo, name="showlogo"),
    url(r'^grapher/logos/(?P<logoid>[\w]+)/edit/$', admin_views.editlogo, name="editlogo"),
    url(r'^grapher/logos/(?P<logoid>[\w]+)$', admin_views.managelogo, name="managelogo"),
    url(r'^grapher/sources/$', admin_views.listsources, name="listsources"),
    url(r'^grapher/sources/(?P<sourceid>[\w]+)/$', admin_views.showsource, name="showsource"),
    url(r'^grapher/sources/(?P<sourceid>[\w]+)/edit/$', admin_views.editsource, name="editsource"),
    url(r'^grapher/sources/(?P<sourceid>[\w]+)$', admin_views.managesource, name="managesource"),
    url(r'^grapher/sourceTemplate/', admin_views.editsourcetemplate, name="editsourcetemplate"),
    url(r'^grapher/subcategories/(?P<subcatid>[\w]+)/edit/$', admin_views.editsubcategory, name="editsubcategory"),
    url(r'^grapher/subcategories/(?P<subcatid>[\w]+)$', admin_views.managesubcategory, name="managesubcategory"),
    url(r'^grapher/subcategories/create/$', admin_views.createsubcategory, name="createsubcategory"),
    url(r'^grapher/subcategories$', admin_views.storesubcategory, name="storesubcategory"),
    url(r'^grapher/users/$', admin_views.listusers, name="listusers"),
    # for future use on the frontend
    url(r'^grapher/charts\.json$',  admin_views.listcharts, name="listchartsjson"),
    url(r'^grapher/charts/create.json$', admin_views.createchart, name="createchartjson"),
    url(r'^grapher/charts/(?P<chartid>[\w]+)/edit\.json$', admin_views.editchart, name="editchartjson"),
    url(r'^grapher/import.json$', admin_views.importdata, name="importdatajson"),
    url(r'^grapher/users\.json$', admin_views.listusers, name="listusersjson"),

    ### Public

    url(r'^grapher/login/$', admin_views.custom_login, name='login'),
    url(r'^grapher/logout/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^grapher/config/(?P<configid>\d+)\.js$', owid_views.config, name="serveconfig"),
    url(r'^grapher/data/variables/(?P<ids>[\w\+]+)', owid_views.variables, name="servevariables"),
    url(r'^grapher/latest/?$', owid_views.latest, name="latestchart"),
    url(r'^grapher/testall', owid_views.test_all, name="testall"),
    url(r'^grapher/invite/$', admin_views.invite_user, name="inviteuser"),
    url(r'^grapher/invitation/(?P<code>[\w]+)$', admin_views.register_by_invite, name="registerbyinvite"),
    url(r'^grapher/(?P<slug>[^/]+)\.export', owid_views.show, name="exportchart"),
    url(r'^grapher/(?P<slug>[^/]+)\.(?P<fileformat>.+)', owid_views.exportfile, name="exportfile"),
    url(r'^grapher/(?P<slug>[^/]+)/?$', owid_views.show, name="showchart"),
]