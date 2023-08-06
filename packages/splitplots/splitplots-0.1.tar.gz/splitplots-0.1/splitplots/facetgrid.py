import inspect
import warnings

import numpy as np
import matplotlib.pyplot as plt
from decorator import decorator


@decorator
def mapper(f, self, *args, **kwargs):
    signature = inspect.signature(f)
    arg_names = list(signature.parameters.keys())
    assert arg_names[:2] == ['self', 'func']
    if len(args) >= 1 and callable(args[0]):
        func = args[0]
        args = args[1:]
        return f(self, func, *args, **kwargs)
    else:
        def inner(func):
            return f(self, func, *args, **kwargs)

        return inner


class FacetGrid:
    def __init__(self, data, row=[], col=[], hue=[], size=3.5, aspect=1.2, sharex=True, sharey=True, margin_titles=True):
        self.data = data.reset_index()
        self.row = [row] if isinstance(row, str) else row
        self.col = [col] if isinstance(col, str) else col
        self.hue = [hue] if isinstance(hue, str) else hue
        self.margin_titles = margin_titles

        self.n = len(self.data)
        self.size = size
        self.aspect = aspect
        self.width = self.size * self.aspect ** 0.5
        self.height = self.size / self.aspect ** 0.5

        for k in ['row', 'col', 'hue']:
            vals = [tuple(v) for v in self.data[getattr(self, k)].values]
            ix_map = {v: i for i, v in enumerate(sorted(set(vals)))}
            ix = np.array([ix_map[v] for v in vals])
            setattr(self, f'{k}_n', len(ix_map))
            setattr(self, f'{k}_ix_map', ix_map)
            setattr(self, f'{k}_ix', ix)

        self.fig, self.ax = plt.subplots(nrows=self.row_n, ncols=self.col_n, figsize=(self.col_n * self.width, self.row_n * self.height), sharex=sharex, sharey=sharey, squeeze=False)
        if self.margin_titles:
            for v, i in self.row_ix_map.items():
                a = self.ax[i, -1]
                a.annotate('\n'.join(f'{k}={v}' for k, v in zip(self.row, v)), xy=(1.02, 0.5), xycoords='axes fraction', rotation=270, ha='left', va='center')
            for v, i in self.col_ix_map.items():
                self.ax[0, i].annotate('\n'.join(f'{k}={v}' for k, v in zip(self.col, v)), xy=(0.5, 1.05), xycoords='axes fraction', ha='center')

        self.legend_entries = {}
        self.fig.tight_layout()

    @property
    def colors(self):
        return [f'C{i % 10}' for i in range(self.hue_n)]

    @mapper
    def map(self, func, *args, func_row=None, func_col=None, func_ax=None, func_hue=None, func_x=None, **kwargs):
        self.legend_entries = {}

        data = self.data.copy()
        args_cols = [f'_a_{i}' for i in range(len(args))]
        for k, a in zip(args_cols, args):
            data[k] = data[a] if a in data else data.eval(a)

        if sum(f is not None for f in [func_row, func_col, func_ax, func_hue, func_x]) > 1:
            warnings.warn('More than one of func_row, func_col, func_ax, func_hue, func_x is set')
        for k in args_cols:
            if func_row is not None:
                data[k] = data.groupby(self.row)[k].transform(func_row)
            if func_col is not None:
                data[k] = data.groupby(self.col)[k].transform(func_col)
            if func_ax is not None:
                data[k] = data.groupby(self.row + self.col)[k].transform(func_ax)
            if func_hue is not None:
                data[k] = data.groupby(self.row + self.col + self.hue)[k].transform(func_hue)
        if func_x is not None:
            for k in args_cols[1:]:
                data[k] = data.groupby(self.row + self.col + self.hue + ['_a_0'])[k].apply(func_x)

        for row_k, row_gr in (data.groupby(self.row) if self.row else [([], data)]):
            for col_k, col_gr in (row_gr.groupby(self.col) if self.col else [([], row_gr)]):
                for hue_k, hue_gr in (col_gr.groupby(self.hue) if self.hue else [([], col_gr)]):
                    ix = hue_gr.index[0]
                    plt.sca(self.ax[self.row_ix[ix], self.col_ix[ix]])
                    if not self.margin_titles:
                        plt.title(' '.join([f'{k}={v}' for k, v in dict(hue_gr.iloc[0][[*self.row, *self.col]]).items()]))
                    if 'c' not in kwargs:
                        kwargs['color'] = self.colors[self.hue_ix[ix]]
                    hndl = func(*[hue_gr[k] for k in args_cols], **kwargs, label=hue_k)
                    if isinstance(hndl, (list, tuple)):
                        hndl = hndl[0]
                    self.legend_entries[tuple(hue_k) if isinstance(hue_k, list) else hue_k] = hndl

    @mapper
    def map_ax(self, func, *args, func_row=None, func_col=None, func_ax=None, func_hue=None, func_x=None, **kwargs):
        data = self.data.copy()
        args_cols = [f'_a_{i}' for i in range(len(args))]
        for k, a in zip(args_cols, args):
            data[k] = data[a] if a in data else data.eval(a)

        if sum(f is not None for f in [func_row, func_col, func_ax, func_hue, func_x]) > 1:
            warnings.warn('More than one of func_row, func_col, func_ax, func_hue, func_x is set')
        for k in args_cols:
            if func_row is not None:
                data[k] = data.groupby(self.row)[k].transform(func_row)
            if func_col is not None:
                data[k] = data.groupby(self.col)[k].transform(func_col)
            if func_ax is not None:
                data[k] = data.groupby(self.row + self.col)[k].transform(func_ax)
            if func_hue is not None:
                data[k] = data.groupby(self.row + self.col + self.hue)[k].transform(func_hue)
        if func_x is not None:
            for k in args_cols[1:]:
                data[k] = data.groupby(self.row + self.col + self.hue + ['_a_0'])[k].apply(func_x)

        for row_k, row_gr in (data.groupby(self.row) if self.row else [([], data)]):
            for col_k, col_gr in (row_gr.groupby(self.col) if self.col else [([], row_gr)]):
                ix = col_gr.index[0]
                plt.sca(self.ax[self.row_ix[ix], self.col_ix[ix]])
                hndl = func(*[col_gr[k] for k in args_cols], **kwargs)

    @mapper
    def map_all_ax(self, func):
        for a in self.ax.ravel():
            plt.sca(a)
            func()

    def legend(self):
        if self.row_n * self.height > 20:
            locs = ['upper right', 'lower right', 'center right']
        elif self.row_n * self.height > 10:
            locs = ['upper right', 'lower right']
        else:
            locs = ['center right']
        for loc in locs:
            leg = self.fig.legend(self.legend_entries.values(), self.legend_entries.keys(), title=', '.join(self.hue), frameon=True, loc=loc)
        self.fig.draw(self.fig.canvas.get_renderer())
        legend_width = leg.get_window_extent().width / self.fig.dpi
        figure_width = self.fig.get_figwidth()
        self.fig.set_figwidth(figure_width + legend_width)
        self.fig.draw(self.fig.canvas.get_renderer())
        space_needed = legend_width / (figure_width + legend_width)
        self.fig.subplots_adjust(right=1 - (0.03 + space_needed))

    def show_counts(self):
        data = self.data
        for row_k, row_gr in (data.groupby(self.row) if self.row else [([], data)]):
            for col_k, col_gr in (row_gr.groupby(self.col) if self.col else [([], row_gr)]):
                ix = col_gr.index[0]
                plt.sca(self.ax[self.row_ix[ix], self.col_ix[ix]])
                plt.text(0.01, 0.985, f'n={len(col_gr)}',
                         bbox={'pad': 1, 'alpha': 0.9, 'facecolor': 'white', 'edgecolor': 'none'},
                         transform=plt.gca().transAxes, ha='left', va='top')

    def set(self, **kwargs):
        for a in self.ax.ravel():
            a.set(**kwargs)
