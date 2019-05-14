from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from thread.forms import Post_Thread, Post_answer
from django.views.generic import TemplateView
from thread.models import Post, Post_reply


class Thread(TemplateView):
    template_name = 'thread/Post.html'

    def get(self, request):
        form = Post_Thread()
        posts = Post.objects.all().order_by('-date')
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = Post_Thread(request.POST)
        posts = Post.objects.all().order_by('-date')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text ="Your Post Has Been Posted Successfully."
            form = Post_Thread()
        args = {'form': form, 'text': text, 'posts': posts}
        return render(request, self.template_name, args)


class Answer(TemplateView):
    template_name = 'thread/question_details.html'

    def get(self, request, pk):
        comment_form=Post_answer()
        post = get_object_or_404(Post, pk=pk)
        form = Post_answer()
        posts = Post_reply.objects.filter(question=post.pk).order_by('-date')
        pk = post.pk
        args = {'form': form, 'posts': posts, 'pk': pk, 'post': post,'comment_form':comment_form}
        return render(request, self.template_name, args)

    def post(self, request, pk):
        question = get_object_or_404(Post, pk=pk)
        form = Post_answer(request.POST)
        posts = Post_reply.objects.filter(question=question.pk).order_by('-date')
        if form.is_valid():
            pk = question.pk
            post = form.save(commit=False)
            post.user = request.user
            post.question = question
            post.save()
            form = Post_answer()
        args = {'form': form, 'pk': pk, 'post': question, 'posts':posts}
        return render(request, self.template_name, args)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)

def comment(request):
    reply = get_object_or_404(Post_reply, pk=request.POST.get('comment_id'))
    form = Post_answer(request.POST)
    if form.is_valid():
        pk = reply.pk
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('/Home/')
    else:
        return redirect('/Home/Profile')

