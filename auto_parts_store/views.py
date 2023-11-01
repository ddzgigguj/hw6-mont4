from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic

class AvtopartsListView(generic.ListView):
    template_name = 'avto_parts/avtoparts_list.html'
    queryset = models.AutoParts.objects.all()

    def get_queryset(self):
        return models.AutoParts.objects.all()

# def avtopartsListView(request):
#     avtoparts = models.AutoParts.objects.all()
#     html_name = 'avto_parts/avtoparts_list.html'
#     context = {
#         'avtoparts_key': avtoparts,
#     }
#     return render(request, html_name, context)

class AvtopartsDetailView(generic.DetailView):
    template_name = 'avto_parts/avtoparts_detail.html'

    def get_object(self, **kwargs):
        avtoparts_id = self.kwargs.get('id')
        return get_object_or_404(models.AutoParts, id=avtoparts_id)

# def avtopartsDetailView(request, id):
#     avtoparts_id = get_object_or_404(models.AutoParts, id=id)
#     html_name = 'avto_parts/avtoparts_detail.html'
#     context = {
#         'avtoparts_id': avtoparts_id,
#     }
#     return render(request, html_name, context)

class CreateProductsView(generic.CreateView):
    template_name = 'avto_parts/create_product.html'
    form_class = forms.ProductForm
    queryset = models.AutoParts.objects.all()
    success_url = '/avtoparts_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductsView, self).form_valid(form=form)

# def createProductsView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Товар успешно добавлен')
#     else:
#         form = forms.ProductForm()
#
#     return render(request, 'avto_parts/create_product.html', {'form': form})

class DeleteProductsView(generic.DeleteView):
    template_name = 'avto_parts/confirm_delete.html'
    success_url = '/avtoparts_list/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.AutoParts, id=product_id)

# def deleteProductsView(request, id):
#     product_id = get_object_or_404(models.AutoParts, id=id)
#     product_id.delete()
#     return HttpResponse('Товар успешно удалён')

class UpdateProductsView(generic.UpdateView):
    template_name = 'avto_parts/update_product.html'
    form_class = forms.ProductForm
    success_url = '/avtoparts_list/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.AutoParts, id=product_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateProductsView, self).form_valid(form=form)

# def updateProductsView(request, id):
#     product_id = get_object_or_404(models.AutoParts, id=id)
#     if request.method == 'POST':
#         form = forms.ProductForm(instance=product_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Товар изменён')
#
#     else:
#         form = forms.ProductForm(instance=product_id)
#     return render(request, 'avto_parts/update_product.html',
#                   {
#                       'form': form,
#                       'product_id': product_id
#                   }
#                   )

class Search(generic.ListView):
    template_name = 'avto_parts/avtoparts_list.html'
    context_object_name = 'product'
    paginate_by = 5

    def get_queryset(self):
        return models.AutoParts.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class FormCommentView(generic.CreateView):
    template_name = 'avto_parts/review_form.html'
    form_class = forms.ReviewForm
    queryset = models.ReviewProducts.objects.all()
    success_url = '/avtoparts_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(FormCommentView, self).form_valid(form=form)