from django import forms
from blog_board.models import Comments


class BlogForm(forms.Form):
    title = forms.CharField(max_length=15, required=True)
    text = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)