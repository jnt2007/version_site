from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.template.defaultfilters import register

from dashboard.models import PowerMaxVersion, PanelVersion


@register.filter
def in_category(things, category):
    return things.filter(panel_version=category)


def index(request):

    result = PowerMaxVersion.objects.order_by('panel_type').all()
    panel_versions = PanelVersion.objects.order_by('-version').all()

    context = {
        'result': result,
        'panel_versions': panel_versions
    }

    return render(request, 'Power_master.html', context)


def panel_version(request, version_id=None):

    version = get_object_or_404(PowerMaxVersion, id=version_id)

    result = PowerMaxVersion.objects.filter(id=version_id).all()

    context = {
        'result': result[0],
        'version': version
    }

    return render(request, 'Panel_version_details.html', context)