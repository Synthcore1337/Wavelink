from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from nextcord.types.voice import GuildVoiceState, VoiceServerUpdate
    from typing_extensions import NotRequired, TypeAlias
    
class VoiceState(TypedDict):
    token: str
    endpoint: str
    sessionId: str
    connected: NotRequired[bool]
    ping: NotRequired[int]


class nextcordVoiceState(GuildVoiceState, VoiceServerUpdate):
    ...
