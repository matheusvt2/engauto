from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from . import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()


schema_view = get_swagger_view(title='Project Name')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('run/', views.Insert_run.as_view()),
    path('history/', views.History.as_view()),
    path('docs/', get_schema_view(title='API',
                                description='Documentação da API'), 
                                name='openapi'),
    path('docs/swagger/', TemplateView.as_view(
                                template_name='documentation.html',
                                extra_context={'schema_url':'openapi'}),
                                name='swagger-ui'),
]