from django import forms
from .models import News, Category


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class NewsForm_WithOutModel(forms.Form):
    title = forms.CharField(max_length=150, label='Наименование',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    is_published = forms.BooleanField(label='Опубликовать?', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, label='Категория',
                                      empty_label=None)
