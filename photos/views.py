from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .models import Photo

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
    ctx = {
        'photo' : photo
    }
    return render(request,'view_photo.html',ctx)

def delete_photo(request,pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect(list_photos)
