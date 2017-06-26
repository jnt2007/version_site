from django.shortcuts import render, get_object_or_404

# Create your views here.
from dashboard.models import PowerMaxVersion


def index(request):

    result = PowerMaxVersion.objects.all()

    context = {
        'result': result,
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