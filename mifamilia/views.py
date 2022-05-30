from django.shortcuts import render
from mifamilia.models import Family

# # Create your views here.
def familia(request):
        familia = Family.objects.all()
        context = {'familia':familia}
        return render(request, 'familia_template.html', context=context)