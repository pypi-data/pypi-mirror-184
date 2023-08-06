"""DoHome lights broadcast"""

from typing import List
from ..transport import DoHomeBroadcastTransport
from .light import DoHomeLight
from .light import parse_response

class DoHomeLightsBroadcast(DoHomeLight):
    """DoHome broadcast light controller class"""
    _transport: DoHomeBroadcastTransport

    def __init__(self, sids: List[str], transport: DoHomeBroadcastTransport):
        super().__init__(sids, transport)
        self._sids = sids

    async def _send_request(self, request: str):
        response_data = await self._transport.send_request(
            request, 1, len(self._sids)
        )
        responses = list(map(parse_response, response_data))
        if len(responses) != len(self._sids):
            raise Exception("Not all lights responds")
        for response in responses:
            if response["res"] != 0:
                raise Exception('Command error')
        return responses[0]
