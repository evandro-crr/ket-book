
import plotly.graph_objs as go
import numpy as np


def bloch_sphere(ket: np.array) -> go.Figure:
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 40)
    phi, theta = np.meshgrid(phi, theta)
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    sphere = go.Surface(x=x, y=y, z=z, showscale=False, opacity=0.02)

    equator_theta = np.linspace(0, 2 * np.pi, 100)
    equator_x = np.cos(equator_theta)
    equator_y = np.sin(equator_theta)
    equator_z = np.zeros_like(equator_theta)

    equator = go.Scatter3d(
        x=equator_x,
        y=equator_y,
        z=equator_z,
        mode="lines",
        line=dict(color="gray", width=3),
        opacity=0.1,
    )

    zero_to_one = go.Scatter3d(
        x=[0, 0],
        y=[0, 0],
        z=[1, -1],
        mode="lines",
        line=dict(color="gray", width=3),
        opacity=0.1,
    )

    basis_points = [
        ([0, 0, 1], "|0⟩"),
        ([0, 0, -1], "|1⟩"),
        ([1, 0, 0], "|+⟩"),
        ([-1, 0, 0], "|‒⟩"),
        ([0, 1, 0], "|i+⟩"),
        ([0, -1, 0], "|i‒⟩"),
    ]

    basis = [
        go.Scatter3d(
            x=[p[0]],
            y=[p[1]],
            z=[p[2]],
            mode="text",
            text=[text],
            textposition="middle center",
        )
        for p, text in basis_points
    ]

    bra = np.conjugate(ket.T)

    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.array([[1, 0], [0, -1]])
    exp_x = float((bra @ X @ ket).real[0][0])
    exp_y = float((bra @ Y @ ket).real[0][0])
    exp_z = float((bra @ Z @ ket).real[0][0])

    qubit = go.Scatter3d(
        x=[exp_x],
        y=[exp_y],
        z=[exp_z],
        mode="text",
        text=["|ѱ⟩"],
        textposition="middle center",
    )

    line = go.Scatter3d(
        x=[0, exp_x],
        y=[0, exp_y],
        z=[0, exp_z],
        mode="lines",
        line=dict(color="red", width=3),
        opacity=0.5,
    )

    fig = go.Figure(
        data=[
            sphere,
            qubit,
            line,
            equator,
            zero_to_one,
            *basis,
        ]
    )

    fig.update_layout(
        scene=dict(
            xaxis=dict(
                range=[-1, 1],
                showgrid=False,
                showbackground=False,
                visible=False,
            ),
            yaxis=dict(
                range=[-1, 1],
                showgrid=False,
                showbackground=False,
                visible=False,
            ),
            zaxis=dict(
                range=[-1, 1],
                showgrid=False,
                showbackground=False,
                visible=False,
            ),
            aspectmode="cube",
        ),
        showlegend=False,
    )

    return fig