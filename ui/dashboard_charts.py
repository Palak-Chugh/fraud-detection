import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def create_fraud_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",

            value=score * 100,

            title={
                "text":
                "Fraud Risk Score"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "thickness": 0.4
                },

                "steps": [
                    {
                        "range": [0, 40]
                    },
                    {
                        "range": [40, 75]
                    },
                    {
                        "range": [75, 100]
                    }
                ]
            }
        )
    )

    fig.update_layout(
        height=350
    )

    return fig


def create_risk_chart():

    data = pd.DataFrame({
        "Risk":
        [
            "Low",
            "Medium",
            "High"
        ],

        "Count":
        [
            8,
            4,
            2
        ]
    })

    fig = px.pie(
        data,
        values="Count",
        names="Risk",
        title="Risk Distribution"
    )

    fig.update_layout(
        height=350
    )

    return fig