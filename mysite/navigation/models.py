from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from .blocks import ExternalLinkBlock, PageLinkBlock



@register_snippet
class Navbar(models.Model):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI.
    """
    name = models.CharField(max_length=255)
    menu_items = StreamField([
        ('external_link', ExternalLinkBlock()),
        ('page_link', PageLinkBlock()),
        ],)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('menu_items')
    ]

    def __str__(self):
        return self.name


class NavbarPage(Page):
    navbar = models.ForeignKey(
        Navbar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels=[
        FieldPanel('title'),
        SnippetChooserPanel('navbar')
    ]
