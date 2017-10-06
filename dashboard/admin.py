from django.contrib import admin

from dashboard.models import PowerMaxVersion, KP250Version, PlinkVersion, PanelVersion, IPMPVersion


# Register your models here.
class PowerMaxVersionAdmin(admin.ModelAdmin):
    pass


class KP250VersionAdmin(admin.ModelAdmin):
    pass


class PlinkVersionAdmin(admin.ModelAdmin):
    pass


class PanelVersionAdmin(admin.ModelAdmin):
    pass


class IPMPVersionAdmin(admin.ModelAdmin):
    pass


admin.site.register(PowerMaxVersion, PowerMaxVersionAdmin)
admin.site.register(KP250Version, KP250VersionAdmin)
admin.site.register(PlinkVersion, PlinkVersionAdmin)
admin.site.register(PanelVersion, PanelVersionAdmin)
admin.site.register(IPMPVersion, IPMPVersionAdmin)
