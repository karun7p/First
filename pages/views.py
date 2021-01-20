from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Article
from blogs.forms import CreateArticleForm

# Create your views here.

def article_delete_view(request, my_id):
	if not request.user.is_authenticated:
		return redirect('login')
	
	obj = get_object_or_404(Article, id= my_id)
	if obj.author.username != request.user.username:
		return redirect ('../..')
	if request.method == "POST":
		obj.delete()
		return redirect ('../..')
	context={
		'object': obj
	}
	return render(request, 'article_delete.html', context)


def article_category_view(request, cats):
	if not request.user.is_authenticated:
		return redirect('login')
	query_set = Article.objects.filter(category= cats)
	print(query_set)
	my_list = query_set[::-1]
	context = {
		'object_list' : my_list,
		'category' : cats
	}
	return render(request, 'category.html', context)


def profile_view(request):
	if not request.user.is_authenticated:
		return redirect('login')
	print(type(request.user))
	query_set = Article.objects.filter(author =request.user)
	my_list = query_set[::-1]
	context = {
		'object_list' : my_list
	}
	return render(request, 'profile.html', context)


def article_create_view(request):
	if not request.user.is_authenticated:
		return redirect('login')
	my_form = CreateArticleForm()

	if request.method == 'POST':
		my_form = CreateArticleForm(request.POST)
		Article.objects.create(
			title=request.POST.get('title'), 
			content=request.POST.get('content'),
			category=request.POST.get('category'), 
			author=request.user )
		my_form = CreateArticleForm()		
	
	context = {
		'form' : my_form
	}
	return render(request, 'article_create.html', context)


def home_view(request, *args, **kwargs):
	if not request.user.is_authenticated:
		return redirect('login')
	
	query_set = Article.objects.all()
	my_list = query_set[::-1]
	context = {
		'object_list' : my_list
	}
	return render(request, 'home.html', context)


def article_detail_view(request, my_id):
	if not request.user.is_authenticated:
		return redirect('login')
	
	print(my_id)
	obj = Article.objects.get(id = my_id)
	context ={
		'object': obj
	}
	return render(request, 'article_detail.html', context)	






