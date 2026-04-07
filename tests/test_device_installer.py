import json
import unittest
from unittest.mock import patch

from lib.classes.device_installer import DeviceInstaller


class DeviceInstallerTests(unittest.TestCase):
    @patch("lib.classes.device_installer.subprocess.check_call")
    @patch.object(DeviceInstaller, "check_numpy", return_value=True)
    @patch.object(DeviceInstaller, "get_package_version", return_value=False)
    def test_install_device_packages_falls_back_to_supported_cuda_tag(
        self,
        _get_package_version,
        _check_numpy,
        mock_check_call,
    ):
        installer = DeviceInstaller()
        device_info = json.dumps(
            {
                "name": "cuda",
                "os": "manylinux_2_28",
                "arch": "x86_64",
                "pyvenv": [3, 12],
                "tag": "cu120",
                "note": "",
            }
        )

        result = installer.install_device_packages(device_info)

        self.assertEqual(result, 0)
        mock_check_call.assert_called_once_with(
            [
                unittest.mock.ANY,
                "-m",
                "pip",
                "install",
                "--no-cache-dir",
                "torch==2.7.1",
                "torchaudio==2.7.1",
                "--force-reinstall",
                "--index-url",
                "https://download.pytorch.org/whl/cu118",
            ]
        )


if __name__ == "__main__":
    unittest.main()
