from django.shortcuts import render, HttpResponse
from rest_framework import generics

from handler_code.code_form import CodeForm
from handler_code.collector_code import get_html_result_compiling


def rec(request):
    # return HttpResponse('hello!')
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data['input_code'])
            data_received = form.cleaned_data['input_code']
            data, flag_errors, line_error = get_html_result_compiling(data_received)
            if flag_errors:
                form.highlight_line_with_error(data_received, line_error)
        # print("\n\n\nPOST request\n\n\n")
    else:
        form = CodeForm()
        # form.highlight_line_with_error("sds", "sdsd")
        # form.fields['input_code'].initial = 'New value'
        data = "<-Введите код в обасть для ввода кода"
        # print("\n\n\nGET request\n\n\n")
    return render(request, 'handler_code/index.html', context={'form': form, 'data_from_server': data})


def index(request):
    return render(request, 'handler_code/index.html')
