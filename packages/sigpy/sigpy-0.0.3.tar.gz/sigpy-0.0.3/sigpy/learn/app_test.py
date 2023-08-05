import unittest
import numpy as np
import numpy.testing as npt
from sigpy.learn import app

if __name__ == '__main__':
    unittest.main()


class TestApp(unittest.TestCase):

    def test_ConvSparseDecom(self):

        lamda = 1e-9
        l = np.array([[1 , 1],
                      [1, -1]], dtype=np.float) / 2**0.5
        data = np.array([[1, 1]], dtype=np.float) / 2**0.5

        r_j = app.ConvSparseDecom(data, l, lamda=lamda).run()

        npt.assert_allclose(r_j, [[[1], [0]]])

    def test_ConvSparseCoefficients(self):

        lamda = 1e-10
        l = np.array([[1 , 1],
                      [1, -1]], dtype=np.float) / 2**0.5
        data = np.array([[1, 1]], dtype=np.float) / 2**0.5

        r_j = app.ConvSparseCoefficients(data, l, lamda=lamda)
        
        npt.assert_allclose(r_j[:], [[[1], [0]]])        
        npt.assert_allclose(r_j[0, :], [[1], [0]])
        npt.assert_allclose(r_j[:, 0], [[1]])
        npt.assert_allclose(r_j[:, :, 0], [[1, 0]])
        

    def test_ConvSparseCoding(self):

        num_atoms = 1
        filt_width = 2
        batch_size = 1
        data = np.array([[1, 1]], dtype=np.float) / 2**0.5
        lamda = 1e-3
        alpha = np.infty

        l = app.ConvSparseCoding(data, num_atoms, filt_width, batch_size,
                                 alpha=alpha, lamda=lamda, max_iter=10).run()

        npt.assert_allclose(np.abs(l) / np.abs(l).max(), [[1, 1]])

    def test_LinearRegression(self):

        n = 2
        k = 5
        m = 4
        batch_size = n

        r_j = np.random.randn(n, k)
        data = np.random.randn(n, m)
        
        alpha = 1 / np.linalg.svd(r_j, compute_uv=False)[0]**2

        mat = app.LinearRegression(r_j, data, batch_size, alpha).run()
        
        mat_lstsq = np.linalg.lstsq(r_j, data, rcond=None)[0]

        npt.assert_allclose(mat, mat_lstsq, atol=1e-3, rtol=1e-3)
