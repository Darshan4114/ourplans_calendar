from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import calendarHomeView

app_name = 'calendarcore'

urlpatterns = [
    path('', calendarHomeView, name="calendarHomeView"),

]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
