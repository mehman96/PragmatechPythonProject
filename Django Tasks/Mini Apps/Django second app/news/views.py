from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request,'index.html')

news=[
        {
            'id' : 1,
            'ad' : 'xeber1',
            'txt' : 'lorem ipsom dolor sit'
            
        },
          {
            'id' : 2,
            'ad' : 'xeber2',
            'txt' : 'lorem ipsom dolor '
         
        }
    ]





def add(request):
    context={'news' : news }
    return render(request, 'add.html',context)    



def show (request,id):
   news1=news[0]['id']
   news2=news[1]['id']
   context={
   'news1' :news1, 
   'news2': news2,
   }
   return render(request, 'show.html',context)    