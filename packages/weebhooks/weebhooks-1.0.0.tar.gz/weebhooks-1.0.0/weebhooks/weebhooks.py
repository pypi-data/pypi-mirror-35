import requests
import aiohttp
import json
from .errors import InvalidArgument
from .embed import Embed

class Webhook:
    """
    The Discord webhook object. 

    Params:

    `is_async` (bool): Whether to use the webhooks in async or sync.

    `avatar_url` (str): The URL for the avatar that the webhook will use. Will use the webhook's avatar by default.

    `username` (str): The username that the webhook will use. Will use the webhook's name by default.

    """

    def __init__(self, url, **options):
        self.url = url
        self.is_async = options.get("is_async", False)
        self.avatar_url = options.get("avatar_url", None)
        self.username = options.get("username", None) or options.get("name", None)
        
        
        self.session = aiohttp.ClientSession() if self.is_async else requests.Session() 

    async def _send_async(self, content, **options):
        """
        Private function to send in async.
        """
        embed = options.get("embed", None)
        embeds = options.get("embeds", None)
        tts = options.get("tts", False)
        if embed and embeds:
            raise InvalidArgument("Cannot provide both embed and embeds parameters.")
        data = {
            "content": content,
            "avatar_url": self.avatar_url,
            "username": self.username,
            "tts": tts
        }
        if embed or embeds:
            data['embeds'] = [embed.results] if embed else list(map(lambda x: x.results, embeds))
        headers = {
            "Content-Type": "application/json"
        }
        b = self.session.post(self.url, data=json.dumps(data), headers=headers)
        return b

    

    def send(self, content, **options):
        """
        Sends the actual webhook message.

        `content` (str): The message content for the webhook message.

        `embed` (weebhooks.Embed): An Embed object for the bot to send. If this is provided, `embeds` cannot be provided.

        `embeds` (List: weebhooks.Embed): A List of Embed objects for the bot to send. If this is provided, `embed` cannot be provided.
        
        `tts` (bool): Whether to send the message with Text-to-Speech. Defaults to False.
        """
        embed = options.get("embed", None)
        embeds = options.get("embeds", None)
        tts = options.get("tts", False)
        if self.is_async:
            return self._send_async(content, **options)
        data = {
            "content": content,
            "avatar_url": self.avatar_url,
            "username": self.username,
            "tts": tts
        }
        if embed or embeds:
            data['embeds'] = [embed.results] if embed else list(
                map(lambda x: x.results, embeds))
        headers = {
            "Content-Type": "application/json"
        }
        b = self.session.post(self.url, data=json.dumps(data), headers=headers)    
        return b
