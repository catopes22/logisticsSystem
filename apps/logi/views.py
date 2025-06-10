from django.views.generic import ListView, DetailView
from .models import Route, Category
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from ..services.mixins import AuthorRequiredMixin
from .forms import RouteCreateForm, RouteUpdateForm


class RouteListView(ListView):
    model = Route
    template_name = 'logi/route_list.html'
    context_object_name = 'routes'
    paginate_by = 2
    queryset = Route.custom.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class RouteDetailView(DetailView):
    model = Route
    template_name = 'logi/route_detail.html'
    context_object_name = 'route'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class RouteFromCategory(ListView):
    model = Route
    template_name = 'logi/route_list.html'
    context_object_name = 'routes'
    category = None
    paginate_by = 1
    queryset = Route.custom.all()

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Route.objects.filter(category__slug=self.category.slug)
        if not queryset:
            sub_cat = Category.objects.filter(parent=self.category)
            queryset = Route.objects.filter(category__in=sub_cat)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Записи из категории: {self.category.title}'
        return context


class RouteCreateView(LoginRequiredMixin, CreateView):
    """
    Представление: создание материалов на сайте
    """
    model = Route
    template_name = 'logi/route_create.html'
    form_class = RouteCreateForm
    login_url = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление маршрута на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class RouteUpdateView(AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Представление: обновления материала на сайте
    """
    model = Route
    template_name = 'logi/route_update.html'
    context_object_name = 'route'
    form_class = RouteUpdateForm
    login_url = 'home'
    success_message = 'Запись была успешно обновлена!'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Обновление маршрута: {self.object.title}'
        return context

    def form_valid(self, form):
        # form.instance.updater = self.request.user
        form.save()
        return super().form_valid(form)
