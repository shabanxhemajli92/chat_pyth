from django.shortcuts import render,redirect
from .forms import InputForm, ResultForm
import os
import openai
import ratelimit


api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key
@ratelimit.limits(calls=1, period=1)
def get_response_from_api(prompt, max_tokens):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="what test",
        max_tokens=1
    )
    return response["choices"][0]["text"]

def test_hub(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            result_text = get_response_from_api(input_text, 1)
            return redirect('result', result_text=result_text)
    else:
        form = InputForm()
    return render(request, 'easytest/test_hub.html', {'form': form})

def result(request, result_text):
    result_form = ResultForm(initial={'result_text': result_text})
    return render(request, 'easytest/result.html', {'result_form': result_form})

def result_render(request):
    return render(request,"easytest/result.html")    