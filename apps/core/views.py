from django.shortcuts import render, get_object_or_404
from .filters import DomainFilter
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as po
from django import forms
from .forms import *
from .models import *


# Create your views here.
def home(requests):
    return render(requests, 'core/home.html')

def projects(requests):
    dropdown_domains = Dropdown_Domains()
    dropdown_tshirt_sizes = Dropdown_Tshirt_Sizes()
    dropdown_states = Dropdown_States()

    context = {
        'dropdown_domains': dropdown_domains,
        'dropdown_tshirt_sizes': dropdown_tshirt_sizes,
        'dropdown_states': dropdown_states,
    }

    return render(requests, 'core/projects.html', context)

def submit_new_project(requests):
    print("TEST")
    if requests.method == 'POST':
        
        name = request.POST["project_name"]
        estimation = request.POST["estimation"]

        context = {
            'project_name': name,
            'project_estimation': estimation,
        }

    return render(requests, 'core/projects.html', context)


def about(requests):
    projects = Project.objects.all()
    
    '''
        OVERALL PROJECT TABLE
    '''
    # apply filter
    tableFilter = DomainFilter(requests.GET, queryset=projects)
    projects = tableFilter.qs

    '''
        NUMBER OF PROJECTS PER STATE
    '''
    states = []
    counts = []
    project_states = Project.objects.values_list('prj_state').distinct()
    for state in project_states:
        count = Project.objects.filter(prj_state=state[0]).count()
        states.append(state[0])
        counts.append(count)

    df = pd.Series(data=counts, index=states)
    state_counts = df.to_dict()

    '''
        PLOTLY
    '''
    data1 = {
   "values": states,
   "labels": counts,
   "domain": {"column": 0},
   "name": "seats",
   "hoverinfo":"label+percent+name",
   "hole": .7,
   "type": "pie"
    }
    data2 = {
    "values": states,
    "labels": counts,
    "domain": {"column": 1},
    "name": "vote share",
    #"hoverinfo":"label+percent",
    #"hole": .8,
    "type": "pie"
    }

    data = [data1,data2]
    layout = go.Layout(
    {
        "title":"Parliamentary Election 2019",
        "grid": {"rows": 1, "columns": 2},
        "annotations": [
            {
                "font": {
                "size": 20
                },
                "showarrow": False,
                "text": "seats",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                "size": 20
                },
                "showarrow": False,
                "text": "votes",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = po.plot(fig, output_type='div')


    # context preparation for handover to html
    context = {'prjs': projects, 'state_counts': state_counts, 'plot_div': plot_div, 'tableFilter': tableFilter}

    return render(requests, 'core/about.html', context)
    