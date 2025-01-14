import os
from typing import Dict, List, Optional, TypedDict
from attr import dataclass
import yaml

from gptcli.assistant import AssistantConfig

CONFIG_FILE_PATHS = [
    os.path.join(os.path.expanduser("~"), ".config", "gpt-cli", "gpt.yml"),
    os.path.join(os.path.expanduser("~"), ".gptrc"),
]


class LLaMAConfig(TypedDict):
    llama_cpp_dir: str
    models: Dict[str, str]  # name -> path


@dataclass
class GptCliConfig:
    default_assistant: str = "general"
    markdown: bool = True
    show_price: bool = True
    api_key: Optional[str] = os.environ.get("OPENAI_API_KEY")
    openai_api_key: Optional[str] = os.environ.get("OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = os.environ.get("ANTHROPIC_API_KEY")
    log_file: Optional[str] = None
    log_level: str = "INFO"
    assistants: Dict[str, AssistantConfig] = {}
    interactive: Optional[bool] = None
    llama_config: Optional[LLaMAConfig] = None


def choose_config_file(paths: List[str]) -> str:
    for path in paths:
        if os.path.isfile(path):
            return path
    return ""


def read_yaml_config(file_path: str) -> GptCliConfig:
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
        return GptCliConfig(
            **config,
        )
