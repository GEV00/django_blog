from django import forms
from blog_board.models import Comments
from django.core.exceptions import ValidationError
import csv


class BlogForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=15, required=True)
    text = forms.CharField(label='Содержание', max_length=1000, widget=forms.Textarea, required=True)
    images = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'multiple':True}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)

#for for csv loading
class CSVForm(forms.Form):
    file = forms.FileField(label='CSV файл')

    def clean_file(self): #название должно быть clean_*название поля*
        file = self.cleaned_data['file']
        with open(file, newline='') as f:
            csv_file = csv.DictReader(f)
            if not (csv_file['Title'] and csv_file['Text']):
                raise ValidationError(f"Неправильная структура переданного файла:",
                                      "первый столбец должен иметь название 'Title'",
                                      ", второй дожнен иметь название 'Text'.")