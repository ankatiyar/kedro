import os
import tempfile
from pathlib import Path

from kedro.config import OmegaConfigLoader


class OmegaConfigLoaderSuite:
    """Benchmark suite for OmegaConfigLoader."""

    # ASV setup method, called once per class
    def setup(self):
        # Create a temporary directory with some dummy config files
        self.temp_dir = tempfile.TemporaryDirectory()
        self.conf_source = Path(self.temp_dir.name)
        self.env = "local"
        self.config_content = """
        key1: value1
        key2: value2
        nested_key:
          nested_key1: nested_value1
        """
        # Create base and local config directories
        self.base_dir = self.conf_source / "base"
        self.local_dir = self.conf_source / self.env
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.local_dir.mkdir(parents=True, exist_ok=True)
        
        # Create some dummy config files
        with open(self.base_dir / "config1.yml", "w") as f:
            f.write(self.config_content)

        with open(self.local_dir / "config1.yml", "w") as f:
            f.write(self.config_content.replace("value1", "local_value1"))

        # Create an instance of OmegaConfigLoader
        self.config_loader = OmegaConfigLoader(conf_source=str(self.conf_source), env=self.env)

    # ASV teardown method, called once per class
    # def teardown(self):
    #     # Clean up temporary files
    #     self.temp_dir.cleanup()

    # Benchmark the loading of configurations
    def time_load_config(self):
        """Time how long it takes to load and merge configuration."""
        self.config_loader["config1"]

    # Benchmark the loading of configurations without merging
    def time_load_config_without_merge(self):
        """Time how long it takes to load configurations without merging."""
        self.config_loader.load_and_merge_dir_config(
            str(self.base_dir), patterns=["config1.yml"], key="config1", processed_files=set()
        )

    # Benchmark initialization of OmegaConfigLoader
    def time_initialization(self):
        """Time the initialization of OmegaConfigLoader."""
        OmegaConfigLoader(conf_source=str(self.conf_source), env=self.env)

    # Benchmark merging strategies
    def time_destructive_merge(self):
        """Benchmark the destructive merging strategy."""
        base_config = {'key1': 'value1', 'key2': 'value2'}
        env_config = {'key1': 'overridden_value1', 'key3': 'value3'}
        self.config_loader._destructive_merge(base_config, env_config, str(self.local_dir))

    def time_soft_merge(self):
        """Benchmark the soft merging strategy."""
        base_config = {'key1': 'value1', 'key2': 'value2'}
        env_config = {'key1': 'overridden_value1', 'key3': 'value3'}
        self.config_loader._soft_merge(base_config, env_config)

    # Benchmark resolving environment variables
    def time_resolve_environment_variables(self):
        """Benchmark the resolution of environment variables in the config."""
        config = OmegaConf.create({"path": "${oc.env:HOME}"})
        self.config_loader._resolve_environment_variables(config)

