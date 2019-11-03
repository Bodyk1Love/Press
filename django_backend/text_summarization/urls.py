from django.urls import path
from text_summarization.views import TextSummarizationApiView, UserApiView

app_name = "testing"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('summarize/', TextSummarizationApiView.as_view()),
    path('users/', UserApiView.as_view()),
    # path('currentUser/', current_user)
]