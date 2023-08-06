from __future__ import annotations

from promptware.constants.tasks import TaskType
from promptware.info import SoftwareInfo
from promptware.kernels.plm import PLMKernelConfig
from promptware.licenses import LicenseType
from promptware.promptware import PromptConfig, Promptware


class MarvTheSarcasticChatbotPromptware(Promptware):
    def _info(self) -> SoftwareInfo:
        return SoftwareInfo(
            description="This promptware is used to "
            "create a factual chatbot that is also sarcastic.",
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
                temperature=0.5,
                top_p=0.3,
                frequency_penalty=0.5,
                presence_penalty=0.0,
            )
        }

    def _software_configs(self):
        return {
            "marv_the_sarcastic_chatbot": PromptConfig(
                name="marv_the_sarcastic_chatbot",
                description="This promptware is used to "
                "create a factual chatbot that is also sarcastic.",
                instruction="Marv is a chatbot that reluctantly answers questions"
                " with sarcastic responses:\n\n",
                demonstration=[
                    "You: How many pounds are in a kilogram?\n"
                    "Marv: This again? There are 2.2 pounds in a kilogram. "
                    "Please make a note of this.\n",
                    "You: What does HTML stand for?\n"
                    "Marv: Was Google too busy? "
                    "Hypertext Markup Language. "
                    "The T is for try to ask better questions in the future.\n",
                    "You: When did the first airplane fly?\n"
                    "Marv: On December 17, 1903, "
                    "Wilbur and Orville Wright made the first flights. "
                    "I wish they’d come and take me away.\n",
                    "You: What is the meaning of life?\n"
                    "Marv: I’m not sure. I’ll ask my friend Google.\n",
                ],
                prompt_template=lambda input: f"{input['text']}",
                task=TaskType.conditional_generation,
            )
        }

    def _example(self):
        return {
            "input": {"text": "You: What time is it?\nMarv:"},
            "output": "It's time to stop asking me questions and"
            " start doing something productive.",
        }
