from conans import ConanFile, CMake, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package_multi"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self):
            bin_path = os.path.join("bin", "test_package")
            in_wav_path = os.path.join(self.source_folder, "8kadpcm.wav")
            out_ogg_path = os.path.join("bin", "sample.ogg")
            self.run("{0} < {1} > {2}".format(bin_path, in_wav_path, out_ogg_path), run_environment=True)
