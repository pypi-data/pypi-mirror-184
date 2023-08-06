# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2022 Scipp contributors (https://github.com/scipp)

from ...core.utils import merge_masks
from .canvas import Canvas

import scipp as sc
import numpy as np
from typing import Dict
import uuid


def _parse_dicts_in_kwargs(kwargs, name):
    out = {}
    for key, value in kwargs.items():
        if isinstance(value, dict):
            if name in value:
                out[key] = value[name]
        else:
            out[key] = value
    return out


class Line:
    """
    Artist to represent one-dimensional data.
    If the coordinate is bin centers, the line is (by default) a set of markers.
    If the coordinate is bin edges, the line is a step function.

    Parameters
    ----------
    canvas:
        The canvas that will display the line.
    data:
        The initial data to create the line from.
    number:
        The canvas keeps track of how many lines have been added to it. This number is
        used to set the color and marker parameters of the line.
    """

    def __init__(self, canvas: Canvas, data: sc.DataArray, number: int = 0, **kwargs):

        self._fig = canvas.fig
        self._data = data

        args = _parse_dicts_in_kwargs(kwargs, name=data.name)

        self._line = None
        self._mask = None
        self._error = None
        self._dim = None
        self._unit = None
        self.label = data.name
        self._dim = self._data.dim
        self._unit = self._data.unit
        self._coord = self._data.meta[self._dim]
        self._id = uuid.uuid4().hex

        self._make_line(data=self._make_data(), number=number, **args)

    def _make_line(self,
                   data: Dict,
                   number: int,
                   errorbars: bool = True,
                   mask_color: str = 'black',
                   mode='markers',
                   marker=None,
                   **kwargs):
        """
        Create either plot markers or a step function, depending on whether the data
        contains bin edges or not.

        Parameters
        ----------
        data:
            A dictionary containing data entries that have been pre-processed to be in
            a format that Matplotlib can directly use.
        number:
            The line number to set colors and marker style.
        errorbars:
            Show errorbars if ``True``.
        mask_color:
            The color to be used to represent the masks.
        **kwargs:
            The kwargs are forwarded to:

            - ``matplotlib.pyplot.plot`` for data with a non bin-edge coordinate
            - ``matplotlib.pyplot.step`` for data with a bin-edge coordinate
        """
        import plotly.graph_objects as go
        from plotly.colors import qualitative as plotly_colors

        has_mask = data["mask"] is not None
        mask_data_key = "mask" if has_mask else "values"

        default_colors = plotly_colors.Plotly
        default_line_style = {'color': default_colors[number % len(default_colors)]}
        default_marker_style = {'symbol': number % 53}  # Plotly has 52 marker styles

        line_shape = None

        if data["hist"]:
            line_shape = 'vh'
            mode = 'lines'

        marker_style = default_marker_style if marker is None else marker
        line_style = {**default_line_style, **kwargs}

        self._line = go.Scatter(x=np.asarray(data["values"]["x"]),
                                y=np.asarray(data["values"]["y"]),
                                name=self.label,
                                mode=mode,
                                marker=marker_style,
                                line_shape=line_shape,
                                line=line_style)

        if errorbars and ("e" in data["variances"]):
            self._error = go.Scatter(x=np.asarray(data["variances"]["x"]),
                                     y=np.asarray(data["variances"]["y"]),
                                     line=line_style,
                                     name=self.label,
                                     mode='markers',
                                     marker={'opacity': 0},
                                     error_y={
                                         'type': 'data',
                                         'array': data["variances"]["e"]
                                     },
                                     showlegend=False)

        marker_line_style = {'width': 3, 'color': mask_color}
        if 'line' in marker_style:
            marker_style['line'].update(marker_line_style)
        else:
            marker_style['line'] = marker_line_style
        if 'width' in line_style:
            line_style['width'] *= 5
        else:
            line_style['width'] = 5
        if data["hist"]:
            line_style['color'] = mask_color

        self._mask = go.Scatter(x=np.asarray(data["values"]["x"]),
                                y=np.asarray(data[mask_data_key]["y"]),
                                name=self.label,
                                mode=mode,
                                marker=marker_style,
                                line_shape=line_shape,
                                line=line_style,
                                visible=has_mask,
                                showlegend=False)

        # Below, we need to re-define the line because it seems that the Scatter trace
        # that ends up in the figure is a copy of the one above.
        # Plotly has no concept of zorder, so we need to add the traces in a specific
        # order
        if data["hist"]:
            self._fig.add_trace(self._mask)
            self._mask = self._fig.data[-1]
            self._fig.add_trace(self._line)
            self._line = self._fig.data[-1]
            if self._error is not None:
                self._fig.add_trace(self._error)
                self._error = self._fig.data[-1]
        else:
            self._fig.add_trace(self._line)
            self._line = self._fig.data[-1]
            if self._error is not None:
                self._fig.add_trace(self._error)
                self._error = self._fig.data[-1]
            self._fig.add_trace(self._mask)
            self._mask = self._fig.data[-1]
        self._line._plopp_id = self._id
        self._mask._plopp_id = self._id
        if self._error is not None:
            self._error._plopp_id = self._id

    def _preprocess_hist(self, data: dict) -> dict:
        """
        Convert 1d data to be plotted to internal format, e.g., padding
        histograms and duplicating info for variances.
        """
        x = data["values"]["x"]
        y = data["values"]["y"]
        hist = len(x) != len(y)
        if hist:
            data["values"]["y"] = np.concatenate((y[0:1], y))
            if data["mask"] is not None:
                data["mask"]["y"] = np.concatenate(
                    (data["mask"]["y"][0:1], data["mask"]["y"]))
        if self._data.variances is not None:
            data["variances"]["x"] = 0.5 * (x[1:] + x[:-1]) if hist else x
        data["variances"]["y"] = y
        data["hist"] = hist
        return data

    def _make_data(self) -> dict:
        data = {"values": {}, "variances": {}, "mask": None}
        data["values"]["x"] = self._data.meta[self._dim].values
        data["values"]["y"] = self._data.values
        if self._data.variances is not None:
            data["variances"]["e"] = sc.stddevs(self._data.data).values
        if len(self._data.masks):
            one_mask = merge_masks(self._data.masks).values
            data["mask"] = {
                "y": np.where(one_mask, data["values"]["y"], None).astype(np.float32)
            }
        return self._preprocess_hist(data)

    def update(self, new_values: sc.DataArray):
        """
        Update the x and y positions of the data points from new data.

        Parameters
        ----------
        new_values:
            New data to update the line values, masks, errorbars from.
        """
        self._data = new_values
        new_values = self._make_data()

        with self._fig.batch_update():
            self._line.update({
                'x': new_values["values"]["x"],
                'y': new_values["values"]["y"]
            })

            if (self._error is not None) and ("e" in new_values["variances"]):
                self._error.update({
                    'x': new_values["variances"]["x"],
                    'y': new_values["variances"]["y"],
                    'error_y': {
                        'array': new_values["variances"]["e"]
                    }
                })

            if new_values["mask"] is not None:
                update = {'x': new_values["values"]["x"], 'y': new_values["mask"]["y"]}
                self._mask.update(update)
                self._mask.visible = True
            else:
                self._mask.visible = False

    def remove(self):
        """
        Remove the line, masks and errorbar artists from the canvas.
        """
        self._fig.data = [
            trace for trace in list(self._fig.data) if trace._plopp_id != self._id
        ]

    @property
    def color(self):
        """
        The line color.
        """
        return self._line.line.color

    @color.setter
    def color(self, val):
        self._line.line.color = val
