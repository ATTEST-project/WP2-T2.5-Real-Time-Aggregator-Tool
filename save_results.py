from xlrd import *
from numpy import *
from pyomo.environ import *
from math import *
import pandas as pd
import xlwt


def save_results_aggr(m_h, t_main):

    DF_P_w = pd.DataFrame()
    DF_P_g = pd.DataFrame()
    DF_P_aggr_w_up = pd.DataFrame()
    DF_P_aggr_w_down = pd.DataFrame()

    for i in range(0, t_main + 1):
        m = m_h[i]

        for v in m.component_objects(Var, active=True):
            for index in v:  # index[0, j, i, t]; v = ve_in_hp,...
                    if v.name == 'P_w':
                        if (index[1]) == i:
                            DF_P_w.at[index[0], i] = value(v[index])
                    if v.name == 'P_g':
                        if (index[1]) == i:
                            DF_P_g.at[index[0], i] = value(v[index])
                    if v.name == 'P_aggr_w_up':
                        if (index[1]) == i:
                            DF_P_aggr_w_up.at[index[0], i] = value(v[index])
                    if v.name == 'P_aggr_w_down':
                        if (index[1]) == i:
                            DF_P_aggr_w_down.at[index[0], i] = value(v[index])

    print("...Save data...")
    with pd.ExcelWriter("Bids_aggregator.xls") as writer:
        DF_P_w.to_excel(writer, sheet_name='Electricity energy bid')
        DF_P_g.to_excel(writer, sheet_name='Gas energy bid')
        DF_P_aggr_w_up.to_excel(writer, sheet_name='Upward secondary band')
        DF_P_aggr_w_down.to_excel(writer, sheet_name='Downward secondary band')


    return 0

