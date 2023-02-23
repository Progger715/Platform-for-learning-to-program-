from django.shortcuts import render, HttpResponse
from handler_code.code_form import CodeForm


def rec(request):
    # return HttpResponse('hello!')
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['input_code'])
        print("\n\n\nPOST request\n\n\n")
    else:
        form = CodeForm()
        form.result_compiling.widget(attrs={'placeholder': 'Здесь'})
        print("\n\n\nGET request\n\n\n")
    return render(request, 'handler_code/index.html', context={'form': form})


def index(request):
    return render(request, 'handler_code/index.html')
