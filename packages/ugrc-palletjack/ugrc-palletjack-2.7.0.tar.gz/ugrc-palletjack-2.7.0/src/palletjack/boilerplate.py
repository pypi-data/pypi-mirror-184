import logging

import arcgis
import numpy as np
import pandas as pd
from arcgis import GeoAccessor, GeoSeriesAccessor

import palletjack

logging.basicConfig(level=logging.DEBUG)

gis = arcgis.gis.GIS(username='Jake.Adams@UtahAGRC')


def test_adds(gis):
    new_poly = arcgis.geometry.Polygon({
        'rings': [[[-128, 37], [-127, 37], [-127, 36], [-128, 36]]],
        'spatialReference': {
            "wkid": 4326
        }
    })

    new_dataframe = pd.DataFrame({
        'state_name': ['newqsuare'],
        'state_fips': ['98'],
        'state_abbr': ['ns'],
        # 'nc2': ['bar'],
        # 'OBJECTID': [100],
        'SHAPE': [new_poly.JSON]
    })

    new_spatial_df = pd.DataFrame.spatial.from_df(new_dataframe, geometry_column='SHAPE')
    print(new_spatial_df.spatial.validate())

    updates = palletjack.load.FeatureServiceUpdater.add_features(
        gis, 'de73df9e253f4836a34c40e0dd986618', new_spatial_df
    )

    logging.info('number of features added:')
    logging.info(updates)

    # updater = palletjack.load.FeatureServiceUpdater(
    #     gis, 'de73df9e253f4836a34c40e0dd986618', new_spatial_df, fields=list(new_dataframe.columns)
    # )

    # adds = updater.add_new_data_to_hosted_feature_layer()


def test_updates_no_geometry(gis):
    new_dataframe = pd.DataFrame({
        'state_name': ['Old Square'],
        'state_abbr': ['xy'],
        'state_fips': ['42'],
        # 'nc2': ['bar'],
        'OBJECTID': [52],
    })

    updates = palletjack.load.FeatureServiceUpdater.update_features(
        gis,
        'de73df9e253f4836a34c40e0dd986618',
        new_dataframe,
        update_geometry=False
        # fields=['state_name', 'state_abbr', 'OBJECTID']
    )

    logging.info('number of features updated:')
    logging.info(updates)


def test_updates_geometry(gis):
    new_poly = arcgis.geometry.Polygon({
        'rings': [[[-129, 37], [-127, 37], [-127, 36], [-129, 36]]],
        'spatialReference': {
            "wkid": 4326
        }
    })
    new_dataframe = pd.DataFrame({
        'state_name': ['New Square'],
        'state_fips': ['98'],
        'state_abbr': ['za'],
        # 'nc2': ['bar'],
        'OBJECTID': [53],
        'SHAPE': [new_poly.JSON]
    })

    updates = palletjack.load.FeatureServiceUpdater.update_features(
        gis,
        'de73df9e253f4836a34c40e0dd986618',
        new_dataframe,
        # fields=['state_name', 'state_abbr', 'OBJECTID', 'SHAPE']
    )

    logging.info('number of features updated:')
    logging.info(updates)


def test_deletes(gis):

    updates = palletjack.load.FeatureServiceUpdater.remove_features(gis, 'de73df9e253f4836a34c40e0dd986618', '6,11,12')

    logging.info('number of features deleted:')
    logging.info(updates)


def test_truncate_and_load(gis):

    new_data = pd.DataFrame.spatial.from_featureclass(r'C:\gis\Projects\FastData\FastData.gdb\upsert_test_edits2')

    updates = palletjack.load.FeatureServiceUpdater.truncate_and_load_features(
        gis, 'de73df9e253f4836a34c40e0dd986618', new_data, 'd:\temp'
    )

    logging.info('number of features loaded:')
    logging.info(updates)


def big_tnl(gis):

    #: This fails on both the load and reload because of an exception 'The page was not displayed because the request entity is too large.'. This occurs after a few minutes of constant 50k up and down and then a burst that looks to be the entire big dataset (sys.getsizeof(kwargs['edits']) -> 1214020985). Live data remains empty due to earlier truncate.

    logging.info('Loading parcels...')
    new_data = pd.DataFrame.spatial.from_featureclass(r'C:\gis\Projects\FastData\FastData.gdb\slco_lir_20221229_3857')
    new_data['built_yr'].fillna(0, inplace=True)
    new_data['effbuilt_yr'].fillna(0, inplace=True)
    new_data['built_yr'] = new_data['built_yr'].astype('int16')
    new_data['effbuilt_yr'] = new_data['effbuilt_yr'].astype('int16')

    updates = palletjack.load.FeatureServiceUpdater.truncate_and_load_features(
        gis, 'f1d7b3e86b8d4ee6bc6e1d7d636f1adb', new_data, r'd:\temp'
    )

    logging.info('number of features loaded:')
    logging.info(updates)


# test_adds(gis)

# test_updates_no_geometry(gis)
# test_updates_geometry(gis)

# test_deletes(gis)

# test_truncate_and_load(gis)

big_tnl(gis)

#: TODO: size is working at 10mb size limit (100 and 50 didn't work) but now I'm getting {"layerName":"slco_lir_20221229","submissionTime":1672793254217,"lastUpdatedTime":1672793264930,"recordCount":0,"status":"Failed","error":{"code":500,"description":"Input string was not in a correct format.Couldn't store \u003c\u003e in parcel_acres Column.  Expected type is Double."}} errors (huh?)
