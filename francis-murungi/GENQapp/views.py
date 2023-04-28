from django.shortcuts import render, redirect
from .forms import GENQModelsForm
from .models import GENQModels
from django.contrib import messages
# Create your views here.

#post data
def form_data(request, id =None):
    # return render(request,'form_data.html')
    if request.method == 'POST':
        if id == None:
            form = GENQModelsForm(request.POST)
        else:
            candidate = GENQModels.objects.get(pk = id)
            form = GENQModelsForm(request.POST, instance = candidate)
        if form.is_valid():
            form.save()
            messages.su
        return redirect('form_data')
    else:
        if id == None:
            form = GENQModelsForm()
        else:
            candidate = GENQModels.objects.get(pk = id)
            form = GENQModelsForm(instance = candidate)
        return render(request, 'form_data.html', {'form':form})
    
#delete
def data_delete(request, candidate_id):
    candidate = GENQModels.objects.get(id = candidate_id)
    candidate.delete()
    return redirect('/form_data')