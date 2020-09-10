#!/usr/bin/env python
# coding: utf-8

# データの種類ごとにさらにモジュールを分割する

import pandas as pd
import numpy as np
import os 
import re
from datetime import datetime

#日付情報を取得
from datetime import datetime
from pytz import timezone
date_now = datetime.now(timezone('Asia/Tokyo')).strftime("%Y%m%d")

path_stock_default = '/Users/username'
path_demand_default = ''
path_sales_default = ''
path_purchase_default = ''

path_indicator_default = ''
path_bmf_default = ''
path_scm_default = ''
path_supply_root_default = ''

# TODO ヘッダーファイル、データ型ファイルは別ファイルにまとめる
# メタデータは辞書化して管理した方が楽？
HEADER_STOCK = []
DTYPE_STOCK = {}
HEADER_DEMAND = []
DTYPE_DEMAND = {}
HEADER_SALES = []
DTYPE_SALES = {}
HEADER_PURCHASE = []
DTYPE_PURCHASE = {}

HEADER_INDICATOR = []
DTYPE_INDICATOR = {}

HEADER_BMF = []
DTYPE_BMF = {}
usecols_bmf_default = [0, 1, 2, 3]

DTYPE_SCM = {}
usecols_scm_default = [0, 1, 2, 3]

DTYPE_SUPPLY_ROOT = {}
usecols_supply_default = [0, 1, 2, 3]

class Stock:
    def __init__(self):
        print('Stockクラスからインスタンスが生成されました')
        
    def read_all_stock_pre(self, HEADER_STOCK, DTYPE_STOCK, path_stock=path_stock_default):
        '''STOCKデータを読みこむ
        '''
        
        filename = os.path.join(path_stock, 'STOCK.csv')
        df = pd.read_csv(filename,
                         sep=',',
                         set_lowmemory=False,
                         names=HEADER_STOCK,
                         header=None,index_col=None,
                         low_memory=False,
                         dtype=DTYPE_STOCK
                        )
        
    def moh_catogorize(self, float):
        '''mohの判定
        '''
        if float < 1:
            return 'a.1'
        elif float < 2:
            return 'b.2'
        else:
            return 'z.other'
        
    def caliculate_non_moving(self, df):
        '''nonmovingを計算する
        '''
        pass


def read_demand(HEADER_DEMAND, DTYPE_DEMAND, path_demand=path_demand_default):
    '''DEMANDの読み込み
    '''
    '''
    filename = os.path.join(path_demand, 'demand.csv')
    df = pd.read_csv(filename,
                     names=HEADER_DEMAND,
                     header=None,
                     index_col=None,
                     low_memory=False,
                     dtype= DTYPE_DEMAND
                    )
    '''
    pass

def read_purchase(HEADER_PURCHASE, DTYPE_PURCHASE, path_purchase=path_purchase_default):
    '''PURCHASEの読み込み.発注月列の追加と発注日のdatetime型への変換
    '''
    '''
    filename　= os.path.join(path_purchase, 'purchase.csv')
   
    df = pd.read_csv(filename,
                     names=HEADER_PURCHASE,
                     header=None,
                     index_col=None,
                     low_memory=False,
                     dtype= DTYPE_PURCHASE)

    df['日付 (発注月）'] = df['日付 (発注日）'].str[:6]
    df['日付 (発注日）'] = pd.to_datetime(df['日付 (発注日）'],format= '%Y%m%d')
    '''
    pass

def read_bmf_txt(HEADER_BMF, DTYPE_BMF, path_bmf= path_bmf_default, usecols=usecols_bmf_default):
    '''テキスト化したBMFを読みこむ
    '''
    '''
    filename = os.path.join(path_bmf, 'bmf.csv')
    df = pd.read_csv(filename,
                     usecols=usecols
                     low_memory=False,
                     dtype= DTYPE_BMF
                     )
    '''              
    pass

def read_scm_txt(HEADER_SCM, DTYPE_SCM, path_scm= path_scm_default, usecols=usecols_scm_default):
    '''テキスト化したscmを読みこむ
    '''
    '''
    filename = os.path.join(path_bmf, 'bmf.csv')
    df = pd.read_csv(filename,
                     usecols=usecols
                     low_memory=False,
                     dtype= DTYPE_BMF
                     )
    '''              
    pass

class Indicator:
    
    def __init__(self):
        print('Indicatorクラスからインスタンスが生成されました')
    
    def read_indicator(self, HEADER_INDICATOR, DTYPE_INDICATOR, path_indicator= path_indicator_default):
        '''INDICATORの読み込み
        '''
        '''
        filename = os.path.join(path_indicator,  'INDICATOR.csv')
        df = pd.read_csv(filaname,
                         names=HEADER_INDICATOR,
                         header=None,
                         index_col=None,
                         low_memory=False,
                         skiprows=1,
                         sep='\t',
                         dtype=DTYPE_INDICATOR
                        )
        '''
        pass
    
    def affiliate_name_indicator(self, df):
        '''アフィリエートネームをつける
        '''
        pass
    
    def pivot_indicator(self, df):
        '''INDICAOTRのpivot
        '''
        df_indicator_pivot =  pd.pivot_table(df, index='PARTNO', columns=df.Affiliatename, aggfunc={'MT':sum, 'RK':sum})

# TODO supply_rootをクラス化して読み込みと同時に最新データに更新
class SupplyRoot:
    
    def __init__(self, DTYPE_SUPPLY_ROOT, path=path_supply_root_default, usecols=usecols_supply_default):
        print('SupplyRootクラスからインスタンスが生成されました')
    
    def read_supply_root(self, DTYPE_SUPPLY_ROOT, path=path_supply_root_default, usecols= usecols_supply_default):
        '''supply_rootの読み込み
        '''
        filename = os.path.join(path, 'supply_root.csv')
        df = pd.read_csv(filename,
                         usecols=usecols,
                         low_memory=False,
                         dtype=DTYPE_SUPPLY_ROOT
                        )
        
    def newest_supply_root(self, df_list):
        '''supply_rootを最新のデータに更新
        '''
        # TODOリストを受け取り一意のデータを返す
        pass



def translate_affiliate_code(str):
    '''facコードの変換
    '''
    pass

def translate_fac_code(str):
    '''アフィリエイトコードの変換
    '''
    pass

def translate_depo_code(str):
    '''デポコードの変換
    '''
    pass

def summarize_affiliate_code(str):
    '''複数のaffiliateCodeを一つにまとめる
    '''
    pass
