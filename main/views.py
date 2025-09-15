from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import *


def hello_view(request):
    return HttpResponse(
        """
        <h1>Hello, world from django views!</h1>
        <hr>
        <p>Bugun darsimizda MVT strukturasini o'tmoqdamiz</p>
        """
    )


def home_view(request):
    return render(request, 'home.html')


def students_view(request):
    if request.method == 'POST':
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else 0
        )
        return redirect('/students/')


    students = Talaba.objects.all()

    search = request.GET.get('search')
    if search:
        students = students.filter(ism__contains=search)

    ordering = request.GET.get('ordering')
    if ordering:
        students = students.order_by(ordering)

    kurs = request.GET.get('kurs')
    if kurs:
        students = students.filter(kurs=kurs)

    context = {
        'students': students,
        'search': search,
        'ordering': ordering,
        'kurs': kurs,
    }
    return render(request, 'students.html', context)


def bitiruvchi_talabalar(request):
    students = Talaba.objects.filter(kurs=4)
    context = {
        'students': students,
    }
    return render(request, 'bitiruvchi-talabalar.html', context)


# retrieve
def student_details_view(request, student_id):
    student = Talaba.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'student-details.html', context)


def authors_view(request):
    authors = Muallif.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'authors.html', context)


def author_details_view(request, author_id):
    author = Muallif.objects.get(id=author_id)
    context = {
        'author': author,
    }
    return render(request, 'author-details.html', context)


def book_details_view(request, book_id):
    book = Kitob.objects.get(id=book_id)
    context = {
        "book": book,
    }
    return render(request, 'book-details.html', context)


def student_delete_view(request, pk):
    student = get_object_or_404(Talaba, pk=pk)
    student.delete()
    return redirect('/students/')


def books_view(request):
    if request.method == 'POST':
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=get_object_or_404(Muallif, id=request.POST.get('muallif_id'))
        )
        return redirect('/books/')
    books = Kitob.objects.all()
    authors = Muallif.objects.all()

    search = request.GET.get('search')
    if search:
        books = books.filter(
            Q(nom__contains=search) |
            Q(muallif__ism__contains=search)
        )

    muallif_id = request.GET.get('muallif_id')
    if muallif_id:
        books = books.filter(muallif__id=muallif_id)

    context = {
        'books': books,
        'authors': authors,
        'search': search,
        'muallif_id': int(muallif_id) if muallif_id else 0,
    }
    return render(request, 'books.html', context)


def book_delete_confirm_view(request, pk):
    book = get_object_or_404(Kitob, pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book-confirm-delete.html', context)


def book_delete_view(request, pk):
    book = get_object_or_404(Kitob, pk=pk)
    book.delete()
    return redirect('/books/')
