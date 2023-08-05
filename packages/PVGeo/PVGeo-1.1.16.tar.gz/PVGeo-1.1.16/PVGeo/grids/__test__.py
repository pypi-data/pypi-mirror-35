import unittest
import numpy as np
import shutil
import tempfile
import os

import urllib

# VTK imports:
import vtk
from vtk.util import numpy_support as nps
from vtk.numpy_interface import dataset_adapter as dsa

from .. import _helpers

# Functionality to test:
from .__init__ import *
from ..filters import PointsToPolyData

RTOL = 0.000001



###############################################################################

class TestTableToGrid(unittest.TestCase):
    """
    Test the `TableToGrid` filter
    """
    # TODO: This is conceptually difficult to decipher whether or not it is working
    def setUp(self):
        # Create some input tables
        self.table = vtk.vtkTable()
        # Populate the tables
        self.arrs = [None, None, None]
        self.n = 400
        self.titles = ('Array 0', 'Array 1', 'Array 2')
        self.arrs[0] = np.random.random(self.n)
        self.arrs[1] = np.random.random(self.n)
        self.arrs[2] = np.random.random(self.n)
        self.table.AddColumn(_helpers.numToVTK(self.arrs[0], self.titles[0]))
        self.table.AddColumn(_helpers.numToVTK(self.arrs[1], self.titles[1]))
        self.table.AddColumn(_helpers.numToVTK(self.arrs[2], self.titles[2]))
        return

    def check_data_fidelity(self, ido):
        """`TableToGrid`: data fidelity"""
        wido = dsa.WrapDataObject(ido)
        for i in range(len(self.titles)):
            arr = wido.PointData[self.titles[i]]
            self.assertTrue(np.allclose(arr, self.arrs[i], rtol=RTOL))

    def test_simple(self):
        """`TableToGrid`: check simple"""
        # Rearange data to check to match table
        for i in range(len(self.arrs)):
            a = np.reshape(self.arrs[i], (20, 2, 10))
            a = np.swapaxes(a, 0, 2)
            self.arrs[i] = a.flatten()
        # Use filter
        f = TableToGrid()
        f.SetInputDataObject(self.table)
        f.SetExtent(20, 2, 10)
        f.SetSpacing(5, 5, 5)
        f.SetOrigin(3.3, 6.0, 7)
        f.Update()
        ido = f.GetOutput()
        self.check_data_fidelity(ido)


    def test_fortran(self):
        """`TableToGrid`: check fortran order"""
        # Rearange data to check to match table
        for i in range(len(self.arrs)):
            a = np.reshape(self.arrs[i], (20, 2, 10))
            a = np.swapaxes(a, 0, 2)
            self.arrs[i] = a.flatten(order='F')
        # Use filter
        f = TableToGrid()
        f.SetInputDataObject(self.table)
        f.SetExtent(20, 2, 10)
        f.SetSpacing(5, 5, 5)
        f.SetOrigin(3.3, 6.0, 7)
        f.SetOrder('F')
        f.Update()
        ido = f.GetOutput()
        self.check_data_fidelity(ido)

    def test_seplib(self):
        """`TableToGrid`: check seplib"""
        # # Rearange data to check to match table
        # for i in range(len(self.arrs)):
        #     a = np.reshape(self.arrs[i], (10, 2, 20))
        #     a = np.swapaxes(a, 0, 2)
        #     a = np.swapaxes(a, 1, 2)
        #     #a = np.swapaxes(a, 0, 2)
        #     self.arrs[i] = a.flatten()
        # Use filter
        f = TableToGrid()
        f.SetInputDataObject(self.table)
        f.SetExtent(20, 2, 10)
        f.SetSpacing(5, 5, 5)
        f.SetOrigin(3.3, 6.0, 7)
        f.SetSEPlib(True)
        f.Update()
        ido = f.GetOutput()
        # TODO: self.check_data_fidelity(ido)
        return

    def test_swapXY(self):
        """`TableToGrid`: check swapXY"""
        # Rearange data to check to match table
        # for i in range(len(self.arrs)):
        #     a = np.reshape(self.arrs[i], (20, 2, 10))
        #     a = np.swapaxes(a, 0, 2)
        #     a = np.swapaxes(a, 1, 2)
        #     self.arrs[i] = a.flatten()
        # Use filter
        f = TableToGrid()
        f.SetInputDataObject(self.table)
        f.SetExtent(20, 2, 10)
        f.SetSpacing(5, 5, 5)
        f.SetOrigin(3.3, 6.0, 7)
        f.SetSwapXY(True)
        f.Update()
        ido = f.GetOutput()
        # TODO: self.check_data_fidelity(ido)
        return



###############################################################################

class TestReverseImageDataAxii(unittest.TestCase):
    """
    Test the `ReverseImageDataAxii` filter
    """

    def test(self):
        """`ReverseImageDataAxii`: check that it works on point and cell data"""
        # Create input vtkImageData:
        nx, ny, nz = 10, 11, 12
        arr = np.random.random((nz, ny, nx))
        arrCells = np.random.random((nz-1, ny-1, nx-1))
        image = vtk.vtkImageData()
        image.SetDimensions(nx, ny, nz)
        image.SetSpacing(2, 2, 2)
        image.SetOrigin(0, 0, 0)
        data = nps.numpy_to_vtk(num_array=arr.flatten(), deep=True)
        data.SetName('Data')
        cellData = nps.numpy_to_vtk(num_array=arrCells.flatten(), deep=True)
        cellData.SetName('CellData')
        image.GetPointData().AddArray(data)
        image.GetCellData().AddArray(cellData)
        # Now perfrom the reverse for only X:
        f = ReverseImageDataAxii()
        f.SetInputDataObject(image)
        f.SetFlipX(True)
        f.SetFlipY(False)
        f.SetFlipZ(False)
        f.Update()
        ido = f.GetOutput()
        self.assertIsNotNone(ido)
        self.assertEqual(ido.GetNumberOfPoints(), len(arr.flatten()))
        # Check that x-axis was reversed
        wido = dsa.WrapDataObject(ido)
        test = wido.PointData['Data']
        testCells = wido.CellData['CellData']
        self.assertTrue(np.allclose(test, np.flip(arr, axis=2).flatten(), rtol=RTOL))
        self.assertTrue(np.allclose(testCells, np.flip(arrCells, axis=2).flatten(), rtol=RTOL))
        # Now perfrom the reverse for all axii:
        f.SetFlipX(True)
        f.SetFlipY(True)
        f.SetFlipZ(True)
        f.Update()
        ido = f.GetOutput()
        self.assertIsNotNone(ido)
        self.assertEqual(ido.GetNumberOfPoints(), len(arr.flatten()))
        # Check that x-axis was reversed
        wido = dsa.WrapDataObject(ido)
        test = wido.PointData['Data']
        testCells = wido.CellData['CellData']
        tarr = np.flip(arr, axis=0)
        tarr = np.flip(tarr, axis=1)
        tarr = np.flip(tarr, axis=2)
        tarrCells = np.flip(arrCells, axis=0)
        tarrCells = np.flip(tarrCells, axis=1)
        tarrCells = np.flip(tarrCells, axis=2)
        self.assertTrue(np.allclose(test, tarr.flatten(), rtol=RTOL))
        self.assertTrue(np.allclose(testCells, tarrCells.flatten(), rtol=RTOL))


###############################################################################

class TestTranslateGridOrigin(unittest.TestCase):
    """
    Test the `TranslateGridOrigin` filter
    """
    def setUp(self):
        # Create some input tables
        self.idi = vtk.vtkImageData()
        self.idi.SetDimensions(20, 2, 10)
        self.idi.SetSpacing(1, 1, 1)
        self.idi.SetOrigin(100, 100, 100)
        # Populate the tables
        self.n = 400
        self.title = 'Array 0'
        self.arr = np.random.random(self.n)
        self.idi.GetPointData().AddArray(_helpers.numToVTK(self.arr, self.title))
        return

    def test_all(self):
        """`TranslateGridOrigin`: make sure works"""
        f = TranslateGridOrigin()
        f.SetInputDataObject(self.idi)
        f.SetCorner(1)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100-19)
        self.assertEqual(oy, 100)
        self.assertEqual(oz, 100)
        f.SetCorner(2)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100)
        self.assertEqual(oy, 100-1)
        self.assertEqual(oz, 100)
        f.SetCorner(3)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100-19)
        self.assertEqual(oy, 100-1)
        self.assertEqual(oz, 100)
        f.SetCorner(4)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100)
        self.assertEqual(oy, 100)
        self.assertEqual(oz, 100-9)
        f.SetCorner(5)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100-19)
        self.assertEqual(oy, 100)
        self.assertEqual(oz, 100-9)
        f.SetCorner(6)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100)
        self.assertEqual(oy, 100-1)
        self.assertEqual(oz, 100-9)
        f.SetCorner(7)
        f.Update()
        ido = f.GetOutput()
        ox, oy, oz = ido.GetOrigin()
        self.assertEqual(ox, 100-19)
        self.assertEqual(oy, 100-1)
        self.assertEqual(oz, 100-9)


###############################################################################


class TestSurferGridReader(unittest.TestCase):
    """
    Test the `SurferGridReader` and `WriteImageDataToSurfer`
    """
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.fname = os.path.join(self.test_dir, 'bouguer_alps_egm08.grd')

        import sys

        if sys.version_info[0] >= 3:
            from urllib.request import urlretrieve
        else:
            from urllib import urlretrieve

        urlretrieve('https://gist.github.com/leouieda/6023922/raw/' \
                        '948b0acbadb18e6ad49efe2092d9d9518b247780/' \
                        'bouguer_alps_egm08.grd', filename=self.fname)

    def tearDown(self):
        # Remove the test data directory after the test
        shutil.rmtree(self.test_dir)


    def test(self):
        """`SurferGridReader` and `WriteImageDataToSurfer`: Test reader and writer for Surfer format"""
        reader = SurferGridReader()
        reader.AddFileName(self.fname)
        reader.SetDataName('foo')
        reader.Update()
        img = reader.GetOutput()
        self.assertIsNotNone(img)
        # Check shapes of the surfer grid
        nx, ny, nz = img.GetDimensions()
        self.assertEqual(nx, 182)
        self.assertEqual(ny, 222)
        self.assertEqual(nz, 1)
        # Now test writer
        writer = WriteImageDataToSurfer()
        fname = os.path.join(self.test_dir, 'test-writer.grd')
        writer.SetFileName(fname)
        writer.SetInputArrayToProcess(0, 0, 0, 0, 'foo')
        writer.Write(img)
        # Read again and compare
        reader = SurferGridReader()
        reader.AddFileName(fname)
        reader.SetDataName('foo2')
        reader.Update()
        read = reader.GetOutput()
        self.assertIsNotNone(read)
        nx, ny, nz = read.GetDimensions()
        self.assertEqual(nx, 182)
        self.assertEqual(ny, 222)
        self.assertEqual(nz, 1)
        self.assertEqual(img.GetBounds(), read.GetBounds())
        # Check the data arrays
        imgArr = dsa.WrapDataObject(img).PointData['foo']
        readArr = dsa.WrapDataObject(read).PointData['foo2']
        self.assertTrue(np.allclose(imgArr, readArr))
        return



###############################################################################


class TestExtractTopography(unittest.TestCase):
    """
    Test the `ExtractTopography` filter
    """
    def test(self):
        """`ExtractTopography`: Test extraction on simple data"""
        # Produce some input data
        data = vtk.vtkImageData()
        data.SetOrigin(0.0, 0.0, 0.0)
        data.SetSpacing(5.0, 5.0, 5.0)
        data.SetDimensions(20, 20, 20)
        x = y = np.linspace(0, 100, num=50, dtype=float)
        g = np.meshgrid(x, y)
        # Convert to XYZ points
        points = np.vstack(map(np.ravel, g)).T
        z = np.reshape(np.full(len(points), 55.0), (len(points), -1))
        #z = np.reshape(np.random.uniform(low=55.0, high=65.0, size=(len(points),)), (len(points), -1))
        points = np.concatenate((points, z), axis=1)
        topo = PointsToPolyData(points)


        # # Apply filter
        filter = ExtractTopography()
        grd = filter.Apply(data, topo)

        # Test the output
        self.assertIsNotNone(grd)
        self.assertEqual(grd.GetDimensions(), data.GetDimensions())
        self.assertEqual(grd.GetSpacing(), data.GetSpacing())
        self.assertEqual(grd.GetOrigin(), data.GetOrigin())
        # Now check the active topo cell data?
        # TODO: implement
        active = dsa.WrapDataObject(grd).CellData['Active Topography']
        for i in range(grd.GetNumberOfCells()):
            cell = grd.GetCell(i)
            bounds = cell.GetBounds()
            z = bounds[5]#(bounds[4]+bounds[5])/2.0
            if z <= 55.0:
                self.assertTrue(active[i])
            elif z > 55.0:
                self.assertFalse(active[i])
            else:
                self.fail(msg='Non-testable cell encountered')

        return
