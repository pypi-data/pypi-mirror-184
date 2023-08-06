from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class ESRBRatingsPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "categorize text based upon ESRB ratings.",
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
                max_tokens=60,
                temperature=0,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["\n"],
            )
        }

    def _software_configs(self):
        return {
            "esrb_rating": PromptConfig(
                name="esrb_rating",
                description="This promptware is used to "
                "categorize text based upon ESRB ratings.",
                instruction="Provide an ESRB rating for the following text:\n\n",
                demonstration=[],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {
                "text": "\"i'm going to blow your brains"
                " out with my ray gun then stomp on your "
                'guts."\n\nESRB rating:'
            },
            "output": "Mature (M)",
        }
