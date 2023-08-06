import numpy as np
import pandas as pd
import ezhc as hc
from scipy import interpolate

ROUND_NB_DIGIT = 2


def vol_unit(unit):
    """
    to help express vol either in bp/day or bp/year
    """
    u = unit.upper()
    if u == 'DAY' or u == 'D':
        return 1 / 252 ** 0.5
    else:
        return 1


def get_diff(data, start_date, end_date):
    """
    get difference between 2 dates
    """
    mask_1 = (data.index.get_level_values('date') == end_date)
    mask_2 = (data.index.get_level_values('date') == start_date)
    one = data.loc[mask_1]
    one.index = one.index.droplevel('date')
    two = data.loc[mask_2]
    two.index = two.index.droplevel('date')
    # res=res.index.droplevel('date')
    return one - two


def get_max(data, resize=False, *args):
    """
    get max
    TBC
    """
    if resize:
        data = select_data(data, *args)
    x = data.groupby(level='expiry').apply(max)
    return x.reindex(data.index.get_level_values('expiry').unique(), axis=0)


def get_min(data, resize=False, *args):
    """
    get min
    TBC
    """
    if resize:
        data = select_data(data, *args)
    x = data.groupby(level='expiry').apply(min)
    return x.reindex(data.index.get_level_values('expiry').unique(), axis=0)


def get_surface(data, date):
    """
    get surface for given date
    TBC
    """
    mask = (data.index.get_level_values('date') == date)
    x = data.loc[mask]
    return drop_level(x, 'date')


def select_data(data, args):
    """
    select data from dataframe
    args:
        for discrete values
            field, value1, value2, etc
        for range of values
            field, value_start, value_end, 'range'

    returns subset dataframe
    TBC
    """
    arg = args
    if arg[0] == 'date':
        if len(arg) == 4 and arg[3] == 'range':
            mask = (data.index.get_level_values(arg[0]) >= arg[1]) & (
                data.index.get_level_values(arg[0]) <= arg[2])
        else:
            mask = (data.index.get_level_values(arg[0]) == arg[1])
            for ar in arg[2:len(arg)]:
                mask = mask | (data.index.get_level_values(arg[0]) == ar)
    else:
        mask = (data.index.get_level_values(arg[0]) == arg[1])
        for ar in arg[2:len(arg)]:
            mask = mask | (data.index.get_level_values(arg[0]) == ar)

    return data.loc[mask]


def drop_level(data, index):
    """
    drop level of input dataframe - inplace
    TBC
    """
    data.index = data.index.droplevel(index)
    return data


def get_percentile(data, date, resize=False, *args):
    """
    get percentile rank from input dataframe
    TBC
    """
    if resize:
        data = select_data(data, *args)
    return get_surface(data.groupby(level='expiry').rank(pct=True), date)


def get_mean(data, resize=False, *args):
    """
    get mean
    TBC
    """
    if resize:
        data = select_data(data, *args)
    data = data.dropna()
    x = data.groupby(level='expiry').apply(np.mean)
    return x.reindex(data.index.get_level_values('expiry').unique(), axis=0)


def get_std(data, resize=False, *args):
    """
    get standard deviation
    TBC
    """
    if resize:
        data = select_data(data, *args)
    data = data.dropna()
    x = data.groupby(level='expiry').apply(np.std)
    return x.reindex(data.index.get_level_values('expiry').unique(), axis=0)


def get_z_score(data, end_dt, resize=False, *args):
    """
    get z-score
    TBC
    """
    if resize:
        data = select_data(data, *args)
    return (get_surface(data, end_dt) - get_mean(data)) / get_std(data)


def build_weight(spread, weight, **kwargs):
    """
    build weight
    TBC
    """
    if (len(spread) is not len(weight)):
        if kwargs == {}:
            kwargs.setdefault('type', 'S')
        else:
            kwargs = kwargs['kwargs']

        if (len(spread) % 2 == 0 or (len(spread) % 2 == 0 and len(spread) % 3 == 0)) and (
                kwargs['type'].upper() != 'FLY' or kwargs['type'].upper() != 'F'):
            print('spread - weight len mismatch by default spread weighted (-1,1)')
            w = np.repeat(1, len(spread))
            pos = np.arange(1, len(w), 2)
            w[pos] = w[pos] * -1
        elif (len(spread) % 3 == 0 or (len(spread) % 2 == 0 and len(spread) % 3 == 0)) and (
                kwargs['type'].upper() == 'FLY' or kwargs['type'].upper() == 'F'):
            print('fly - weight len mismatch by default fly weighted (-1,2,-1)')
            w = np.repeat(-1, len(spread))
            pos = np.arange(1, len(w), 2)
            w[pos] = w[pos] * -2
    else:
        w = weight
    return w


# def build_spread(data, spread, typ_, resize=False, *args):
#     """
#     build spread
#     TBC
#     """
#     if resize:
#         data = select_data(data, args)
#     res = pd.DataFrame()
#     if typ_.upper() == "S" or typ_.upper() == "SLOPE":
#         for s in spread:
#             res[s[0] + s[1]] = data[s[1]] - data[s[0]]
#         return res
#     if typ_.upper() == "C" or typ._upper() == "CALENDAR":
#         from collections import OrderedDict
#         dic = OrderedDict()
#         for s in spread:
#             dic[(s[0] + s[1])] = data.loc[s[1]] - data.loc[s[0]]
#         res = pd.concat(dic.values(), keys=dic.keys())
#         res.index.names = ('expiry', 'date')
#         return res


def build_spread(data, spread, axis="T", weight=[], resize=False, *args, **kwargs):
    """
    build weight
    TBC
    """
    if resize:
        data = select_data(data, args)
    res = pd.DataFrame()
    w = build_weight(spread[0], weight, **kwargs)
    if axis.upper() == 'T' or axis.upper() == 'TENOR':
        for s in spread:
            nme = str()
            for i, e in enumerate(s):
                if i == 0:
                    res_tmp = data[s[i]] * w[i]
                else:
                    res_tmp = res_tmp + data[s[i]] * w[i]
                nme = nme + s[i]
            res[nme] = res_tmp
        return res

    if axis.upper() == 'E' or axis.upper() == 'EXPIRY':
        from collections import OrderedDict
        dic = OrderedDict()
        idx = data.loc[spread[0][0]].index
        col = data.loc[spread[0][0]].columns
        for s in spread:
            res_tmp = pd.DataFrame(0, index=idx, columns=col)
            nme = str()
            for i, e in enumerate(s):
                res_tmp = res_tmp + data.loc[s[i]] * w[i]
                nme = nme + s[i]
            dic[nme] = res_tmp
        res = pd.concat(dic.values(), keys=dic.keys())
        res.index.names = ('expiry', 'date')
        return res


def select(vol, expiries, tenors):
    if 'tenor' in vol.columns.names and 'expiry' in vol.index.names:
        return vol[tenors].loc[expiries]
    elif 'tenor' in vol.index.names and 'expiry' in vol.columns.names:
        return vol[expiries].loc[tenor]
    elif 'tenor' in vol.columns.names and 'expiry' in vol.columns.names:
        if vol.columns.names[0] is 'tenor':
            return vol.loc[:, (tenors, expiries)]
        else:
            return vol.loc[:, (expiries, tenors)]
    elif 'tenor' in vol.index.names and 'expiry' in vol.index.names:
        if vol.index.names[0] is 'tenor':
            return vol.loc[(tenors, expiries), :]
        else:
            return vol.loc[(expiries, tenors), :]


def generate_couples(start, end, step):
    return [[round(start + i * step, 2), round(end - i * step, 2)] for i in range(int((0.5 - start) / step))]


def volatility_cone(vol, expiries, tenors, start_date, start=0, end=1, step=0.25, plot=True):
    exp = expiries.split(',')
    ten = tenors.split(',')
    assert len(exp) is 1 or len(ten) is 1, """ one of expiries or tenors should take a single value """
    df = select(vol, exp, ten)
    df2 = df.loc[start_date:].quantile(q=np.arange(start, end + step, step))
    df2.loc['last'] = df.iloc[-1]
    return df2


def ewma(data, window=None, alpha=None):
    if alpha is None:
        alpha = 2 / (window + 1.0)
        alpha_rev = 1 - alpha
    else:
        alpha_rev = alpha
        alpha = 1 - alpha_rev

    n = data.shape[0]

    pows = alpha_rev ** (np.arange(n + 1))
    scale_arr = 1 / pows[:-1]
    offset = data[0] * pows[1:]
    pw0 = alpha * alpha_rev ** (n - 1)

    mult = data * pw0 * scale_arr
    cumsums = mult.cumsum()
    out = offset + cumsums * scale_arr[::-1]
    return out


def built_quantile_series(df, list_of_quantiles, colors):
    df = df.T
    df.columns = [round(float(d), 2) if d is not 'last' else d for d in df.columns]

    quantiles = []
    k = 0
    for i in list_of_quantiles:
        quantiles.append({
            'name': str(i[0] * 100) + ' ' + str(i[1] * 100) + ' percentile.',
            'data': [[list(df[i[0]].to_dict().values())[j], list(df[i[1]].to_dict().values())[j]] for j in
                     range(len(df.index))],
            'type': 'arearange',
            'color': colors[k],
            'marker': {
                'enabled': 'false'
            }
        })
        k += 1
    res = quantiles + [{'name': 'median',
                        'data': list(df[0.5].to_dict().values()),
                        'color': '#EEEEEE',
                        'lineWidth': 5,
                        'marker': {
                            'enabled': 'false'
                        }}, ] + [{'name': 'last',
                                  'data': list(df['last'].to_dict().values()),
                                  'color': '#FF0000',
                                  'lineWidth': 5,
                                  'marker': {'symbol': "circle",
                                             'radius': 5}}, ]
    return res


def vol_cone_plot(series, iv_rea, exp_ten, dt, xaxis=None, unit=' (bp/d)', save=False, save_path=None):
    g = hc.Highcharts()
    g.chart.height = 550
    g.legend.enabled = True
    g.legend.layout = 'horizontal'
    g.legend.align = 'center'
    g.legend.maxHeight = 100
    # g.tooltip.crosshairs = True
    g.tooltip.shared = True
    g.tooltip.valueSuffix = unit
    g.tooltip.valueDecimals = 2
    g.chart.zoomType = 'x'
    g.title.text = iv_rea + ' Volatility cone on ' + exp_ten + ' from ' + dt

    g.yAxis = [{'title': {'text': unit}},
               {'title': {'text': unit}, 'opposite': True}]

    g.xAxis = [{
        'categories': xaxis  # ['1M10Y', '3M10Y', '6M10Y', '1Y10Y','2Y10Y','5Y10Y']
    }]

    g.series = series + []
    display(g.plot(save=save))


def generate_relative_strikes(start, end, step):
    l = np.arange(start, end + step, step)
    return ",".join(['@' + str(ll) + 'bp' for ll in l])


def local_interpolation_one_by_two(df, idx, nb_of_points=2, step=0.001):
    c = list(df.columns)
    index = df.index
    width = []
    error = []
    k = 0
    for i in idx:
        ind = index[k]
        idx_ = c.index(i)
        min_ = c[idx_ - nb_of_points]
        max_ = c[idx_ + nb_of_points]
        data = df.loc[ind, min_:max_]
        strikes = [d.replace('@', '') for d in data.index]
        strikes = [float(s.replace('bp', '')) for s in strikes]
        tck = interpolate.splrep(strikes, data, s=0)
        xnew = np.arange(strikes[0], strikes[-1] + step, step)
        ynew = interpolate.splev(xnew, tck, der=0)
        ynew = pd.DataFrame([ynew], columns=xnew)
        ynew_abs = ynew.abs()
        width.append(float(ynew_abs.idxmin(axis=1)) / 2)
        ii = list(xnew).index(float(ynew_abs.idxmin(axis=1)))
        error.append(ynew.iloc[0, ii])
        k += 1
    return pd.concat([pd.DataFrame(width, columns=['width'], index=index).abs(),
                      pd.DataFrame(error, columns=['error'], index=index)], axis=1)
