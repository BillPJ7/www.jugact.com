from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Post

def index(request):
    #foo_instance = Foo.objects.create(name='test')
   #return render(request, 'some_name.html.html')
    if request.method == "POST":
        is_locked = False
        if request.POST['Name'] != 'xyzgo':
            is_locked = Post.objects.filter(name='xyzlock')
        if is_locked:
            return render(request, 'jughead4/nicetry.html')
        else:
            post_instance = Post.objects.create(name = request.POST['Name'], 
            R1 = request.POST['R1'], R2 = request.POST['R2'], 
            R3 = request.POST['R3'], R4 = request.POST['R4'],
            R5 = request.POST['R5'], R6 = request.POST['R6'], 
            R7 = request.POST['R7'], R8 = request.POST['R8'],
            R9 = request.POST['R9'], R10 = request.POST['R10'], 
            R11 = request.POST['R11'])
            my_post = Post.objects.filter(pk=post_instance.pk)
            if request.POST['Name'] == 'xyzgo':
                GetWinners(my_post)
            context = {'my_post': my_post}
            return render(request, 'jughead4/confirm.html', context)
        #my_post = get_object_or_404(Post, pk=post_instance.pk)
       # post_instance = get_object_or_404(Post, pk=post_instance.pk)
        #return render(request, 'jughead4/confirm.html', {'post_instance': post_instance})
    else:
        return render(request, 'jughead4/index.html')
    
def result(request, post_id):
    #if request.method == "POST":
        post_actual = Post.objects.filter(name='xyzgo')
        if post_actual:
            
            my_post = Post.objects.filter(pk=post_id)
            win_post = Post.objects.filter(winner=True)
            #win_post = winner(post_actual)
           # win_post = Post.objects.filter(pk=i)
           # return render(request, 'jughead4/result.html', {'my_post': my_post, 'post_actual': post_actual})
            context = {'my_post': my_post, 'win_post': win_post, 'post_actual': post_actual}
            return render(request, 'jughead4/result.html', context)
            #find winner display results
        else:
            my_post = Post.objects.filter(pk=post_id)
            context = {'my_post': my_post}
            return render(request, 'jughead4/confirm.html', context)
            #post_instance = get_object_or_404(Post, pk=post_id)
            #post_instance = Post.objects.filter(id=44)
            #return HttpResponseRedirect(reverse('jughead4:confirm'))
            #return render(request, 'jughead4/confirm.html', {'post_instance': post_instance})
        #context = {'post_actual': post_actual}
        #return render(request, 'jughead4/')
    #else:
        #return render(request, 'jughead4/result.html')
def GetWinners(post_actual):
    for pa in post_actual:
        pa1 = pa.R1
        pa2 = pa.R2
        pa3 = pa.R3
        pa4 = pa.R4
        pa5 = pa.R5
        pa6 = pa.R6
        pa7 = pa.R7
        pa8 = pa.R8
        pa9 = pa.R9
        pa10 = pa.R10
        pa11 = pa.R11
    high = 100
    for p in Post.objects.exclude(name='xyzgo').exclude(name='xyzlock'):
        r1 = p.R1
        r2 = p.R2
        r3 = p.R3
        r4 = p.R4
        r5 = p.R5
        r6 = p.R6
        r7 = p.R7
        r8 = p.R8
        r9 = p.R9
        r10 = p.R10
        r11 = p.R11
        new = abs(pa1-r1)+abs(pa2-r2)+abs(pa3-r3)+abs(pa4-r4)+abs(pa5-r5)+abs(pa6-r6)+abs(pa7-r7)+abs(pa8-r8)+abs(pa9-r9)+abs(pa10-r10)+abs(pa11-r11)
        Post.objects.filter(pk=p.pk).update(score=new)
        if new < high:
            high = new
            id = p.pk#Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
    for p in Post.objects.exclude(name='xyzgo').exclude(name='xyzlock'):
        if p.score == high:
            Post.objects.filter(pk=p.pk).update(winner=True)
        
