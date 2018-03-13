from django.db import models

from wagtail.core.models import Page
from blog.models import BlogNavigation


class HomePage(Page):
    def get_context(self, request):

        # Filter by tag
        blog_navigation = BlogNavigation.objects.first()

        # Update template context
        context = super().get_context(request)
        # Blog's Navigation
        context['blog_navigation'] = blog_navigation
        return context
