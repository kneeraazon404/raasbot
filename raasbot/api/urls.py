from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('add-scraped', views.add_scraped_users, name='add_scraped_user'),
    path('get-next-user', views.get_next_user, name='get_next_user'),
    path('get-init-data', views.get_init_data, name='get_init_data'),
    path('get-text', views.get_text, name='get_text'),
    path('get-tokens', views.get_tokens, name='get_token'),
    path('should-scrape', views.should_scrape, name='should_scrape'),
    path('log-result', views.log_result, name='log_result'),
    path('log-dup-result', views.log_dup_result, name='log_dup_result'),
    path('mark-dead', views.mark_dead, name='mark_dead'),
    path('add-bulk-token', views.add_bulk_token, name='add_bulk_token')
]
