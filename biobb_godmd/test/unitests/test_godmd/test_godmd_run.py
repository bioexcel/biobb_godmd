from biobb_common.tools import test_fixtures as fx
from biobb_godmd.godmd.godmd_run import godmd_run


class TestGOdMDrun():
    def setup_class(self):
        fx.test_setup(self, 'godmd_run')

    def teardown_class(self):
        #fx.test_teardown(self)
        pass

    def test_godmd_run(self):
        godmd_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.not_empty(self.paths['output_ene_path'])
        assert fx.not_empty(self.paths['output_trj_path'])
        # assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
        # assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_rst_path'])
