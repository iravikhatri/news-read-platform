from django import forms
from .models import News

inputClass = """w-full py-2 px-4 mb-1 bg-gray-300 text-gray-700 leading-tight rounded border-2
    border-gray-300 appearance-none focus:outline-none focus:bg-white focus:border-indigo-700"""

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'image_url']

        widgets = {
            'title': forms.TextInput(attrs={'class' : inputClass}),
            'content': forms.Textarea(attrs={'class' : inputClass}),
            'image_url': forms.TextInput(attrs={'class' : inputClass}),
        }
