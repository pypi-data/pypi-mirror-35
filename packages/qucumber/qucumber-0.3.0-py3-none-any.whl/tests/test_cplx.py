# Copyright 2018 PIQuIL - All Rights Reserved

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import unittest

import numpy as np
import torch

from qucumber.utils import cplx


class TestCplx(unittest.TestCase):
    def assertTensorsEqual(self, a, b, msg=None):
        self.assertTrue(torch.equal(a, b), msg=msg)

    def assertTensorsAlmostEqual(self, a, b, tol=1e-7, msg=None):
        self.assertTrue(((a - b).abs() <= tol).all(), msg=msg)

    def test_make_complex_vector(self):
        x = torch.tensor([1, 2, 3, 4])
        y = torch.tensor([5, 6, 7, 8])
        z = cplx.make_complex(x, y)

        expect = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])

        self.assertTensorsEqual(expect, z, msg="Make Complex Vector failed!")

    def test_make_complex_vector_with_zero_imaginary_part(self):
        x = torch.tensor([1, 2, 3, 4])
        z = cplx.make_complex(x)

        expect = torch.tensor([[1, 2, 3, 4], [0, 0, 0, 0]])

        self.assertTensorsEqual(
            expect, z, msg="Making a complex vector with zero imaginary part failed!"
        )

    def test_make_complex_matrix(self):
        x = torch.tensor([[1, 2], [3, 4]])
        y = torch.tensor([[5, 6], [7, 8]])
        z = cplx.make_complex(x, y)

        expect = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

        self.assertTensorsEqual(expect, z, msg="Make Complex Matrix failed!")

    def test_bad_complex_matrix(self):
        with self.assertRaises(RuntimeError):
            x = torch.tensor([[1, 2, 3]])
            y = torch.tensor([[4, 5, 6, 7]])
            return cplx.make_complex(x, y)

    def test_elementwise_mult(self):
        z1 = torch.tensor([[2, 3, 5], [6, 7, 2]], dtype=torch.double)
        z2 = torch.tensor([[1, 2, 2], [3, 4, 8]], dtype=torch.double)

        expect = torch.tensor([[-16, -22, -6], [12, 26, 44]], dtype=torch.double)

        self.assertTensorsEqual(
            cplx.elementwise_mult(z1, z2),
            expect,
            msg="Elementwise multiplication failed!",
        )

    def test_elementwise_div(self):
        z1 = torch.tensor([[2, 3, 5], [6, 7, 2]], dtype=torch.double)
        z2 = torch.tensor([[1, 2, 2], [3, 4, 8]], dtype=torch.double)

        expect = torch.tensor(
            [[2, (17 / 10), (13 / 34)], [0, (1 / 10), (-9 / 17)]], dtype=torch.double
        )

        self.assertTensorsAlmostEqual(
            cplx.elementwise_division(z1, z2),
            expect,
            msg="Elementwise division failed!",
        )

    def test_elementwise_div_fail(self):
        with self.assertRaises(ValueError):
            z1 = torch.tensor([[2, 3], [6, 7]], dtype=torch.double)
            z2 = torch.tensor([[1, 2, 2], [3, 4, 8]], dtype=torch.double)
            return cplx.elementwise_division(z1, z2)

    def test_scalar_vector_mult(self):
        scalar = torch.tensor([2, 3], dtype=torch.double)
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)

        expect = torch.tensor([[-7, -8], [9, 14]], dtype=torch.double)

        self.assertTensorsEqual(
            cplx.scalar_mult(scalar, vector),
            expect,
            msg="Scalar * Vector multiplication failed!",
        )

    def test_scalar_matrix_mult(self):
        scalar = torch.tensor([2, 3])
        matrix = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

        expect = torch.tensor([[[-13, -14], [-15, -16]], [[13, 18], [23, 28]]])

        self.assertTensorsEqual(
            cplx.scalar_mult(scalar, matrix),
            expect,
            msg="Scalar * Matrix multiplication failed!",
        )

    def test_scalar_mult_overwrite(self):
        scalar = torch.tensor([2, 3], dtype=torch.double)
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)
        out = torch.zeros_like(vector)
        expect = torch.tensor([[-7, -8], [9, 14]], dtype=torch.double)

        cplx.scalar_mult(scalar, vector, out=out)

        self.assertTensorsEqual(
            out,
            expect,
            msg="Scalar * Vector multiplication with 'out' parameter failed!",
        )

    def test_scalar_mult_overwrite_fail(self):
        scalar = torch.tensor([2, 3], dtype=torch.double)
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)

        with self.assertRaises(RuntimeError):
            cplx.scalar_mult(scalar, vector, out=vector)

        with self.assertRaises(RuntimeError):
            cplx.scalar_mult(scalar, vector, out=scalar)

    def test_matrix_vector_matmul(self):
        matrix = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)

        expect = torch.tensor([[-34, -42], [28, 48]], dtype=torch.double)

        self.assertTensorsEqual(
            cplx.matmul(matrix, vector),
            expect,
            msg="Matrix * Vector multiplication failed!",
        )

    def test_matrix_matrix_matmul(self):
        matrix1 = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)
        matrix2 = torch.tensor([[[1, 0], [3, 0]], [[0, 6], [0, 8]]], dtype=torch.double)
        expect = torch.tensor(
            [[[7, -78], [15, -106]], [[23, 22], [31, 50]]], dtype=torch.double
        )
        self.assertTensorsEqual(
            cplx.matmul(matrix1, matrix2),
            expect,
            msg="Matrix * Matrix multiplication failed!",
        )

    def test_scalar_inner_prod(self):
        scalar = torch.tensor([1, 2], dtype=torch.double)
        expect = torch.tensor([5, 0], dtype=torch.double)
        self.assertTensorsEqual(
            cplx.inner_prod(scalar, scalar), expect, msg="Scalar inner product failed!"
        )

    def test_vector_inner_prod(self):
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)
        expect = torch.tensor([30, 0], dtype=torch.double)
        self.assertTensorsEqual(
            cplx.inner_prod(vector, vector), expect, msg="Vector inner product failed!"
        )

    def test_outer_prod(self):
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)
        expect = torch.tensor(
            [[[10, 14], [14, 20]], [[0, 2], [-2, 0]]], dtype=torch.double
        )
        self.assertTensorsEqual(
            cplx.outer_prod(vector, vector), expect, msg="Outer product failed!"
        )

    def test_outer_prod_error_small(self):
        # take outer prod of 2 rank 1 tensors, instead of rank 2
        tensor = torch.tensor([1, 2], dtype=torch.double)
        with self.assertRaises(ValueError):
            cplx.outer_prod(tensor, tensor)

    def test_outer_prod_error_large(self):
        # take outer prod of 2 rank 3 tensors, instead of rank 2
        tensor = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)
        with self.assertRaises(ValueError):
            cplx.outer_prod(tensor, tensor)

    def test_conjugate(self):
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)

        expect = torch.tensor([[1, 2], [-3, -4]], dtype=torch.double)

        self.assertTensorsEqual(
            cplx.conjugate(vector), expect, msg="Vector conjugate failed!"
        )

    def test_matrix_conjugate(self):
        matrix = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)
        expect = torch.tensor(
            [[[1, 3], [2, 4]], [[-5, -7], [-6, -8]]], dtype=torch.double
        )
        self.assertTensorsEqual(
            cplx.conjugate(matrix), expect, msg="Matrix conjugate failed!"
        )

    def test_kronecker_prod(self):
        matrix = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)

        expect = torch.tensor(
            [
                [
                    [-24, -28, -28, -32],
                    [-32, -36, -36, -40],
                    [-32, -36, -36, -40],
                    [-40, -44, -44, -48],
                ],
                [
                    [10, 16, 16, 24],
                    [22, 28, 32, 40],
                    [22, 32, 28, 40],
                    [42, 52, 52, 64],
                ],
            ],
            dtype=torch.double,
        )

        self.assertTensorsEqual(
            cplx.kronecker_prod(matrix, matrix), expect, msg="Kronecker product failed!"
        )

    def test_kronecker_prod_error_small(self):
        # take KronProd of 2 rank 2 tensors, instead of rank 3
        tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)
        with self.assertRaises(ValueError):
            cplx.kronecker_prod(tensor, tensor)

    def test_kronecker_prod_error_large(self):
        # take KronProd of 2 rank 4 tensors, instead of rank 3
        tensor = torch.arange(16, dtype=torch.double).reshape(2, 2, 2, 2)
        with self.assertRaises(ValueError):
            cplx.kronecker_prod(tensor, tensor)

    def test_vector_scalar_divide(self):
        scalar = torch.tensor([1, 2], dtype=torch.double)
        vector = torch.tensor([[1, 2], [3, 4]], dtype=torch.double)
        expect = torch.tensor([[1.4, 2.0], [0.2, 0.0]], dtype=torch.double)

        self.assertTensorsAlmostEqual(
            cplx.scalar_divide(vector, scalar),
            expect,
            msg="Vector / Scalar divide failed!",
        )

    def test_matrix_scalar_divide(self):
        scalar = torch.tensor([1, 2], dtype=torch.double)
        matrix = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.double)

        expect = torch.tensor(
            [[[2.2, 2.8], [3.4, 4.0]], [[0.6, 0.4], [0.2, 0.0]]], dtype=torch.double
        )

        self.assertTensorsAlmostEqual(
            cplx.scalar_divide(matrix, scalar),
            expect,
            msg="Matrix / Scalar divide failed!",
        )

    def test_norm_sqr(self):
        scalar = torch.tensor([3, 4], dtype=torch.double)
        expect = torch.tensor(25, dtype=torch.double)

        self.assertTensorsEqual(cplx.norm_sqr(scalar), expect, msg="Norm failed!")

    def test_norm(self):
        scalar = torch.tensor([3, 4], dtype=torch.double)
        expect = torch.tensor(5, dtype=torch.double)

        self.assertTensorsEqual(cplx.norm(scalar), expect, msg="Norm failed!")

    def test_absolute_value(self):
        tensor = torch.tensor(
            [[[5, 5, -5, -5], [3, 6, -9, 1]], [[2, -2, 2, -2], [-7, 8, 0, 4]]],
            dtype=torch.double,
        )

        expect = torch.tensor(
            [[[np.sqrt(29)] * 4, [np.sqrt(58), 10, 9, np.sqrt(17)]]], dtype=torch.double
        )

        self.assertTensorsAlmostEqual(
            cplx.absolute_value(tensor), expect, msg="Absolute Value failed!"
        )


if __name__ == "__main__":
    unittest.main()
