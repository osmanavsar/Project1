from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.io as pio

def home(request):
    return render(request, "base.html")

def plot(request):
    df = pd.read_csv("static/data.csv", header=0)
    df.info(verbose=True)
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Turkey')
    div = pio.to_html(fig, include_plotlyjs=False, full_html=False)
    return render(request, "plotly_demo.html", {"my_plot": div})