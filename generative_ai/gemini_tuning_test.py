# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

import gemini_tuning


@pytest.mark.skip(reason="Skip due to tuning taking a long time.")
def test_gemini_tuning() -> None:
    response = gemini_tuning.gemini_tuning_basic()
    assert response

    response = gemini_tuning.gemini_tuning_advanced()
    assert response


def test_get_tuning_job() -> None:
    response = gemini_tuning.get_tuning_job()
    assert response


def test_list_tuning_jobs() -> None:
    response = gemini_tuning.list_tuning_jobs()
    assert response


@pytest.mark.skip(reason="Skip due to tuning taking a long time.")
def test_cancel_tuning_job() -> None:
    gemini_tuning.cancel_tuning_job()
