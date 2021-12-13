from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from backend.forms import SalvarHistorico, HistoricoForms


@login_required()
def home(request):
    if request.method == 'POST':
        form = SalvarHistorico(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect('/api/history')

    else:
        form = HistoricoForms()

    return render(request, 'frontend/home.html', {'form': form})
