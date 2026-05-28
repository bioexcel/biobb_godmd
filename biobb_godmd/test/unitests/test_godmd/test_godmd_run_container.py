# type: ignore
from biobb_common.tools import test_fixtures as fx
from biobb_godmd.godmd.godmd_run import godmd_run
import pytest
import sys


class TestGOdMDrunDocker():
    def setup_class(self):
        fx.test_setup(self, 'godmd_run_docker')

    def teardown_class(self):
        # fx.test_teardown(self)
        pass

    def test_godmd_run_docker(self):
        godmd_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.not_empty(self.paths['output_ene_path'])
        assert fx.not_empty(self.paths['output_trj_path'])
        assert fx.not_empty(self.paths['output_pdb_path'])
        # assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
        # assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_rst_path'])


@pytest.mark.skipif(sys.platform == 'darwin', reason="singularity not available on macOS")
class TestGOdMDrunSingularity():
    def setup_class(self):
        fx.test_setup(self, 'godmd_run_singularity')

    def teardown_class(self):
        # fx.test_teardown(self)
        pass

    def test_godmd_run_singularity(self):
        godmd_run(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_log_path'])
        assert fx.not_empty(self.paths['output_ene_path'])
        assert fx.not_empty(self.paths['output_trj_path'])
        assert fx.not_empty(self.paths['output_pdb_path'])
        # assert fx.equal(self.paths['output_traj_path'], self.paths['ref_output_traj_path'])
        # assert fx.equal(self.paths['output_rst_path'], self.paths['ref_output_rst_path'])
