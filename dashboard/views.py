from django.shortcuts import render


# Create your views here.
from dashboard.models import PowerMaxVersion


def index(request):

    result = PowerMaxVersion.objects.all()

    context = {
        'result': result,
    }

    return render(request, 'index.html', context)
