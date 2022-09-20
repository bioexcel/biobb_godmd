from biobb_common.tools import test_fixtures as fx
from biobb_godmd.godmd.godmd_prep import godmd_prep

class TestGOdMDPrep():
    def setup_class(self):
        fx.test_setup(self, 'godmd_prep')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_godmd_prep(self):
        godmd_prep(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_aln_orig_path'])
        assert fx.not_empty(self.paths['output_aln_target_path'])
        #assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
        #assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_rst_path'])
