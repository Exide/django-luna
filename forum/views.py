from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from models import Topic, Post
from forms import TopicForm, PostForm
from tagging.models import Tag, TaggedItem

import logging

def index(request):
    tags = Tag.objects.usage_for_model(Topic, counts=True)
    return render_to_response('forum/index.html',
        {
            'recent_topics': Topic.objects.order_by('-updated_at'),
            'recent_tags': sorted(tags, key=lambda x: x.count, reverse=True)
        },
        context_instance=RequestContext(request))

def show(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    posts = Post.objects.filter(topic=topic)
    return render_to_response('forum/show.html',
        {
            'topic': topic,
            'posts': posts
        },
        context_instance=RequestContext(request))

def with_tag(request, tag_name, object_id=None, page_number=1):
    tag = get_object_or_404(Tag, name=tag_name)
    return render_to_response("forum/with_tag.html",
        {
            'tag': tag,
            'topics': TaggedItem.objects.get_by_model(Topic, tag).order_by('-created_at'),
        },
        context_instance=RequestContext(request))

@login_required
def new(request):
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        post_form = PostForm(request.POST)
        
        if topic_form.is_valid() and post_form.is_valid():
            topic = topic_form.save()
            post = post_form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('/forum/%d' % topic.id)
    else:
        topic_form = TopicForm()
        post_form = PostForm()
    
    return render_to_response('forum/new.html',
        {
            'topic_form': topic_form,
            'post_form': post_form
        },
        context_instance=RequestContext(request))

@login_required
def edit(request, topic_id, post_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('/forum/%d' % topic.id)
    else:
        form = PostForm(instance=post)
    return render_to_response('forum/edit.html',
        {
            'topic': topic,
            'post': post,
            'form': form,
        },
        context_instance=RequestContext(request))

@login_required
def reply(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            topic.updated_at = post.updated_at
            topic.save()
            return redirect('/forum/%d' % topic.id)
    else:
        form = PostForm()
    return render_to_response('forum/reply.html',
        {
            'topic': topic,
            'form': form,
        },
        context_instance=RequestContext(request))

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    posts = Post.objects.filter(topic=topic)
    for post in posts:
        post.delete()
    topic.delete()
    return redirect('/forum')

@login_required
def delete_post(request, topic_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/forum/%s' % topic_id)