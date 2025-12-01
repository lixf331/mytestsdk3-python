# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CompletionCreateResponse", "Choice", "ChoiceMessage", "Usage", "UsagePromptTokensDetails"]


class ChoiceMessage(BaseModel):
    content: Optional[str] = None
    """The content of the message."""

    role: Optional[str] = None
    """The role of the author of this message."""


class Choice(BaseModel):
    index: Optional[int] = None
    """The index of the choice in the list of choices."""

    message: Optional[ChoiceMessage] = None


class UsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None
    """Number of tokens that were cached and reused."""


class Usage(BaseModel):
    completion_tokens: Optional[int] = None
    """Number of tokens in the generated completion."""

    prompt_tokens: Optional[int] = None
    """Number of tokens in the prompt."""

    prompt_tokens_details: Optional[UsagePromptTokensDetails] = None
    """Breakdown of tokens in the prompt."""

    total_tokens: Optional[int] = None
    """Total number of tokens used in the request (prompt + completion)."""


class CompletionCreateResponse(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the chat completion."""

    choices: Optional[List[Choice]] = None
    """A list of chat completion choices.

    Can be more than one if `n` is greater than 1.
    """

    created: Optional[int] = None
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: Optional[str] = None
    """The model used for the chat completion."""

    object: Optional[Literal["chat.completion"]] = None
    """The object type, which is always `chat.completion`."""

    service_tier: Optional[Literal["auto", "on_demand", "flex", "performance"]] = None
    """The service tier used for the request."""

    system_fingerprint: Optional[str] = None
    """This fingerprint represents the backend configuration that the model runs with.

    Can be used in conjunction with the `seed` request parameter to understand when
    backend changes have been made that might impact determinism.
    """

    usage: Optional[Usage] = None
    """Usage statistics for the completion request."""
