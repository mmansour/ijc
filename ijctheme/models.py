from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

class HomePage(Page):
    headerone = RichTextField("Header One")
    headertwo = RichTextField("Header Two")
    coloneheader = RichTextField("Column One Header")
    coltwoheader = RichTextField("Column Two Header")
    colthreeheader = RichTextField("Column Three Header")
    colonetext = RichTextField("Column One Text")
    coltwotext = RichTextField("Column Two Text")
    colthreetext = RichTextField("Column Three Text")

    def can_add(self, request):
        return self.children.count() == 0

    def can_delete(self, request):
        return request.user.is_superuser or self.parent is not None

class Services(Page):
    headertext = RichTextField("Header Text")
    colonetext = RichTextField("Column One Text")
    coltwotext = RichTextField("Column Two Text")

    def can_add(self, request):
        return self.children.count() == 0

    def can_delete(self, request):
        return request.user.is_superuser or self.parent is not None

class About(Page):
    headertext = RichTextField("Header Text")
#    subheadertext = RichTextField("Sub Header Text")
    bodytext = RichTextField("Body Text")

    def can_add(self, request):
        return self.children.count() == 0

    def can_delete(self, request):
        return request.user.is_superuser or self.parent is not None
