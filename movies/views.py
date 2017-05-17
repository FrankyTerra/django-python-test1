from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import Comment, Film
from django.utils import timezone

from .forms import CommentForm

def index(request):
	context = {'films': Film.objects.all()}
	return render(request, 'movies/index.html', context)

def detail(request, film_id):
	form = CommentForm
	context = {	'comments': Comment.objects.filter(film = film_id),
				'film': Film.objects.get(pk=film_id),
				'form': form}
	return render(request, 'movies/detail.html', context)

def addcomment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.film = Film.objects.get(pk=int(request.POST['film']))
			if request.POST['parent'] != "":
				new_comment.parent = Comment.objects.get(pk=int(request.POST['parent']))
			else:
				new_comment.parent = None
			new_comment.author = request.POST['author']
			new_comment.text = request.POST['text']
			new_comment.pub_date = timezone.now()
			new_comment.save()

			return redirect('movies:detail', film_id = int(request.POST['film']))
		else:
			return redirect('movies:detail', film_id = int(request.POST['film']))
	else:
		form = CommentForm()

	form = CommentForm
	context = {	'comments': Comment.objects.filter(film = request.POST['film']).order_by('pk'),
				'film': Film.objects.get(pk=request.POST['film']),
				'form': form}
	return render(request, 'movies/detail.html', context)