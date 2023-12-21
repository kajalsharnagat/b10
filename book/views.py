from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.

import logging
logger = logging.getLogger("first")

def welcome(request):
    logger.info("In Homepage view")          #django logger
    logger.info("all_books")
    books = Book.objects.all()
    return render(request, "home.html", {"all_books": books, "Model": Book})


def create_book(request):
    logger.info(request.POST)         #DJAHNGO LOGGER
    if request.method == "GET":
        return render(request, "createbook.html")
    elif request.method == "POST":

        data = request.POST
        if not data.get("id"):
            Book.objects.create(title=data.get("title"), author=data.get("auth"), 
                            publication_date=data.get("pub_date"), price=data.get("prc"), publication_name=data.get("pub_name"))
        else:
            try:
                book_obj = Book.objects.get(id=int(data.get("id")))
            except Exception as msg:
                logger.error(f"{msg}----------------in exception")    

            book_obj.title = data.get("title")
            book_obj.author = data.get("auth")
            book_obj.publication_date = data.get("pub_date")
            book_obj.price = data.get("prc")
            book_obj.save()

        return redirect("home")
    

def edit_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        return render(request, "createbook.html", {"book": book_obj})
    
def delete_book(request, bid):
    
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        if request.POST.get("type_of_delete") == "HardDelete":
            book_obj.delete()   # hard delete
        else:
            book_obj.isdeleted = True  # soft delete
            book_obj.save()
        return redirect("home")

def show_deleted_books(request):
    deleted_books = Book.objects.filter(isdeleted=True)
    return render(request, "deleted_books.html", {"deleted_books": deleted_books})


def restore_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exist")
    else:
        book_obj.isdeleted = False 
        book_obj.save()
        return redirect("home")


from book.forms import StudentForm, FileUploadForm 
from book.models import FileUpload

def index(request):  
    student = StudentForm()  # object
    return render(request,"index.html",{'student_form':student})  


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES) # name, filepath
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})


def file_list(request):
    files = FileUpload.objects.all()
    return render(request, 'file_list.html', {'all_files': files})



# status codes
# 200
# 3xx
# 500 Internal Server

