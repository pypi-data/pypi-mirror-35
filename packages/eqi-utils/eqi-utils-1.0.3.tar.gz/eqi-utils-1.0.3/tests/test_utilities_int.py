import os
import unittest

import pandas as pd

from eqi_utils.config import config
from eqi_utils.data import bundle
from eqi_utils.data import dbview
from eqi_utils.data import view
from eqi_utils.utils.ResourceUtils import get_resource_filename


def _create_test_df():
    return pd.DataFrame({'A': ['a', 'b', 'a', 'c'] * 6,
                         'B': ['d', 'e', 'a'] * 8, })


class EQITestBase(unittest.TestCase):
    """
    Integration Test Base Class. Please set up the ./resource/config.ini
    accordingly to run the tests in this file.
    """
    def setUp(self):
        os.environ['EQI_HOME'] = get_resource_filename(__name__,
                                                       'resource',
                                                       '')
        config.reload_config()
        bundle.reload_inventory()

    def tearDown(self):
        os.unsetenv('EQI_HOME')


class TestBundle(EQITestBase):
    def test_list_bundle(self):
        bundles = bundle.get_bundles()
        self.assertTrue('testbundle' in bundles)

    def test_load_df(self):
        df = bundle.load_to_df('testbundle', 'Categories')
        self.assertTrue(len(df) > 0)

    def test_get_bucket_name(self):
        bucket_name = bundle.get_bucket_name(bundle.get_bundles()[0])
        self.assertTrue(bucket_name)

    def test_get_datafile_location(self):
        bundle_ = bundle.get_bundles()[0]
        datafile = bundle.get_datafiles(bundle_)[0]
        self.assertTrue(bundle.get_datafile_location(bundle_, datafile))

    def test_get_datafile_desc(self):
        bundle_ = bundle.get_bundles()[0]
        self.assertTrue(bundle.get_datafile_desc(bundle_))

    def test_list_datafile(self):
        bundle_ = bundle.get_bundles()[0]
        self.assertGreater(len(bundle.get_datafiles(bundle_)), 0)

    def test_load_to_df(self):
        bundle_ = bundle.get_bundles()[0]
        datafile = bundle.get_datafiles(bundle_)[0]
        df = bundle.load_to_df(bundle_, datafile)
        self.assertGreater(len(df), 0)


class TestView(EQITestBase):

    def test_save_view_remote(self):
        df = _create_test_df()
        view_name = 'sp500_symbols'
        view.save_view(df, view_name, desc='SP 500 symbol', remote=True)
        views = view.get_views(remote=True)
        self.assertTrue(view_name in views)

    def test_save_view_local(self):
        df = _create_test_df()
        view_name = 'sp500_symbols_local'
        view.save_view(df, view_name, desc='SP 500 symbol')
        views = view.get_views()
        self.assertTrue(view_name in views)

    def test_delete_view_local(self):
        df = _create_test_df()
        test_view = 'test_view'
        view.save_view(df, test_view, desc='SP 500 symbol')
        views = view.get_views()
        self.assertTrue(test_view in views)
        view.delete_view(test_view)
        views = view.get_views()
        self.assertTrue(test_view not in views)

    def test_delete_view_remote(self):
        df = _create_test_df()
        view_name = 'test_view_remote'
        view.save_view(df, view_name, desc='SP 500 symbol',
                       remote=True)
        views = view.get_views(remote=True)
        self.assertTrue(view_name in views)
        view.delete_view(view_name, remote=True)
        views = view.get_views(remote=True)
        self.assertTrue(view_name not in views)

    def test_load_to_df_self_remote(self):
        df = _create_test_df()
        view_name = 'test_load_df_view_self_remote'
        view.save_view(df, view_name,
                       desc='SP 500 symbol',
                       remote=True)
        df_remote = view.load_to_df(view_name,
                                    remote=True)
        self.assertGreater(len(df_remote), 0)

    def test_load_to_df_self_local(self):
        df = _create_test_df()
        view_name = 'test_load_df_view_self_local'
        view.save_view(df, view_name,
                       desc='SP 500 symbol')
        df_local = view.load_to_df(view_name)
        self.assertGreater(len(df_local), 0)

    def test_load_to_df_others_remote(self):
        df_remote = view.load_to_df('sp_500_symbol2', user='test-user',
                                    remote=True)
        self.assertGreater(len(df_remote), 0)

    def test_load_to_df_others_local(self):
        view_name = 'sp_500_symbol2'
        view.load_to_df(view_name, user='test-user', remote=True)
        df_local = view.load_to_df('sp_500_symbol2', user='test-user')
        self.assertGreater(len(df_local), 0)


class TestDbview(EQITestBase):
    def test_load_to_df(self):
        top100_price = r'select * from quantprod.tqa_price where rownum <= 100'
        df = dbview.load_to_df(top100_price)
        self.assertGreater(len(df), 0)


if __name__ == '__main__':
    unittest.main()
