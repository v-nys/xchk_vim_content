from django.urls import path

from . import contentviews

urlpatterns = [
    path('vim_text_editor', contentviews.VimTextEditorView.as_view(), name=f'{contentviews.VimTextEditorView.uid}_view'),
]
