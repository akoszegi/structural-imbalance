#    Copyright 2020 D-Wave Systems Inc.

#    Licensed under the Apache License, Version 2.0 (the "License")
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http: // www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import subprocess
import unittest
import time
import os

class IntegrationTests(unittest.TestCase):

    def runDemo(self,hardware):
        cwd=os.getcwd()
        output=subprocess.check_output(["python", cwd+"/demo.py", hardware])
        return str(output)

    def test_structural_imbalance_cpu(self):

        output = self.runDemo("cpu")

        with self.subTest(msg="Verify if output contains 'Created CSV file: Results/Global/Structural Imbalance.csv' \n"):
            self.assertIn("Created CSV file: Results/Global/Structural Imbalance.csv".upper(),output.upper())
        with self.subTest(msg="Verify if output contains 'Running demo on cpu' \n"):
            self.assertIn("Running demo on cpu".upper(),output.upper())
        with self.subTest(msg="Verify if error string contains in output \n"):
            self.assertNotIn("ERROR",output.upper())
        with self.subTest(msg="Verify if warning string contains in output \n"):
            self.assertNotIn("WARNING",output.upper())

    def test_structural_imbalance_qpu(self):
        
        output = self.runDemo("qpu")

        with self.subTest(msg="Verify if output contains 'Created CSV file: Results/Global/Structural Imbalance.csv' \n"):
            self.assertIn("Created CSV file: Results/Global/Structural Imbalance.csv".upper(),output.upper())
        with self.subTest(msg="Verify if output contains 'Running demo on qpu' \n"):
            self.assertIn("Running demo on qpu".upper(),output.upper())
        with self.subTest(msg="Verify if error string contains in output \n"):
            self.assertNotIn("ERROR",output.upper())
        with self.subTest(msg="Verify if warning string contains in output \n"):
            self.assertNotIn("WARNING",output.upper())

if __name__ == '__main__':
    unittest.main()
