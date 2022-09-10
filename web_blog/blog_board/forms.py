from django import forms
from blog_board.models import Comments
from django.core.exceptions import ValidationError
import csv


class BlogForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=15, required=True)
    text = forms.CharField(label='Содержание', max_length=1000, widget=forms.Textarea, required=True)
    images = forms.ImageField(label='Фото', widget=forms.ClearableFileInput(attrs={'multiple':True}), required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)

#for for csv loading
class CSVForm(forms.Form):
    file = forms.FileField(label='CSV файл')

    def clean_file(self): #название должно быть clean_*название поля*
        file = self.cleaned_data['file']
        f = file.read().decode('utf-8').strip().split('\n') #читаем csv файл, убираем лишнии пустые строки, разделяем по строкам
        csv_file = csv.reader(f, delimiter=';') #разбираем построчно по разделителю ';', т.к он в csv файле
        for raw in csv_file:
            print(raw)
            if not (raw[0] == 'Title' and raw[1] == 'Text'):
                raise ValidationError(f"Неправильная структура переданного файла:"
                                        "первый столбец должен иметь название 'Title',"
                                        " второй столбец дожнен иметь название 'Text'")
            break
       
        return csv_file #вернет в cleadned_data['file'] csv_file