from datetime import datetime

import alphalens
import pandas as pd

from eqi_utils.data import view
from . import entity
from . import refdata
from .entity import access


def _is_freq_day(df):
    freq = df.index.get_level_values('date').freq
    return freq is not None and freq.freqstr in {'B', 'C', 'D'}


def _to_daily(df):
    if not _is_freq_day(df):
        df = df.groupby(level=[1]).apply(
            lambda df_: df_.to_eqi().e_drop_level('asset').resample(
                'D').bfill().to_pandas()).swaplevel(0, 1).sort_index()
    return df


class Factor:
    """Timeseries factor indexed by asset and date."""

    def __init__(self, df, ticker_type, name):
        """
        Construct a new Factor
        :param df: factor DataFrame, which must meet the requirements: \
                - index exactly as ['date', 'asset']
                - no duplicated index
                - exactly one factor column, with any string name
        :param ticker_type: the ticker type of the asset, e.g. 'RIC' \
                            this will be used for various later stage refdata
                            fetching, e.g. price
        :param name: name of the factor
        """
        self.raw_df = df
        self.name = name
        self.ticker_type = ticker_type
        self._check_factor_index()
        self._check_dup_index()
        self._check_column_name()
        self.meta = self._get_meta()
        self.raw_df.sort_index()

    @staticmethod
    def from_registry(name):
        """
        Load an existing factor from database matching a given name
        :param name: factor name
        :return: existing Factor
        """
        factor = entity.access.get_factor(name)
        df = entity.access.load_to_df(name)
        return Factor(df, factor.ticker_type, factor.name)

    @staticmethod
    def list_registry():
        """
        List all factors from registry
        """
        entity.access.list_factors()

    @staticmethod
    def delete_from_registry(name):
        """
        Delete factor with a specific name from registry
        :param name:
        :return:
        """
        factor = entity.access.find_factors(name=name)
        if len(factor) == 1:
            factor = factor[0]
            entity.access.delete_factor(factor)
            view.delete_view(factor.name, remote=True)
        elif len(factor) == 0:
            raise ValueError("No factor found by name {}".format(name))
        else:
            raise ValueError("Too many results found by name {}".format(name))

    @staticmethod
    def search_registry(**kwargs):
        """
        Search for factors in the registry matching a criteria
        :param kwargs: field=value, e.g. name='my_factor'
        :return: a list of factors found
        """
        entity.access.list_factors(entity.access.find_factors(**kwargs))

    def upload_to_registry(self, desc):
        """
        Upload this factor to registry
        :param desc: factory description
        """
        view.save_view(self.raw_df, self.name, desc=desc, remote=True)
        eqifactor = entity.entity.EQIFactor(name=self.name, path=self.name,
                                            location='S3',
                                            ticker_type=self.ticker_type,
                                            owner=view.DEFAULT_USER,
                                            description=desc,
                                            creation_ts=datetime.now(),
                                            last_modified_ts=datetime.now())
        access.save_factor(eqifactor)

    def to_pop(self):
        pass

    def _get_meta(self):
        return {
            'min_date': self.raw_df.index.get_level_values(
                'date').min().strftime('%d-%b-%Y'),
            'max_date': self.raw_df.index.get_level_values(
                'date').max().strftime('%d-%b-%Y'),
            'tickers': self.raw_df.index.get_level_values(
                'asset').unique().values.tolist()
        }

    def _check_factor_index(self):
        names = self.raw_df.to_eqi().e_index_names()
        if names != ['date', 'asset']:
            raise AttributeError(
                "Expect factor raw DataFrame to have"
                "exact indexes like ['date, 'asset'], not {}, {}".format(
                    names[0], names[1]))

    def _check_dup_index(self):
        if self.raw_df.to_eqi().e_has_dup_index():
            raise AttributeError(
                "Factor raw DataFrame has duplicate index, "
                "please remove")

    def _check_column_name(self):
        if len(self.raw_df.columns) != 1:
            raise AttributeError(
                "Factor needs to contain exactly one value column, "
                "please adjust")
        self.raw_df = self.raw_df.rename(columns=lambda c: str(c))


class CategorizedFactor(Factor):
    """Factor with category information."""

    def __init__(self, categorized_df, ticker_type, name,
                 category_map=None):
        """
        Construct a new CategorizedFactor
        :param categorized_df: input DataFrame, which must meet requirements: \
                            - index exactly as ['date', 'asset', 'category']
                            - no duplicate index
                            - exactly one factor column, with string name
        :param ticker_type: the ticker type of the asset, e.g. 'RIC' \
                            this will be used for various later stage refdata
                            fetching, e.g. price
        :param name: factor name
        :param category_map: category id -> name map, optional
        """
        self.categorized_factor = categorized_df.to_eqi()
        self._check_category_df()
        combined_factor = categorized_df.groupby(level=['date', 'asset']).sum()
        super(CategorizedFactor, self).__init__(combined_factor, ticker_type,
                                                name)
        self.meta['categories'] = self.categorized_factor.e_to_set('category')
        self.meta['category_map'] = category_map

    def _check_category_df(self):
        names = self.categorized_factor.e_index_names()
        if names != ['date', 'asset', 'category']:
            raise AttributeError("Expect factor raw DataFrame to have exact "
                                 "indexes as ['date, 'asset', 'category']")

    @staticmethod
    def from_registry(name):
        factor = entity.access.get_factor(name)
        df = entity.access.load_to_df(name)
        return CategorizedFactor(df, factor.category_col_name,
                                 factor.ticker_type,
                                 factor.name)

    def iteritems(self):
        return ((x, self.categorized_factor.to_eqi().e_is('category',
                                                          x).e_drop_level(
            'category').to_pandas())
                for x in self.meta['categories'])


class Portfolio:
    """Timeseries asset holdings"""

    def __init__(self, factor):
        """
        Construct a Portfolio
        :param factor: Factor used as asset weighting
        """
        self._factor = factor
        self.price = None
        self.alphalens_factor = None
        self.alphalens_factors = None

    def publish_result(self):
        pass

    def join_price(self, price_type='return_index'):
        """
        Fetch the price data for portfolio holdings
        :param price_type: type of price, e.g. 'return_index'
        """
        self.price = refdata.fetch_price(self._factor.meta['tickers'],
                                         self._factor.meta['min_date'],
                                         self._factor.meta['max_date'],
                                         price_type
                                         )

    @staticmethod
    def _to_factor_with_return(df, price, resample_period='',
                               quantile=3,
                               forward_periods=('30D', '90D', '150D'),
                               max_loss=1,
                               **kwargs):
        clean_binning = False if resample_period else True
        alphalens_factor = \
            alphalens.utils.get_clean_factor_and_forward_returns(
                df,
                price, quantiles=quantile, max_loss=max_loss,
                periods=forward_periods, clean_binning=clean_binning, **kwargs)
        if resample_period:
            alphalens_factor = Portfolio.resample(alphalens_factor,
                                                  resample_period)
            alphalens_factor = Portfolio.recompute_quantile(alphalens_factor,
                                                            quantile=quantile)
        return alphalens_factor.sort_index()

    def to_alphalens_factor(self, resample_period='', quantile=3,
                            forward_periods=('30D', '90D', '150D'), max_loss=1,
                            **kwargs):
        """
        Convert Factor into AlphaLens format (joined with forward return and \
        quantile)
        :param resample_period: {'month_start', 'month_end', ''}
        :param quantile: quantile to bin factor data
        :param forward_periods: period used to calculate forward return
        :param max_loss: max data loss allowed during computation
        :param kwargs: additional AlphaLens kwargs
        """
        if self.price is None:
            raise AttributeError(
                "Price data has to be fetched first, "
                "please call portfolio.join_price()")
        self.alphalens_factor = Portfolio._to_factor_with_return(
            self._factor.raw_df,
            self.price, resample_period=resample_period, quantile=quantile,
            max_loss=max_loss,
            forward_periods=forward_periods, **kwargs
        )

        if isinstance(self._factor, CategorizedFactor):
            alphalens_factors = {}
            for category, factor_by_category in self._factor.iteritems():
                print(factor_by_category.head())
                alphalens_factors[
                    category] = Portfolio._to_factor_with_return(
                    factor_by_category,
                    self.price, resample_period=resample_period,
                    quantile=quantile, max_loss=max_loss,
                    forward_periods=forward_periods, **kwargs
                )
            self.alphalens_factors = alphalens_factors

    def analyze_by_alphalens(self, *args, **kwargs):
        """
        Analyze the Portfolio performance with AlphaLens
        :param args: additional AlphaLens positional args
        :param kwargs: additional AlphaLens kwargs
        """
        if self.alphalens_factor is None:
            raise AttributeError(
                "Alphalens factor needs to be computed first,"
                " please call portfolio.to_alphalens_factor()")
        is_by_group = 'group_by' in kwargs
        if isinstance(self._factor, CategorizedFactor):
            alphalens.tears.create_full_tear_sheet_by_categories(
                self.alphalens_factor,
                self.alphalens_factors,
                by_group=is_by_group,
                category_map=self._factor.meta['category_map'], *args,
                **kwargs)
        else:
            alphalens.tears.create_full_tear_sheet(self.alphalens_factor,
                                                   by_group=is_by_group, *args,
                                                   **kwargs)

    @staticmethod
    def to_month_end(df):
        return df.unstack(1).resample(
            'M').last().fillna(0).stack(1)

    @staticmethod
    def to_month_start(df):
        return df.unstack(1).resample(
            'MS').first().fillna(0).stack(1)

    @staticmethod
    def resample(df, period='month_end'):
        if period == 'month_end':
            return Portfolio.to_month_end(df)
        elif period == 'month_start':
            return Portfolio.to_month_start(df)
        else:
            raise AttributeError(
                'Period {} cannot be recognized'.format(period))

    @staticmethod
    def recompute_quantile(df, quantile=5, by_group=False):
        def _to_quantile(df_, quantile_):
            return pd.qcut(df_.rank(method='first'),
                           quantile_,
                           labels=False) + 1

        grouper = [df.index.get_level_values('date')]
        if by_group:
            grouper.append('group')

        factor_quantile = df.groupby(grouper)['factor'] \
            .apply(_to_quantile, quantile)
        df['factor_quantile'] = factor_quantile
        return df
