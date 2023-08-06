from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class TurnByTurnDirectionsPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "convert natural language to turn-by-turn directions.",
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
                temperature=0.3,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
        }

    def _software_configs(self):
        return {
            "turn_by_turn_directions": PromptConfig(
                name="turn_by_turn_directions",
                description="This promptware is used to "
                "convert natural language to turn-by-turn directions.",
                instruction="Create a numbered list of turn-by-turn "
                "directions from this text: \n\n",
                demonstration=[],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {
                "text": "Go south on 95 until you hit Sunrise "
                "boulevard then take it east to us 1 and head south. "
                "Tom Jenkins bbq will be on the left after several "
                "miles."
            },
            "output": "1. Go south on 95\n2. Take Sunrise Boulevard east\n3. Head "
            "south on US 1\n4. Tom Jenkins BBQ will be on the left after "
            "several miles",
        }
