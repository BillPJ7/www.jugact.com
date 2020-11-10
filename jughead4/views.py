from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.urls import reverse
from .models import Post
'''
Attention Azavea people! Before looking at this, take a look
at the Specs document (my writing sample), which is the specs for this app.
'''
routine = []
routine.append('3 balls + can')
routine.append('3 balls')
routine.append('3 balls + club')
routine.append('4 balls part 1')
routine.append('4 balls part 2')
routine.append('5 balls reverse cascade')
routine.append('5 balls left/right half shower')
routine.append('5 balls 3 left 2 right, 3 right 2 left')
routine.append('5 catch 1 on foot (keep 4 going)')
routine.append('4 balls kick into 5 (stylish kick)')
routine.append('5 ball shower') 
 
def index(request):
    if request.method == "POST": #Entry already submitted
        '''
        If you try to submit after locked, get directed to nicetry.html.
        Otherwise your entries are posted. If these are the actual results,
        then do GetWinners. Get directed to confirm.html
        '''
        is_locked = False
        if request.POST['Name'] != 'xyzgo': #only if not submitting result
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
            if request.POST['Name'] == 'xyzgo': #results being submitted
                GetWinners(my_post)
            context = {'my_post': my_post, "routines":routine}
            return render(request, 'jughead4/confirm.html', context) #displays my guesses
    else: #Just launched
        if Post.objects.filter(name='noact'):
            return render(request, 'jughead4/noact.html')
        else:
            return render(request, 'jughead4/index.html', {"routines":routine}) #displays boxes with +, - buttons so you don't have to type numbers
    
def result(request, post_id):
    '''
    Result link was clicked on confirm.html. Get directed to result.html,
    unless results haven't been posted, then get directed back to confirm.html
    '''
    my_post = Post.objects.filter(pk=post_id)
    if Post.objects.filter(name='xyzgo'): #results were posted
        #my_post = Post.objects.filter(pk=post_id)
        win_post = Post.objects.filter(winner=True)
        context = {'my_post': my_post, 'win_post': win_post, 'post_actual': post_actual}
        return render(request, 'jughead4/result.html', context) #displays my guesses, winning guesses and actual results
    else: #no results yet
        #my_post = Post.objects.filter(pk=post_id)
        context = {'my_post': my_post}
        return render(request, 'jughead4/confirm.html', context) #displays my guesses

def GetWinners(post_actual):
    #loop thru result record and get each routine drops
    for pa in post_actual: 
        #To do: maybe use an array here so there's just one line.
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
    low = 99 #lowest score is best so start high so first entry will be the new best
    #loop thru the participant records and compare to results
    for p in Post.objects.exclude(name='xyzgo').exclude(name='xyzlock').exclude(name='noact'): #only the participants 
        #To do: maybe use an array here so there's just one line.
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
        #add up all the differences between guesses and results to determine score (lowest is best)
        new = abs(pa1-r1)+abs(pa2-r2)+abs(pa3-r3)+abs(pa4-r4)+abs(pa5-r5)+abs(pa6-r6)+abs(pa7-r7)+abs(pa8-r8)+abs(pa9-r9)+abs(pa10-r10)+abs(pa11-r11)
        Post.objects.filter(pk=p.pk).update(score=new)
        if new < low: #check for new low... sorry
            low = new
    for p in Post.objects.exclude(name='xyzgo').exclude(name='xyzlock').exclede(name='noact'): #only the participants
        if p.score == low: #we got a winner
            Post.objects.filter(pk=p.pk).update(winner=True)
        
