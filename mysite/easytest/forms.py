from django import forms

class InputForm(forms.Form):
    input_text = forms.CharField(label='Enter your text', max_length=1000)

class ResultForm(forms.Form):
    result_text = forms.CharField(label='Result', max_length=1000, widget=forms.Textarea)
