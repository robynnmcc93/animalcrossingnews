from django.shortcuts import render

from .models import Heading
from .models import Story


def index(request):
    latest_heading_list = Heading.objects.order_by('-pub_date')[:5]
    latest_story_list = Story.objects
    context = {'latest_heading_list': latest_heading_list}
    return render(request, 'animalcrossingnews/index.html', context, latest_story_list)



