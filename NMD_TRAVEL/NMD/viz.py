import numpy as np
import pandas as pd
from config import *
import plotly.graph_objects as go
import plotly.express as px

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import io


def plot_interact_corr_matrix(df, start_date, end_date, selected_columns):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if selected_columns:
        df_corr = df_filtered[selected_columns]
        corr_matrix = df_corr.drop(columns=['Date'], errors='ignore').corr()

        plt.figure(figsize=(12, 12))
        sns.heatmap(corr_matrix, annot=True, cmap='Greens', vmin=-1, vmax=1)
        plt.suptitle(f'Correlation matrix    ({start_date.date()} - {end_date.date()})', fontweight='bold',
                     color=default_color1, fontsize=18)

        plt.tight_layout()

        st.pyplot(plt.gcf())

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', transparent=True)
        buffer.seek(0)

        st.download_button(
            label="Download Correlation Matrix",
            data=buffer,
            file_name="correlation_matrix.png",
            mime="image/png"
        )

    else:
        st.write("Selecione pelo menos uma coluna para gerar a matriz de correlação.")


def plot_interactive_graph(df):
    if len(df.columns) > 1:
        fig = px.line(
            df,
            x='Date',
            y=df.columns[1:],
            title="Time Evolution of Selected Variables",
            markers=True
        )

        fig.update_layout(
            width=1200,
            height=600,
            legend=dict(
                orientation="v",
                x=40,
                xanchor="right",
                y=1,
                font=dict(size=9)
            )
        )

        st.plotly_chart(fig)
    else:
        st.write("Please select at least one variable to plot.")


def plot_dual_axis_graph(df_interest, df_notional):
    fig = go.Figure()

    for col in df_interest.columns[1:]:
        fig.add_trace(
            go.Scatter(x=df_interest['Date'], y=df_interest[col], name=col,
                       mode='lines+markers', marker=dict(size=5, symbol='circle'),
                       yaxis='y1')
        )

    for col in df_notional.columns[1:]:
        fig.add_trace(
            go.Scatter(x=df_notional['Date'], y=df_notional[col], name=col,
                       mode='lines+markers', marker=dict(size=5, symbol='circle'),
                       yaxis='y2')
        )

    fig.update_layout(
        title="Dual Axis Time Evolution Plot",
        xaxis=dict(title='Date'),
        yaxis=dict(
            title="Interest rates",
            titlefont=dict(color="black"),
            tickfont=dict(color="black")
        ),
        yaxis2=dict(
            title="Notionals (M€)",
            titlefont=dict(color="black"),
            tickfont=dict(color="black"),
            overlaying='y',
            side='right'
        ),
        width=1200,
        height=600,
        legend=dict(
            orientation="v",
            x=40,
            xanchor="right",
            y=1,
            font=dict(size=9)
        )
    )
    st.plotly_chart(fig)