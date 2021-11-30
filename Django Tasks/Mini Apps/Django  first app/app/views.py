from django.shortcuts import render

# Create your views here.

def app(request):
    return render(request,'index.html')

blogs=[
        {
            'id' : 1,
            'ad' : 'Blog1',
            'txt' : 'lorem ipsom dolor sit'
        },
          {
            'id' : 2,
            'ad' : 'Blog2',
            'txt' : 'salam '
        }
    ]

def blog(request):
    context={'blogs' : blogs }
    return render(request,'blog.html',context)

def detail(request, id):
   blog1=blogs[0]['id']
   blog2=blogs[1]['id']
   context={
   'blog1' :blog1, 
   'blog2': blog2 
   }
   return render(request,'detail.html',context)


