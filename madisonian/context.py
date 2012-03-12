from madisonian.models import MadSection

def mad_sections(request):
    return {'mad_sections': MadSection.objects.get_active_sections()}