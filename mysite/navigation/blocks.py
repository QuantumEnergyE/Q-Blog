from wagtail.core import blocks

class BaseLinkBlock(blocks.StructBlock):
    """
    Base StructBlock class used to prevent DRY code.
    """
    display_text = blocks.CharBlock()


class ExternalLinkBlock(BaseLinkBlock):
    """
    Block that holds a link to any URL.
    """
    link = blocks.URLBlock()

    class Meta:
        template = 'navigation/external_link_block.html'

class PageLinkBlock(BaseLinkBlock):
    """
    Block that holds a page.
    """
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'navigation/page_link_block.html'

class LinkChildrenBlock(blocks.StructBlock):
    """
    Base childblock for second level children.
    """
    children = blocks.StreamBlock(
            [
                ('external_link', ExternalLinkBlock()),
                ('page_link', PageLinkBlock()),
            ]
        )

class ExternalLinkWithChildrenBlock(LinkChildrenBlock, ExternalLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create an ExternalLinkBlock that supports Children.
    """
    pass

class PageLinkWithChildrenBlock(LinkChildrenBlock, PageLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create a PageLinkBlock that supports Children.
    """
    pass