from django import forms

from .models import Article,Category

choices = Category.objects.all().values_list('name','name')
#choices = [ ('tech','tech'), ('movies','movies'), ('uncategorised','uncategorised') ]

choice_list = []
for item in choices:
	choice_list.append(item)

class CreateArticleForm(forms.ModelForm):
	class Meta:
		model= Article
		fields = [
			'title',
			'content',
			'author',
			'category'
		]
		widgets = {
			'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'})
		}