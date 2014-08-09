#coding:utf-8
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from zhyblog.models import Blog

#request用户传的数据response返回给用户的数据
#CRUD增查改删

def blog_create(request):
	print request.POST
	if request.method == "POST":
		t = request.POST['a']
		s = request.POST['b']
		Blog(title=t,content=s).save()
	return redirect("/list")

def blog_list(request):
	blogs = Blog.objects.filter().order_by('-id')
	d = {'blogs':blogs}
	return render_to_response('list.html', d, context_instance=RequestContext(request))

def blog_update(request,id):
	b = Blog.objects.get(id=int(id))
	d = {'b':b}
	return render_to_response('update.html', d, context_instance=RequestContext(request))

def blog_update_save(request,id):
	b = Blog.objects.get(id=int(id))
	b.title = request.POST['a']
	b.save()
	return redirect("/list")

def blog_delete(request,id):
	Blog.objects.get(id=int(id)).delete()
	return redirect("/list")

def bl(request):
	blogs = Blog.objects.filter().order_by('-id')
	d = {'blogs':blogs}
	return render_to_response('bl.html', d, context_instance=RequestContext(request))

def test(request,w):
		d = {'name':w,'a':10}
		return render_to_response('test.html', d)
