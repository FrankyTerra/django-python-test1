from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	#film = forms.CharField(widget=forms.HiddenInput())
	#parent = forms.CharField(widget=forms.HiddenInput())
	class Meta:
		model = Comment
		fields = ('film', 'parent', 'author', 'text', )