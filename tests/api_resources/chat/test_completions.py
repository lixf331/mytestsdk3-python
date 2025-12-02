# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mytestsdk3 import Mytestsdk3, AsyncMytestsdk3
from tests.utils import assert_matches_type
from mytestsdk3.types.chat import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Mytestsdk3) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Mytestsdk3) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
            allowed_token_ids=[0],
            best_of=0,
            chat_template_kwargs={"foo": "bar"},
            extra_args={"foo": "bar"},
            api_extra_body={"foo": "bar"},
            frequency_penalty=-2,
            ignore_eos=True,
            include_stop_str_in_output=True,
            logit_bias={"foo": 0},
            logits_processors=["string"],
            logprobs=True,
            max_tokens=0,
            min_p=0,
            min_tokens=0,
            n=0,
            output_kind="cumulative",
            presence_penalty=-2,
            prompt_logprobs=0,
            reasoning_effort="low",
            repetition_penalty=0,
            response_format={
                "type": "text",
                "json_schema": {
                    "name": "name",
                    "description": "description",
                    "schema": {"foo": "bar"},
                    "strict": True,
                },
            },
            seed=0,
            skip_special_tokens=True,
            spaces_between_special_tokens=True,
            stop="\n",
            stop_token_ids=[0],
            stream=True,
            stream_options={
                "continuous_usage_stats": True,
                "include_usage": True,
            },
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            truncate_prompt_tokens=-1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Mytestsdk3) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Mytestsdk3) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMytestsdk3) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMytestsdk3) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
            allowed_token_ids=[0],
            best_of=0,
            chat_template_kwargs={"foo": "bar"},
            extra_args={"foo": "bar"},
            api_extra_body={"foo": "bar"},
            frequency_penalty=-2,
            ignore_eos=True,
            include_stop_str_in_output=True,
            logit_bias={"foo": 0},
            logits_processors=["string"],
            logprobs=True,
            max_tokens=0,
            min_p=0,
            min_tokens=0,
            n=0,
            output_kind="cumulative",
            presence_penalty=-2,
            prompt_logprobs=0,
            reasoning_effort="low",
            repetition_penalty=0,
            response_format={
                "type": "text",
                "json_schema": {
                    "name": "name",
                    "description": "description",
                    "schema": {"foo": "bar"},
                    "strict": True,
                },
            },
            seed=0,
            skip_special_tokens=True,
            spaces_between_special_tokens=True,
            stop="\n",
            stop_token_ids=[0],
            stream=True,
            stream_options={
                "continuous_usage_stats": True,
                "include_usage": True,
            },
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {"foo": "bar"},
                    },
                    "type": "function",
                }
            ],
            top_k=0,
            top_p=0,
            truncate_prompt_tokens=-1,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMytestsdk3) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMytestsdk3) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[
                {
                    "content": "Explain the importance of low latency LLMs",
                    "role": "user",
                }
            ],
            model="meta-llama/Llama-3.3-70B-Instruct1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
