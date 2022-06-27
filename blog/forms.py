from django import forms
from .models import Post, Category, Comment

cat_queryset = Category.objects.values_list('name', 'name')
cat_list = [cat for cat in cat_queryset]

class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'header_image_url', 'category', 'body', 'tag']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_list, attrs={'class': 'form-control'}),
            'header_image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'tag': 'separate tags with commas(tag1,tag2,tag3....)',
        }
       



class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'header_image_url', 'category', 'body', 'tag']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cat_list, attrs={'class': 'form-control'}),
            'header_image_url': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'tag': 'separate tags with commas(tag1,tag2,tag3....)',
        }
        




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
