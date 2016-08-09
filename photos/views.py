from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model


from .models import Photo
from .models import Comment
from .models import Like

from .forms import PhotoForm

User = get_user_model()

def list_photos(request):
    photos = Photo.objects.all().order_by('-created_at')

    ctx = {
        'photos':photos,

    }
    return render(request,'list_photos.html', ctx)

class PhotoCreate(CreateView):
    model = Photo
    fields = ('image', 'description',)
    template_name = 'create_photo.html'

    def form_valid(self,form):
        new_photo = form.save(commit = False)
        new_photo.user = self.request.user
        new_photo.save()
        return super(PhotoCreate, self).form_valid(form)


'''def create_photo(request):
    if request.method == "GET":
        form = PhotoForm()
        ctx = {
            'form' : form
        }
        return render(request, 'create_photo.html', ctx)

    form = PhotoForm(data = request.POST)
    if form.is_valid() is True:
        new_photo = form.save(commit = False)
        new_photo.user = request.user
        new_photo.save()
        url = reverse('photos:view_photo', kwargs={'pk': new_photo.pk})
        return redirect(url)
'''

def view_photo(request,pk):
    photo = Photo.objects.get(pk=pk)
    comments = Comment.objects.filter(photo = photo)
    ctx = {
        'photo' : photo,
        'comments' : comments,
    }
    return render(request,'view_photo.html',ctx)

def delete_photo(request,pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('photos:list_photos')

def create_comment(request,pk):
    photo = Photo.objects.get(pk=pk)
    content = request.POST.get('content')

    new_comment = Comment()
    new_comment.user = request.user
    new_comment.photo = photo
    new_comment.content = content
    new_comment.save()

    url = reverse('photos:list_photos', )
    return redirect(url)

def delete_comment(request,pk):
    comment = Comment.objects.get(pk=pk)
    photo_pk = comment.photo_id
    comment.delete()

    url = reverse('photos:view_photo', kwargs={'pk': photo_pk})
    return redirect(url)

def my_handler404(request):

    return render(request,'404.html', status=404)

def click_like(request,pk,status):
    photo = Photo.objects.get(pk=pk)
    if status == 'true':
        new_like = Like()
        new_like.photo = photo
        new_like.user = request.user
        new_like.save()

    else:
        like = Like.objects.get(photo=photo, user=request.user)
        like.delete()


    url = reverse('photos:list_photos', )
    return redirect(url)

def view_userpage(request,username):
    user = User.objects.get(username=username)
    my_photos = Photo.objects.filter(user= user).order_by('-created_at')

    ctx = {
        'user':user,
        'photos':my_photos,
    }
    return render(request,'view_userpage.html', ctx)
