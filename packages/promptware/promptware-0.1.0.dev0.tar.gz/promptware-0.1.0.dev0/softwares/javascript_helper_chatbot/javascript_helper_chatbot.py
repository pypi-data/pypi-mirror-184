from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class JavaScriptHelperChatbotPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "create a message-style chatbot that can "
            "answer questions about using JavaScript. "
            "It uses a few examples to get the conversation started.",
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
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["You:"],
            )
        }

    def _software_configs(self):
        return {
            "javascript_helper_chatbot": PromptConfig(
                name="javaScript_helper_chatbot",
                description="This promptware is used to "
                "create a message-style chatbot that can "
                "answer questions about using JavaScript. "
                "It uses a few examples to get the conversation started.",
                instruction="",
                demonstration=[
                    "You: How do I combine arrays?\n"
                    "JavaScript chatbot: You can use the concat() method.\n"
                ],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {
                "text": "You: How do you make an alert appear after 10"
                " seconds?\nJavaScript chatbot"
            },
            "output": "You can use the setTimeout() method.",
        }
