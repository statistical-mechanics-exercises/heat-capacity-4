import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) :
        self.assertTrue( "cv_temperatures" in globals(), "there is no variable in your code called cv_temperatures" )
        self.assertTrue( "cv" in globals(), "there is no variable in your code called cv" )
        self.assertTrue( "cv_errors" in globals(), "there is no variable in your code called cv_errors" )
        
    def test_errorbars(self) :
        self.assertTrue( len(cv_errors)==9, "cv_errors has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv_errors) ) :
            tmid = ( filedata[i+1,2] - filedata[i,2] ) / ( filedata[i+1,0] - filedata[i,0] )
            self.assertTrue( np.abs(tmid - cv_errors[i])<1E-6, "The error bars for your graph are incorrect" )
            
    def test_yvalues(self) :
        self.assertTrue( len(cv)==9, "cv has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv) ) :
            tmid = ( filedata[i+1,1] - filedata[i,1] ) / ( filedata[i+1,0] - filedata[i,0] )
            self.assertTrue( np.abs(tmid - cv[i])<1E-6, "the heat capacities have been computed wrongly" )
            
    def test_xvalues(self) :
        self.assertTrue( len(cv_temperatures)==9, "cv_temperatures has the wrong length" )
        filedata = np.loadtxt("md_results.txt")
        for i in range(len(cv_temperatures) ) :
            tmid = ( filedata[i,0] + filedata[i+1,0] ) / 2
            self.assertTrue( np.abs(tmid - cv_temperatures[i])<1E-6, "the temperatures at which you have plotted the heat capacities are incorrect" )
