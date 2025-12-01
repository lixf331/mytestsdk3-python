# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["CompletionCreateParams"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[object]]
    """A list of messages comprising the conversation so far."""

    model: Required[str]
    """ID of the model to use."""

    max_tokens: Optional[int]
    """The maximum number of tokens that can be generated in the chat completion.

    The total length of input tokens and generated tokens is limited by the model's
    context length.
    """

    n: Optional[int]
    """How many chat completion choices to generate for each input message."""

    seed: Optional[int]
    """
    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result.
    """

    stop: Optional[str]
    """the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: Optional[bool]
    """If set, partial message deltas will be sent.

    Tokens will be sent as data-only
    [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
    as they become available, with the stream terminated by a `data: [DONE]`
    message.
    """

    temperature: Optional[float]
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or top_p but not both.
    """

    top_p: Optional[float]
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered. We
    generally recommend altering this or temperature but not both.
    """
