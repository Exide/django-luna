from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Game

def index(request):
	return render_to_response('games/index.html',
		{
			'games': Game.objects.all()
		},
		context_instance=RequestContext(request))

def with_tag(request, tag_name, object_id=None, page_number=1):
	tag = get_object_or_404(Tag, name=tag_name)
	return render_to_response("forum/with_tag.html",
		{
			'tag': tag,
			'games': TaggedItem.objects.get_by_model(Game, tag).order_by('+name')
		},
		context_instance=RequestContext(request))