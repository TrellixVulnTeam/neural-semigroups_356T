"""
   Copyright 2019-2022 Boris Shminke

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os

# pylint: disable-all
from unittest import TestCase

import torch

from neural_semigroups.constants import CURRENT_DEVICE, TEST_TEMP_DATA
from neural_semigroups.utils import (
    connect_to_db,
    create_table_if_not_exists,
    get_magma_by_index,
    import_smallsemi_format,
    insert_values_into_table,
    random_semigroup,
)


class TestUtils(TestCase):
    def setUp(self):
        torch.manual_seed(0)
        self.true_isomorphic_groups = torch.tensor(
            [
                [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]],
                [[1, 0, 3, 2], [0, 1, 2, 3], [3, 2, 1, 0], [2, 3, 0, 1]],
                [[2, 3, 0, 1], [3, 2, 1, 0], [0, 1, 2, 3], [1, 0, 3, 2]],
                [[3, 2, 1, 0], [2, 3, 0, 1], [1, 0, 3, 2], [0, 1, 2, 3]],
            ]
        ).to(CURRENT_DEVICE)

    def test_random_semigroup(self):
        success, cayley_table = random_semigroup(2, 1)
        self.assertTrue(success)
        self.assertEqual(cayley_table.shape, torch.Size([2, 2]))

    def test_get_magma_by_index(self):
        self.assertTrue(
            torch.allclose(
                get_magma_by_index(2, 0).cayley_table,
                torch.tensor([[0, 0], [0, 0]]),
            )
        )
        self.assertTrue(
            torch.allclose(
                get_magma_by_index(2, 15).cayley_table,
                torch.tensor([[1, 1], [1, 1]]),
            )
        )
        self.assertTrue(
            torch.allclose(
                get_magma_by_index(2, 7).cayley_table,
                torch.tensor([[0, 1], [1, 1]]),
            )
        )
        with self.assertRaises(ValueError):
            get_magma_by_index(3, -1)
        with self.assertRaises(ValueError):
            get_magma_by_index(3, 20000)

    def test_import_smallsemi_format(self):
        lines = ["# header", "0100\n", "0101\n", "0011\n"]
        semigroups = import_smallsemi_format(lines)
        self.assertIsInstance(semigroups, torch.Tensor)
        self.assertEqual(semigroups.shape[0], 4)
        true_semigroups = [
            [[0, 0], [0, 0]],
            [[0, 1], [1, 0]],
            [[0, 0], [0, 1]],
            [[0, 0], [1, 1]],
        ]
        for i in range(4):
            self.assertIsInstance(semigroups[i], torch.Tensor)
            self.assertTrue(
                torch.allclose(semigroups[i], torch.tensor(true_semigroups[i]))
            )

    def test_create_table_if_not_exists(self):
        db_name = os.path.join(TEST_TEMP_DATA, "test.db")
        if os.path.exists(db_name):
            os.remove(db_name)
        cursor = connect_to_db(db_name)
        create_table_if_not_exists(
            cursor,
            "test_table",
            ["test1 INT, test2 INT, test3 STRING"],
        )
        insert_values_into_table(cursor, "test_table", (1, 2, "three"))
        cursor.execute(
            "SELECT sql FROM sqlite_master WHERE name = 'test_table'"
        )
        self.assertEqual(
            cursor.fetchone()[0],
            "CREATE TABLE test_table(test1 INT, test2 INT, test3 STRING)",
        )
        cursor.execute("SELECT test1, test2, test3 FROM test_table")
        self.assertEqual(cursor.fetchone(), (1, 2, "three"))
        cursor.connection.close()
