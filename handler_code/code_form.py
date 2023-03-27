from django import forms


class CodeForm(forms.Form):
    input_code = forms.CharField(min_length=5,
                                 widget=forms.Textarea(
                                     attrs={'placeholder': 'Введите ваш код',
                                            'rows': 25,
                                            'cols': 100,
                                            'class': 'from-control w-1'
                                            }
                                 ))

    def highlight_line_with_error(self, source_code: str, line_error: str):
        source_code = source_code.replace(line_error,
                                          f'<span style="color: red;">{line_error}</span>')
        self.fields['input_code'].initial = 'Hello <span style="color: blue;">world</span>!'  # поменять на строку выше
        # self.fields['input_code'].initial = 'New value'
        # 'System.out.println("hello!");\n <span style="color: red;">int i = "stora";</span>'
