from users.models import Officer

def officer_processor(request):
    officers = Officer.objects.all()
    context = {
        'officers': officers,
    }
    return context
