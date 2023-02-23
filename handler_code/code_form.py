from django import forms


class CodeForm(forms.Form):
    input_code = forms.CharField(min_length=5,
                                 widget=forms.Textarea(
                                     attrs={'placeholder': 'Введите ваш код',
                                            'rows': 25,
                                            # 'cols': 60,
                                            'class': 'from-control w-1'
                                            }
                                 ))

    result_compiling = forms.CharField(min_length=5,
                                       widget=forms.Textarea(
                                           attrs={'placeholder': 'Здесь будет отображаться результат компиляции',
                                                  'rows': 25,
                                                  # 'cols': 60,
                                                  'class': 'from-control w-1'
                                                  }
                                       ))
