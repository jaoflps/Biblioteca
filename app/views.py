from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Esta linha é essencial para a tabela não aparecer vazia
        livros = Livro.objects.all()
        return render(request, 'index.html', {'livros': livros})

class DeleteLivroView(View):
    def get(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        livro.delete()
        # Esta mensagem aparecerá no topo após o redirecionamento
        messages.success(request, "Livro excluído com sucesso!")
        return redirect('index')
    
class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

    def post(self, request, *args, **kwargs):
        pass

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html', {'reservas': reservas})

from .forms import LivroForm # Importe o formulário que criamos

class EditLivroView(View):
    def get(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        form = LivroForm(instance=livro)
        return render(request, 'edit.html', {'form': form, 'livro': livro})

    def post(self, request, id):
        livro = get_object_or_404(Livro, pk=id)
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro atualizado com sucesso!")
            return redirect('index')
        return render(request, 'edit.html', {'form': form, 'livro': livro})