from django.contrib import admin

from dashboard.models import PowerMaxVersion, KP250Version, PlinkVersion, PanelVersion


# Register your models here.
class PowerMaxVersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PowerMaxVersion, PowerMaxVersionAdmin)


class KP250VersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(KP250Version, KP250VersionAdmin)


class PlinkVersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlinkVersion, PlinkVersionAdmin)


class PanelVersionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PanelVersion, PanelVersionAdmin)