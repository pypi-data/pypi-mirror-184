from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class JavascriptOneLineFunctionPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "turn a JavaScript function into a one liner.",
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
                model_name="code-davinci-002",
                max_tokens=60,
                temperature=0,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=[";"],
            )
        }

    def _software_configs(self):
        return {
            "javascript_one_line_function": PromptConfig(
                name="javascript_one_line_function",
                description="This promptware is used to "
                "turn a JavaScript function into a one liner.",
                instruction="Use list comprehension to convert "
                "this into one line of JavaScript:\n\n",
                demonstration=[""],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {
                "text": "dogs.forEach((dog) => {\n    car.push(dog);\n});\n\n"
                "JavaScript one line version:"
            },
            "output": "dogs.forEach((dog) => car.push(dog))",
        }
