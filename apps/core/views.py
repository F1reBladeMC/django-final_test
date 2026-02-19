from django.shortcuts import render
from apps.core.models import SiteInfo
# Create your views here.
def index(request):
    site_data = SiteInfo.objects.first()
    
    return render(request, 'index.html', {'site': site_data})