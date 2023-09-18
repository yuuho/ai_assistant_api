"""chatgpt
"""

from logging import getLogger
import os

from langchain.chat_models import ChatOpenAI


logger = getLogger(__name__)
logger.info('loaded application.py')


class ChatGPT:

    def __init__(self):
        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

        logger.info(f'my api key is : {OPENAI_API_KEY}')

        self.model = ChatOpenAI(model_name="gpt-3.5-turbo",
                                openai_api_key=OPENAI_API_KEY,
                                max_tokens=100,
                                model_kwargs={'timeout': 20})

    def chat(self, prompt):
        logger.info('chat start...')
        try:
            ret = self.model.predict(prompt)
        except Exception as exp:
            print(exp)
            logger.warning(str(exp))
        logger.info('chat done.')
        return ret
