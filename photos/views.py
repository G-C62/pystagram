from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from .models import Photo
from .models import Comment

def list_photos(request):
    photos = Photo.objects.all().order_by('-created_at')
    ctx = {
        'photos':photos
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
    new_comment.photo = photo
    new_comment.content = content
    new_comment.save()

    url = reverse('photos:view_photo', kwargs={'pk': photo.pk})
    return redirect(url)

def delete_comment(request,pk):
    comment = Comment.objects.get(pk=pk)
    photo_pk = comment.photo_id
    comment.delete()

    url = reverse('photos:view_photo', kwargs={'pk': photo_pk})
    return redirect(url)
