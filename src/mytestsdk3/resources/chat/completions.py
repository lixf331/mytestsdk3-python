# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chat import completion_create_params
from ..._base_client import make_request_options
from ...types.chat.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lixf331/mytestsdk3-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lixf331/mytestsdk3-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        allowed_token_ids: Optional[Iterable[int]] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        chat_template_kwargs: Optional[Dict[str, object]] | Omit = omit,
        custom_extra_body: Optional[Dict[str, object]] | Omit = omit,
        extra_args: Optional[Dict[str, object]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        ignore_eos: Optional[bool] | Omit = omit,
        include_stop_str_in_output: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logits_processors: Optional[SequenceNotStr[completion_create_params.LogitsProcessor]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        min_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_kind: Optional[Literal["cumulative", "delta", "final_only"]] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt_logprobs: Optional[int] | Omit = omit,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        skip_special_tokens: Optional[bool] | Omit = omit,
        spaces_between_special_tokens: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stop_token_ids: Optional[Iterable[int]] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[completion_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncate_prompt_tokens: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        OpenAI-compatible chat completion endpoint.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use.

          allowed_token_ids: Whitelist of token IDs that can be generated. Only tokens in this list will be
              considered during sampling. If specified, all other tokens are excluded. Useful
              for constrained generation, structured output, or limiting output to specific
              vocabulary (e.g., only numbers, only specific keywords). If null, all tokens are
              allowed.

          best_of: Generate multiple completions and return the best one. Ignored when n is set.

          chat_template_kwargs: Additional keyword args to pass to the template renderer. Will be accessible by
              the chat template.

          custom_extra_body: Additional parameters to include in the request body that are not part of the
              standard API schema. These parameters are passed directly to the underlying
              model or backend service. Useful for accessing experimental features,
              model-specific options, or implementation-specific parameters that haven't been
              standardized yet. The structure and accepted keys depend on the specific model
              and backend implementation being used.

          extra_args: Additional model-specific or implementation-specific arguments not covered by
              standard parameters. This allows passing custom parameters that may be specific
              to certain models or backends. The structure and accepted keys depend on the
              model and implementation being used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          ignore_eos: If true, ignore the EOS (End of Sequence) token and continue generating. When
              false, generation stops when EOS token is encountered.

          include_stop_str_in_output: If true, the stop sequence that triggered the stop will be included in the
              output text. By default (false), stop sequences are removed from the output.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logits_processors: A list of either qualified names of logits processors, or constructor objects,
              to apply when sampling. A constructor is a JSON object with a required
              'qualname' field specifying the qualified name of the processor class/factory,
              and optional 'args' and 'kwargs' fields containing positional and keyword
              arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
              2], 'kwargs': {'param': 'value'}}.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          min_p: Minimum probability threshold relative to the most likely token. Only tokens
              with probability >= (max_probability \\** min_p) are considered. For example, if
              the top token has probability 0.4 and min_p=0.1, only tokens with probability >=
              0.04 are sampled.

          min_tokens: The minimum number of tokens to generate. Generation will continue until at
              least this many tokens are produced, even if stop sequences or EOS tokens are
              encountered. Useful for ensuring a minimum response length.

          n: How many chat completion choices to generate for each input message.

          output_kind: Controls the format of streaming output for incremental text generation. -
              cumulative: Return the full accumulated text so far (default for most use
              cases). - delta: Return only the newly generated tokens since the last update
              (useful for streaming UIs). - final_only: Return only the complete final
              response, no intermediate updates.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_logprobs: Number of most likely tokens to return at each prompt token position, from the
              end of the prompt. For example, prompt_logprobs=5 will return the top 5 most
              likely tokens and their log probabilities for the last 5 tokens in the prompt.
              Useful for analyzing model confidence on input.

          reasoning_effort: Controls the amount of reasoning effort the model applies when generating
              responses. Higher values typically result in more thorough reasoning but may
              increase latency and cost.

          repetition_penalty: Penalty for repeating tokens. Values > 1.0 reduce repetition. Default is 1.0 (no
              penalty). Higher values (e.g., 1.2) make the model less likely to repeat the
              same token.

          response_format: Specifies the format of the response. Controls how the model structures its
              output. - text: Plain text output (default) - json_object: Ensures the response
              is valid JSON - json_schema: Validates response against a JSON schema -
              structural_tag: Uses custom structural tags for structured output

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

          skip_special_tokens: Whether to skip special tokens (e.g., BOS, EOS, padding tokens) in the output
              text. If true, special tokens are filtered out from the response. If false,
              special tokens are included in the output, which may be useful for debugging or
              token-level analysis.

          spaces_between_special_tokens: Whether to add spaces between special tokens when decoding. If true, spaces are
              inserted between special tokens in the output. If false, special tokens are
              concatenated without spaces. This affects the formatting of the decoded text
              output.

          stop: where the API will stop generating further tokens. The returned text will not
              contain the stop sequence.

          stop_token_ids: List of token IDs where the API will stop generating further tokens. The
              returned text will not contain these tokens. Useful when you know specific token
              IDs to stop at (e.g., end-of-text tokens).

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          stream_options: Options for controlling streaming behavior. Only used when stream is true.
              Controls whether usage statistics are included and how they are reported during
              streaming.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or top_p but not
              both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools (functions) the model may call. The model can choose to call one
              or more of these functions during the conversation. Each tool defines a function
              with a name, description, and parameters (JSON schema). The model will generate
              function calls in a structured format when it determines a function should be
              invoked.

          top_k: Limit sampling to the top K most likely tokens. For example, top_k=10 means only
              the 10 most probable tokens are considered. Lower values make output more
              focused, higher values more diverse.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or temperature but not both.

          truncate_prompt_tokens: Maximum number of prompt tokens to keep. If prompt exceeds this limit, tokens
              will be truncated. Use -1 to disable truncation. Positive values truncate from
              the beginning, keeping the end. Useful when prompt is too long for the model's
              context window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/openai/v1/chat/completions",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "allowed_token_ids": allowed_token_ids,
                    "best_of": best_of,
                    "chat_template_kwargs": chat_template_kwargs,
                    "custom_extra_body": custom_extra_body,
                    "extra_args": extra_args,
                    "frequency_penalty": frequency_penalty,
                    "ignore_eos": ignore_eos,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "logit_bias": logit_bias,
                    "logits_processors": logits_processors,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "min_tokens": min_tokens,
                    "n": n,
                    "output_kind": output_kind,
                    "presence_penalty": presence_penalty,
                    "prompt_logprobs": prompt_logprobs,
                    "reasoning_effort": reasoning_effort,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "skip_special_tokens": skip_special_tokens,
                    "spaces_between_special_tokens": spaces_between_special_tokens,
                    "stop": stop,
                    "stop_token_ids": stop_token_ids,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                    "truncate_prompt_tokens": truncate_prompt_tokens,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lixf331/mytestsdk3-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lixf331/mytestsdk3-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        messages: Iterable[completion_create_params.Message],
        model: str,
        allowed_token_ids: Optional[Iterable[int]] | Omit = omit,
        best_of: Optional[int] | Omit = omit,
        chat_template_kwargs: Optional[Dict[str, object]] | Omit = omit,
        custom_extra_body: Optional[Dict[str, object]] | Omit = omit,
        extra_args: Optional[Dict[str, object]] | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        ignore_eos: Optional[bool] | Omit = omit,
        include_stop_str_in_output: Optional[bool] | Omit = omit,
        logit_bias: Optional[Dict[str, int]] | Omit = omit,
        logits_processors: Optional[SequenceNotStr[completion_create_params.LogitsProcessor]] | Omit = omit,
        logprobs: Optional[bool] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        min_tokens: Optional[int] | Omit = omit,
        n: Optional[int] | Omit = omit,
        output_kind: Optional[Literal["cumulative", "delta", "final_only"]] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        prompt_logprobs: Optional[int] | Omit = omit,
        reasoning_effort: Optional[Literal["low", "medium", "high"]] | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[completion_create_params.ResponseFormat] | Omit = omit,
        seed: Optional[int] | Omit = omit,
        skip_special_tokens: Optional[bool] | Omit = omit,
        spaces_between_special_tokens: Optional[bool] | Omit = omit,
        stop: Union[Optional[str], SequenceNotStr[str], None] | Omit = omit,
        stop_token_ids: Optional[Iterable[int]] | Omit = omit,
        stream: Optional[bool] | Omit = omit,
        stream_options: Optional[completion_create_params.StreamOptions] | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[completion_create_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[completion_create_params.Tool]] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        truncate_prompt_tokens: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompletionCreateResponse:
        """
        OpenAI-compatible chat completion endpoint.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use.

          allowed_token_ids: Whitelist of token IDs that can be generated. Only tokens in this list will be
              considered during sampling. If specified, all other tokens are excluded. Useful
              for constrained generation, structured output, or limiting output to specific
              vocabulary (e.g., only numbers, only specific keywords). If null, all tokens are
              allowed.

          best_of: Generate multiple completions and return the best one. Ignored when n is set.

          chat_template_kwargs: Additional keyword args to pass to the template renderer. Will be accessible by
              the chat template.

          custom_extra_body: Additional parameters to include in the request body that are not part of the
              standard API schema. These parameters are passed directly to the underlying
              model or backend service. Useful for accessing experimental features,
              model-specific options, or implementation-specific parameters that haven't been
              standardized yet. The structure and accepted keys depend on the specific model
              and backend implementation being used.

          extra_args: Additional model-specific or implementation-specific arguments not covered by
              standard parameters. This allows passing custom parameters that may be specific
              to certain models or backends. The structure and accepted keys depend on the
              model and implementation being used.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          ignore_eos: If true, ignore the EOS (End of Sequence) token and continue generating. When
              false, generation stops when EOS token is encountered.

          include_stop_str_in_output: If true, the stop sequence that triggered the stop will be included in the
              output text. By default (false), stop sequences are removed from the output.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logits_processors: A list of either qualified names of logits processors, or constructor objects,
              to apply when sampling. A constructor is a JSON object with a required
              'qualname' field specifying the qualified name of the processor class/factory,
              and optional 'args' and 'kwargs' fields containing positional and keyword
              arguments. For example: {'qualname': 'my_module.MyLogitsProcessor', 'args': [1,
              2], 'kwargs': {'param': 'value'}}.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          min_p: Minimum probability threshold relative to the most likely token. Only tokens
              with probability >= (max_probability \\** min_p) are considered. For example, if
              the top token has probability 0.4 and min_p=0.1, only tokens with probability >=
              0.04 are sampled.

          min_tokens: The minimum number of tokens to generate. Generation will continue until at
              least this many tokens are produced, even if stop sequences or EOS tokens are
              encountered. Useful for ensuring a minimum response length.

          n: How many chat completion choices to generate for each input message.

          output_kind: Controls the format of streaming output for incremental text generation. -
              cumulative: Return the full accumulated text so far (default for most use
              cases). - delta: Return only the newly generated tokens since the last update
              (useful for streaming UIs). - final_only: Return only the complete final
              response, no intermediate updates.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt_logprobs: Number of most likely tokens to return at each prompt token position, from the
              end of the prompt. For example, prompt_logprobs=5 will return the top 5 most
              likely tokens and their log probabilities for the last 5 tokens in the prompt.
              Useful for analyzing model confidence on input.

          reasoning_effort: Controls the amount of reasoning effort the model applies when generating
              responses. Higher values typically result in more thorough reasoning but may
              increase latency and cost.

          repetition_penalty: Penalty for repeating tokens. Values > 1.0 reduce repetition. Default is 1.0 (no
              penalty). Higher values (e.g., 1.2) make the model less likely to repeat the
              same token.

          response_format: Specifies the format of the response. Controls how the model structures its
              output. - text: Plain text output (default) - json_object: Ensures the response
              is valid JSON - json_schema: Validates response against a JSON schema -
              structural_tag: Uses custom structural tags for structured output

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

          skip_special_tokens: Whether to skip special tokens (e.g., BOS, EOS, padding tokens) in the output
              text. If true, special tokens are filtered out from the response. If false,
              special tokens are included in the output, which may be useful for debugging or
              token-level analysis.

          spaces_between_special_tokens: Whether to add spaces between special tokens when decoding. If true, spaces are
              inserted between special tokens in the output. If false, special tokens are
              concatenated without spaces. This affects the formatting of the decoded text
              output.

          stop: where the API will stop generating further tokens. The returned text will not
              contain the stop sequence.

          stop_token_ids: List of token IDs where the API will stop generating further tokens. The
              returned text will not contain these tokens. Useful when you know specific token
              IDs to stop at (e.g., end-of-text tokens).

          stream: If set, partial message deltas will be sent. Tokens will be sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          stream_options: Options for controlling streaming behavior. Only used when stream is true.
              Controls whether usage statistics are included and how they are reported during
              streaming.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or top_p but not
              both.

          tool_choice: Controls which (if any) tool is called by the model. `none` means the model will
              not call any tool and instead generates a message. `auto` means the model can
              pick between generating a message or calling one or more tools. `required` means
              the model must call one or more tools. Specifying a particular tool via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that tool.

              `none` is the default when no tools are present. `auto` is the default if tools
              are present.

          tools: A list of tools (functions) the model may call. The model can choose to call one
              or more of these functions during the conversation. Each tool defines a function
              with a name, description, and parameters (JSON schema). The model will generate
              function calls in a structured format when it determines a function should be
              invoked.

          top_k: Limit sampling to the top K most likely tokens. For example, top_k=10 means only
              the 10 most probable tokens are considered. Lower values make output more
              focused, higher values more diverse.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or temperature but not both.

          truncate_prompt_tokens: Maximum number of prompt tokens to keep. If prompt exceeds this limit, tokens
              will be truncated. Use -1 to disable truncation. Positive values truncate from
              the beginning, keeping the end. Useful when prompt is too long for the model's
              context window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/openai/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "allowed_token_ids": allowed_token_ids,
                    "best_of": best_of,
                    "chat_template_kwargs": chat_template_kwargs,
                    "custom_extra_body": custom_extra_body,
                    "extra_args": extra_args,
                    "frequency_penalty": frequency_penalty,
                    "ignore_eos": ignore_eos,
                    "include_stop_str_in_output": include_stop_str_in_output,
                    "logit_bias": logit_bias,
                    "logits_processors": logits_processors,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "min_p": min_p,
                    "min_tokens": min_tokens,
                    "n": n,
                    "output_kind": output_kind,
                    "presence_penalty": presence_penalty,
                    "prompt_logprobs": prompt_logprobs,
                    "reasoning_effort": reasoning_effort,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "seed": seed,
                    "skip_special_tokens": skip_special_tokens,
                    "spaces_between_special_tokens": spaces_between_special_tokens,
                    "stop": stop,
                    "stop_token_ids": stop_token_ids,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                    "truncate_prompt_tokens": truncate_prompt_tokens,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
