from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import MemberForm
from .models import Member


class MemberListView(ListView):
    model = Member
    context_object_name = "members"
    paginate_by = 5

    def get_queryset(self):
        search_query = self.request.GET.get("search", "").strip()
        if search_query:
            return Member.objects.filter(
                Q(first_name__icontains=search_query)
                | Q(last_name__icontains=search_query)
                | Q(email__icontains=search_query)
                | Q(phone_number__icontains=search_query)
            ).distinct()

        return Member.objects.all()


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy("member-list")


class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberForm
    success_url = reverse_lazy("member-list")


class MemberDeleteView(DeleteView):
    model = Member
    context_object_name = "member"
    success_url = reverse_lazy("member-list")
