# Imports from Django.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView


# Imports from assignment-desk.
from assignment_desk.forms import InlineAssignmentFormset
from assignment_desk.forms import WeekCreationForm
from assignment_desk.forms import WeekEditingForm
from assignment_desk.mixins import InlineFormsetMixin
from assignment_desk.models import Assignment
from assignment_desk.models import Role
from assignment_desk.models import Week


DAYS_IN_WEEK = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]


def index_view(request):
    return HttpResponse('Hello, world. You\'re at the assignment-desk index.')


class WeekListView(LoginRequiredMixin, ListView):
    queryset = Week.objects.all()
    template_name = 'assignment_desk/weeks/list.html'


class WeekCreateView(LoginRequiredMixin, CreateView):
    model = Week
    form_class = WeekCreationForm
    template_name = 'assignment_desk/weeks/create_form.html'


class WeekEditView(LoginRequiredMixin, InlineFormsetMixin, UpdateView):
    model = Week
    template_name = 'assignment_desk/weeks/edit_form.html'

    form_class = WeekEditingForm
    inline_formset_class = InlineAssignmentFormset

    def get_queryset(self):
        return Week.objects.prefetch_related(
            'assignments',
            'assignments__staffer',
            'assignments__role',
            'assignments__role__type',
        )

    # def get_initial(self):
    #     initial_data = super(WeekEditView, self).get_initial()

    #     # print(initial_data.assignments.values_list('id', flat=True))
    #     print(initial_data)

    #     initial_assignments = []

    #     initial_assignments.append(
    #         Assignment(
    #             week,
    #             # staffer,
    #             role=Role.objects.get(id=1),
    #             # day=
    #         )
    #     )

    #     initial_data['assignments'] = initial_assignments

    #     print()

    #     return initial_data

    # def get_context_data(self, **kwargs):
    #     pass


class WeekDetailView(LoginRequiredMixin, DetailView):
    queryset = Week.objects.all().prefetch_related(
        'assignments',
        'assignments__role',
        'assignments__staffer',
    )
    template_name = 'assignment_desk/weeks/detail.html'

    def get_context_data(self, **kwargs):
        context = super(WeekDetailView, self).get_context_data(**kwargs)

        grouped_assignments = {}

        for assignment in self.object.assignments.all():
            if assignment.role.name not in grouped_assignments:
                grouped_assignments[assignment.role.name] = {}

            day_name = assignment.day.strftime('%A').lower()

            grouped_assignments[
                assignment.role.name
            ][day_name] = assignment.staffer

        roles_for_type = Role.objects.filter(
            type_id=self.object.role_type.pk
        ).order_by('priority')

        context['available_roles'] = roles_for_type

        context['roles_with_assignments'] = {
            role.slug: {
                (day): (
                    grouped_assignments[role.name][day]
                    if role.name in grouped_assignments
                    and day in grouped_assignments[role.name]
                    else None
                ) for day in DAYS_IN_WEEK
            }
            for role in roles_for_type
        }

        # print(context['roles_with_assignments']['230-meeting']['friday'].name)

        return context
