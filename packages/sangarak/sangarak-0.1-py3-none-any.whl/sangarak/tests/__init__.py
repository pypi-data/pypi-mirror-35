from unittest import TestCase
import numpy as np
import os

import sangarak

fixtures = "sangarak/tests/fixtures/"
np.set_printoptions(precision=3, linewidth=250, suppress=True)

class Test_16x16_4x4_2x2_Matrix(TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_16x16_4x4_2x2_Matrix, self).__init__(*args, **kwargs)
        self.path = os.path.abspath(fixtures + "/16x16_4x4_2x2/") + "/"
        self.matrix = np.arange(16*16).reshape(16,16)
        self.matrix[np.diag_indices_from(self.matrix)] += 5000
        self.n = 16
        self.nb = 4
        self.pb = 2
        self.num_procs = 4

    def test_read_matrix(self):
        files = {
            0: self.path + "0input.txt",
            1: self.path + "1input.txt",
            2: self.path + "2input.txt",
            3: self.path + "3input.txt"
        }
        m = sangarak.read_matrix(files, "row", self.n, self.nb, self.pb, self.num_procs)
        self.assertTrue(np.array_equal(self.matrix, m))
            
class Test_16x16_8x8_2x2_Matrix(TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_16x16_8x8_2x2_Matrix, self).__init__(*args, **kwargs)
        self.path = os.path.abspath(fixtures + "/16x16_8x8_2x2/") + "/"
        self.matrix = np.array([
            [5383., 886., 777., 915., 383., 886., 777., 915., 793.,  335., 386.,
             492.,  793.,  335.,  386.,  492.],
            [ 649., 5421.,362.,  27.,  649.,  421.,  362.,   27.,  690.,   59.,
              763.,  926.,  690.,   59.,  763.,  926.],
            [ 540., 426., 5172., 736.,  540.,  426.,  172.,  736.,  211.,  368.,
              567. , 429.,  211.,  368.,  567., 429.],
            [ 782., 530., 862., 5123.,  782.,  530.,  862.,  123.,   67.,  135.,
              929.,  802.,   67.,  135.,  929.,  802.],
            [ 383., 886., 777., 915., 5383.,  886.,  777.,  915.,  793.,  335.,
              386.,  492.,  793.,  335.,  386.,  492.],
            [ 649., 421., 362., 27.,  649., 5421.,  362.,   27.,  690. ,  59. ,
              763. , 926. , 690. ,  59. , 763. , 926.],
            [ 540., 426., 172., 736.,  540.,  426., 5172.,  736.,  211.,  368.,
              567.,  429.,  211.,  368.,  567.,  429.],
            [ 782., 530., 862., 123.,  782.,  530.,  862., 5123.,   67.,  135.,
              929.,  802.,   67.,  135.,  929.,  802.],
            [  22., 58.,  69.,  167.,   22.,   58.,   69.,  167., 5393.,  456.,
               11.,   42.,  393.,  456.,   11.,   42.],
            [ 229., 373., 421., 919.,  229.,  373.,  421.,  919.,  784., 5537.,
              198.,  324.,  784.,  537.,  198.,  324.],
            [ 315., 370., 413., 526.,  315., 370.,  413.,  526.,   91.,  980.,
              5956. , 873. ,  91.,  980. , 956.,  873.],
            [ 862., 170., 996., 281.,  862.,  170.,  996.,  281.,  305.,  925.,
              84., 5327.,  305.,  925.,   84.,  327.],
            [  22., 58.,  69.,  167.,   22.,   58.,   69.,  167.,  393.,  456.,
               11.,   42., 5393.,  456.,   11.,   42.],
            [ 229., 373., 421., 919.,  229.,  373.,  421.,  919.,  784.,  537.,
              198.,  324.,  784., 5537.,  198.,  324.],
            [ 315., 370., 413., 526.,  315.,  370.,  413.,  526. ,  91. , 980.,
              956. , 873. ,  91.,  980., 5956.,  873.],
            [ 862., 170., 996., 281.,  862.,  170.,  996.,  281.,  305., 925. ,
              84.,  327. , 305.,  925. ,  84., 5327.]
        ]            
        )
        self.n = 16
        self.nb = 8
        self.pb = 2
        self.num_procs = 4
    
    def test_read_matrix(self):
        files = {
            0: self.path + "0input.txt",
            1: self.path + "1input.txt",
            2: self.path + "2input.txt",
            3: self.path + "3input.txt"
        }

        m = sangarak.read_matrix(files, "row", self.n, self.nb, self.pb, self.num_procs)
        self.assertTrue(np.array_equal(self.matrix, m))

    def test_read_file(self):
        m = sangarak.read_file("input", self.n,self.nb,self.pb,self.num_procs,path=self.path)
        self.assertTrue(np.array_equal(self.matrix, m))
