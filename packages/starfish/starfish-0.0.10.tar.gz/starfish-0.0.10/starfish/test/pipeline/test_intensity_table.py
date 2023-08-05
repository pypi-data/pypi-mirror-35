from typing import Tuple

import numpy as np
import pandas as pd

from starfish.constants import Indices, Features
from starfish.intensity_table import IntensityTable
from starfish.codebook import Codebook
from starfish.stack import ImageStack
from starfish.spots._detector.combine_adjacent_features import combine_adjacent_features
# don't inspect pytest fixtures in pycharm
# noinspection PyUnresolvedReferences
from starfish.test.dataset_fixtures import (
    loaded_codebook, simple_codebook_json, simple_codebook_array, single_synthetic_spot)


def make_empty_intensity_table(image_shape=(2, 4, 3)):
    x = [1, 2]
    y = [2, 3]
    z = [1, 1]
    r = [1, 1]
    spot_attributes = pd.MultiIndex.from_arrays(
        [x, y, z, r],
        names=(Features.X, Features.Y, Features.Z, Features.SPOT_RADIUS))
    empty = IntensityTable.empty_intensity_table(spot_attributes, 2, 2, image_shape)
    return empty, spot_attributes


def test_empty_intensity_table():
    image_shape = (2, 4, 3)
    empty, spot_attributes = make_empty_intensity_table(image_shape=image_shape)
    empty = IntensityTable.empty_intensity_table(spot_attributes, 2, 2, image_shape)
    assert empty.shape == (2, 2, 2)
    assert np.sum(empty.values) == 0


def test_synthetic_intensities_generates_correct_number_of_features(loaded_codebook):
    n_spots = 2
    intensities = IntensityTable.synthetic_intensities(loaded_codebook, n_spots=n_spots)
    assert isinstance(intensities, IntensityTable)

    # shape should have n_spots and channels and imaging rounds equal to the codebook's shape
    assert intensities.shape == (n_spots, *loaded_codebook.shape[1:])


def test_synthetic_intensities_have_correct_number_of_on_features(loaded_codebook):
    n_spots = 2
    intensities = IntensityTable.synthetic_intensities(loaded_codebook, n_spots=n_spots)
    on_features = np.sum(intensities.values != 0)
    # this asserts that the number of features "on" in intensities should be equal to the
    # number of "on" features in the codewords, times the total number of spots in intensities.
    num_on = loaded_codebook.sum((Indices.CH.value, Indices.ROUND.value)).values.mean() * n_spots
    assert on_features == num_on


def feature_data() -> Tuple[Codebook, ImageStack]:
    # This codebook has two codes: on/off and on/on
    # This array has 3 spots: one on/off, one on/on, and one off/on
    # They exist in the first and second z-slice, but not the third.
    code_array = [
        {
            # on/off
            Features.CODEWORD: [
                {Indices.ROUND.value: 0, Indices.CH.value: 0, Features.CODE_VALUE: 1},
            ],
            Features.TARGET: "gene_1"
        },
        {
            # on/on
            Features.CODEWORD: [
                {Indices.ROUND.value: 0, Indices.CH.value: 0, Features.CODE_VALUE: 1},
                {Indices.ROUND.value: 1, Indices.CH.value: 0, Features.CODE_VALUE: 1},
            ],
            Features.TARGET: "gene_2"
        }
    ]
    codebook = Codebook.from_code_array(code_array)

    data = np.array(
        [[[[1, 1, 0, 1],  # round 0
           [1, 1, 0, 1],
           [0, 0, 0, 0]],

          [[1, 1, 0, 1],
           [1, 1, 0, 1],
           [0, 0, 0, 0]],

          [[0, 0, 0, 1],
           [0, 0, 0, 1],
           [0, 0, 0, 0]]],

         [[[1, 1, 0, 0],  # round 1
           [1, 1, 0, 0],
           [0, 0, 0, 1]],

          [[1, 1, 0, 0],
           [1, 1, 0, 0],
           [0, 0, 0, 1]],

          [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 1]]]]
    )
    data = data.reshape(2, 1, 3, 3, 4)
    image = ImageStack.from_numpy_array(data)
    return codebook, image


def test_combine_adjacent_features():
    codebook, image = feature_data()
    new_intensities = IntensityTable.from_image_stack(image)

    # TODO ambrosejcarr: this decoder is dropping pixels that don't decode. Desirable?
    new_intensities = codebook.metric_decode(
        new_intensities,
        max_distance=0.5,
        min_intensity=0.5,
        norm_order=2
    )

    # this is "working", with the caveat that the z-coord is a bit weird and potentially wrong.
    combined_intensities, _ = combine_adjacent_features(new_intensities, min_area=0, max_area=10)

    assert np.array_equal(combined_intensities.shape, (2, 1, 2))
    assert np.array_equal(
        combined_intensities[Features.AXIS][Features.TARGET],
        ['gene_2', 'gene_1']
    )


def test_intensity_table_to_dataframe():
    table, _ = make_empty_intensity_table()
    table_df = table.to_dataframe()
    assert np.array_equal(table_df[Features.X], table.coords[Features.X].values)
    assert np.array_equal(table_df[Features.Y], table.coords[Features.Y].values)
    assert np.array_equal(table_df[Features.Z], table.coords[Features.Z].values)
    assert np.array_equal(table_df[Features.SPOT_RADIUS], table.coords[Features.SPOT_RADIUS].values)
    assert np.array_equal(
        table_df.columns,
        [Features.X, Features.Y, Features.Z, Features.SPOT_RADIUS]
    )
