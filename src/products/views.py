from django.contrib import messages
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView 
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone

from .forms import  VariationInventoryFormSet
from .models import Product, Variation, Category
from .mixins import StaffRequiredMixin, LoginRequiredMixin
# Create your views here.
import random
class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "products/product_list.html"

class CategoryDetailView(DetailView):
	model = Category

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		#print(obj)
		product_set = obj.product_set.all()
		#print(product_set)
		default_products = obj.default_category.all()
		#print(default_products)
		products = (product_set | default_products).distinct()
		context['products'] = products
		return context 




class VariationListView(StaffRequiredMixin,ListView):
	model = Variation
	queryset = Variation.objects.all()
	#print(queryset)
	#queryset = Product.objects.all().active()
	#queryset = Product.objects.filter(activo=False)

	def get_context_data(self, *args, **kwargs):
		context = super(VariationListView, self).get_context_data(*args, **kwargs)
		context['formset'] = VariationInventoryFormSet(queryset=self.get_queryset())
		return context

	def get_queryset(self, *args, **kwargs):
		product_pk = self.kwargs.get("pk")
		#print(product_pk)
		if product_pk:
			product = get_object_or_404(Product, pk=product_pk)
			queryset = Variation.objects.filter(product = product)
		return queryset

	def post(self, request, *args, **kwargs):
		formset = VariationInventoryFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				new_item = form.save(commit = False)
				if new_item.title:
					product_pk = self.kwargs.get("pk")
					product = get_object_or_404(Product, pk=product_pk)
					new_item.product = product
					new_item.save()

				
			
			messages.success(request,"Su Inventario y Precios han sido actualizados")
			return redirect("products")

		raise Http404




class ProductListView(ListView):
	model = Product
	queryset = Product.objects.all()
	#queryset = Product.objects.all().active()
	#queryset = Product.objects.filter(activo=False)

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context['now'] = timezone.now()
		context['query'] = self.request.GET.get("q")
		return context

    # función para implementar la busqueda en la página 
	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(title__icontains = query) |
				Q(description__icontains = query) #|
				#Q(precio = query)
				)
			try:
				qs2 = self.model.objects.filter(
				     Q(precio = query)	
				)
				qs = (qs | qs2).distinct()
			except:
				pass
		return qs


class ProductDetailView(DetailView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		#order_by("-title")
		#context["related"] = sorted (Product.objects.get_related(instance)[:6], key = lambda x: x.title, reverse=True)
		context["related"] = sorted (Product.objects.get_related(instance)[:6], key = lambda x: random.random())
		print(context["related"])
		return context

def product_detail(request, id):
	#product_instance = Product.objects.get(pk=id)
	try:
		product_instance = get_object_or_404(Product, pk=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404

	template = "product/product_detail.html"
	context = {
	    "object": product_instance,
	}

	return render(request, template, context)

def imprimir(request):
	template = "imprimir.html"
	return render(request, template, {})


