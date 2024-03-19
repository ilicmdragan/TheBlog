from django import forms
from .models import Post, Category

# STATIC hard codded dropdown list of Category
#choices = [('Coding','Coding'), ('Sports', 'Sports') , ('Entertainment','Entertainment'),] - hard codded dropdown list of Category

# dynamic codded dropdown list of Category
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

#PostForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category','body','snippet','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            #'header_image': forms.Textarea(attrs={'class':'form_control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category','body', 'snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),

        }