from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('gramatyka_present_countinuous', TemplateView.as_view(template_name='gramar/gramatyka_present_countinuous.html'), name='gramatyka_present_countinuous'),
    path('lorem', TemplateView.as_view(template_name='gramar/lorem.html'), name='gramar_lorem'),
]
