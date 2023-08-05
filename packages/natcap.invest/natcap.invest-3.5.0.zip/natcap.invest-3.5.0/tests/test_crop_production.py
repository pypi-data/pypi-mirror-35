"""Module for Regression Testing the InVEST Crop Production models."""
import unittest
import tempfile
import shutil
import os

import pandas
import numpy
from pygeoprocessing.testing import scm

MODEL_DATA_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'invest-data',
    'CropProduction', 'model_data')
SAMPLE_DATA_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'invest-data',
    'CropProduction', 'sample_user_data')
TEST_DATA_PATH = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'invest-test-data',
    'crop_production_model')


class CropProductionTests(unittest.TestCase):
    """Tests for the Crop Production model."""

    def setUp(self):
        """Overriding setUp function to create temp workspace directory."""
        # this lets us delete the workspace after its done no matter the
        # the rest result
        self.workspace_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Overriding tearDown function to remove temporary directory."""
        shutil.rmtree(self.workspace_dir)

    @scm.skip_if_data_missing(SAMPLE_DATA_PATH)
    @scm.skip_if_data_missing(MODEL_DATA_PATH)
    def test_crop_production_percentile(self):
        """Crop Production: test crop production percentile regression."""
        from natcap.invest import crop_production_percentile

        args = {
            'workspace_dir': self.workspace_dir,
            'results_suffix': '',
            'landcover_raster_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover.tif'),
            'landcover_to_crop_table_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover_to_crop_table.csv'),
            'aggregate_polygon_path': os.path.join(
                SAMPLE_DATA_PATH, 'aggregate_shape.shp'),
            'aggregate_polygon_id': 'id',
            'model_data_path': MODEL_DATA_PATH
        }
        crop_production_percentile.execute(args)

        result_table_path = os.path.join(
            args['workspace_dir'], 'aggregate_results.csv')
        expected_result_table_path = os.path.join(
            TEST_DATA_PATH, 'expected_aggregate_results.csv')
        expected_result_table = pandas.read_csv(
            expected_result_table_path)
        result_table = pandas.read_csv(
            result_table_path)
        pandas.testing.assert_frame_equal(
            expected_result_table, result_table, check_dtype=False)

    @scm.skip_if_data_missing(SAMPLE_DATA_PATH)
    @scm.skip_if_data_missing(MODEL_DATA_PATH)
    def test_crop_production_percentile_bad_crop(self):
        """Crop Production: test crop production with a bad crop name."""
        from natcap.invest import crop_production_percentile

        args = {
            'workspace_dir': self.workspace_dir,
            'results_suffix': '',
            'landcover_raster_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover.tif'),
            'landcover_to_crop_table_path': os.path.join(
                self.workspace_dir, 'landcover_to_badcrop_table.csv'),
            'aggregate_polygon_path': os.path.join(
                SAMPLE_DATA_PATH, 'aggregate_shape.shp'),
            'aggregate_polygon_id': 'id',
            'model_data_path': MODEL_DATA_PATH
        }

        with open(args['landcover_to_crop_table_path'],
                  'wb') as landcover_crop_table:
            landcover_crop_table.write(
                'crop_name,lucode\nfakecrop,20\n')

        with self.assertRaises(ValueError):
            crop_production_percentile.execute(args)

    @scm.skip_if_data_missing(SAMPLE_DATA_PATH)
    @scm.skip_if_data_missing(MODEL_DATA_PATH)
    def test_crop_production_regression_bad_crop(self):
        """Crop Production: test crop regression with a bad crop name."""
        from natcap.invest import crop_production_regression

        args = {
            'workspace_dir': self.workspace_dir,
            'results_suffix': '',
            'landcover_raster_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover.tif'),
            'landcover_to_crop_table_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover_to_badcrop_table.csv'),
            'aggregate_polygon_path': os.path.join(
                SAMPLE_DATA_PATH, 'aggregate_shape.shp'),
            'aggregate_polygon_id': 'id',
            'model_data_path': MODEL_DATA_PATH,
            'fertilization_rate_table_path': os.path.join(
                SAMPLE_DATA_PATH, 'crop_fertilization_rates.csv'),
            'nitrogen_fertilization_rate': 29.6,
            'phosphorous_fertilization_rate': 8.4,
            'potassium_fertilization_rate': 14.2,
        }

        with open(args['landcover_to_crop_table_path'],
                  'wb') as landcover_crop_table:
            landcover_crop_table.write(
                'crop_name,lucode\nfakecrop,20\n')

        with self.assertRaises(ValueError):
            crop_production_regression.execute(args)

    @scm.skip_if_data_missing(SAMPLE_DATA_PATH)
    @scm.skip_if_data_missing(MODEL_DATA_PATH)
    def test_crop_production_regression(self):
        """Crop Production: test crop production regression model."""
        from natcap.invest import crop_production_regression

        args = {
            'workspace_dir': self.workspace_dir,
            'results_suffix': '',
            'landcover_raster_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover.tif'),
            'landcover_to_crop_table_path': os.path.join(
                SAMPLE_DATA_PATH, 'landcover_to_crop_table.csv'),
            'aggregate_polygon_path': os.path.join(
                SAMPLE_DATA_PATH, 'aggregate_shape.shp'),
            'aggregate_polygon_id': 'id',
            'model_data_path': MODEL_DATA_PATH,
            'fertilization_rate_table_path': os.path.join(
                SAMPLE_DATA_PATH, 'crop_fertilization_rates.csv'),
            'nitrogen_fertilization_rate': 29.6,
            'phosphorous_fertilization_rate': 8.4,
            'potassium_fertilization_rate': 14.2,
        }
        crop_production_regression.execute(args)

        result_table_path = os.path.join(
            args['workspace_dir'], 'aggregate_results.csv')
        expected_result_table_path = os.path.join(
            TEST_DATA_PATH, 'expected_regression_aggregate_results.csv')
        expected_result_table = pandas.read_csv(
            expected_result_table_path)
        result_table = pandas.read_csv(
            result_table_path)
        pandas.testing.assert_frame_equal(
            expected_result_table, result_table, check_dtype=False)
