"""
URL configuration for compra_ahorra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from compra_ahorra.views import view_index
from compra_ahorra.views import view_region
from compra_ahorra.views import view_login
from compra_ahorra.views import view_home
from compra_ahorra.views import view_fomsdata
from compra_ahorra.views import view_historial
from compra_ahorra.views import view_moda
from compra_ahorra.views import view_tecnologia
from compra_ahorra.views import view_electrodomestico
from compra_ahorra.views import view_ofertas
from compra_ahorra.views import transbankpay
from compra_ahorra.views.home_view import cart
from compra_ahorra.views import view_home2

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

admin.site.register(ContentType)
admin.site.register(Permission)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', view_index.index),
    path('home2/', cart),
    path('', view_index.index),
    path('region/', view_region.region),
    path('login/', view_login.login),
    path('home/', view_home.home),
    path('update-secret', view_login.update_pass),
    path('forms-data/', view_fomsdata.formsdata),
    path('forms-data-guardar/', view_fomsdata.guardar),
    path('historial/', view_historial.historial),
    path('moda/', view_moda.moda),
    path('tecnologia/', view_tecnologia.tecnologia),
    path('electrodomestico/', view_electrodomestico.electrodomestico),
    path('ofertas/', view_ofertas.ofertas),
    path('logout', view_login.logout),
    path('webpay-plus-create', transbankpay.webpay_plus_create),
    path('commit-pay/', transbankpay.commitpay),
    path('home2/', view_home2.home2),
]
