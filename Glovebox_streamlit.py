# -*- coding: utf-8 -*-
"""
Created on 03/10/2021

@author: Filippo Cavalca
"""
  
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#import plotly.express as px
#import numpy as np
import pandas as pd
import streamlit as st

st.title("Glovebox data plotter")
file = st.sidebar.file_uploader("Upload a data file", type=["gdb"])



if file:
    
    #Make pandas dataframe from raw data
    data = pd.read_csv(file, sep='\t', header=9, index_col=0)
    data
    len(data.columns)
    data.index =  pd.to_datetime(data.index, format="%d.%m.%Y %H:%M:%S")

    tmin = st.sidebar.date_input("Select start date", min_value=data.index.min(), max_value=data.index.max(), value=data.index.min())
    tmax = st.sidebar.date_input("Select stop date", min_value=data.index.min(), max_value=data.index.max(), value=data.index.max())

    # Create a Plotly figure.
    fig = go.Figure()
    
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    fig.update_layout(
        hovermode='x',
        height=800,
        width=800,
        plot_bgcolor='#ffffff'
    )
    
    # Dict to set better axis properties.
    xaxis_dict = {
        # Move ticks outside the plot.
        'ticks': 'inside',
        # Show plot borders with these four settings.
        'showline': True,
        'linewidth': 2,
        'linecolor': 'black',
        'mirror': True,
        # Remove gridlines in the plot.
        'showgrid': False
    }
    yaxis_dict = {
        # Move ticks outside the plot.
        'ticks': 'outside',
        # Show plot borders with these four settings.
        'showline': True,
        'linewidth': 2,
        'linecolor': 'black',
        'mirror': True,
        # Remove gridlines in the plot.
        'showgrid': False
    }
    fig.update_xaxes(xaxis_dict)
    fig.update_yaxes(yaxis_dict)
    
    
    #%%
    #fig.add_trace(px.scatter(data, x=data.index, y=data[data.columns[0]]),row=1, col=1)
    if len(data.columns)>5:
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[0]], name = data.columns[0]),row=1, col=1)
        fig.update_yaxes(title_text="Partial pressures (ppm)", row=1, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[1]], name = data.columns[1]),row=1, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[2]], name = data.columns[2]),row=2, col=1)
        fig.update_yaxes(title_text="Pressures", row=2, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[3]], name = data.columns[3]),row=2, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[4]], name = data.columns[4]),row=3, col=1)
        fig.update_yaxes(title_text="Temperatures (°C)", row=3, col=1)
    
    
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[5]], name = data.columns[5]),row=3, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[6]], name = data.columns[6]),row=3, col=1)
        fig.update_xaxes(title_text=data.index.name, row=3, col=1)
        
    else:
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[0]], name = data.columns[0]),row=1, col=1)
        fig.update_yaxes(title_text="Partial pressures (ppm)", row=1, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[1]], name = data.columns[1]),row=1, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[2]], name = data.columns[2]),row=2, col=1)
        fig.update_yaxes(title_text="Pressure", row=2, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[3]], name = data.columns[3]),row=3, col=1)
        
        fig.add_trace(go.Scattergl(x=data.index, y=data[data.columns[4]], name = data.columns[4]),row=3, col=1)
        fig.update_yaxes(title_text="Temperatures (°C)", row=3, col=1)
    
    
        
    
    fig.update_xaxes(range=[tmin, tmax])
    fig.update_yaxes(autorange=True, fixedrange=False)


    
    st.plotly_chart(fig)
    
else:
    st.write("Upload a file to get started")
