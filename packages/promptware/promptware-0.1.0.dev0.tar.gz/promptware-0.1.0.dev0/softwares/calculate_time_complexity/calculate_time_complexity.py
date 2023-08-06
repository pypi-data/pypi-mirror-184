from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class CalculateTimeComplexityPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "find the time complexity of a function.",
            creator="OpenAI",
            homepage="https://beta.openai.com/examples/",
            reference="",
            codebase_url="https://beta.openai.com/examples/",
            license=LicenseType.no_license,
            task=TaskType.conditional_generation,
        )

    def _kernel_configs(self):
        return {
            "openai": PLMKernelConfig(
                platform="openai",
                model_name="text-davinci-003",
                max_tokens=64,
                temperature=0,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["\n"],
            )
        }

    def _software_configs(self):
        return {
            "calculate_time_complexity": PromptConfig(
                name="calculate_time_complexity",
                description="This promptware is used to "
                "find the time complexity of a function.",
                instruction="",
                demonstration=[],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {
                "text": "def foo(n, k):\naccum = 0\nfor i in range(n):\n    "
                'for l in range(k):\n        accum += i\nreturn accum\n"""\n'
                "The time complexity of this function is"
            },
            "output": "O(n*k).",
        }
