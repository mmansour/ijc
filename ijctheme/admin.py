from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from models import HomePage, Services, About

#ABOUT ADMIN
about_extra_fieldsets = ((None, {"fields": ("headertext", "bodytext",)}),)
class AboutAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + about_extra_fieldsets

#HOMEPAGE ADMIN
homepage_extra_fieldsets = ((None, {"fields": ("headerone","headertwo",
                                               "coloneheader", "coltwoheader",
                                               "colthreeheader","colonetext",
                                               "coltwotext", "colthreetext",)}),)
class HomePageAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + homepage_extra_fieldsets

#SERVICES ADMIN
services_extra_fieldsets = ((None, {"fields": ("headertext","colonetext", "coltwotext",)}),)
class ServicesAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + services_extra_fieldsets

admin.site.register(About, AboutAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Services, ServicesAdmin)

  