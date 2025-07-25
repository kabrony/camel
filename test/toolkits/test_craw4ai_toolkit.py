# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========

import pytest

from camel.toolkits.craw4ai_toolkit import Crawl4AIToolkit


@pytest.fixture(scope="function")
def toolkit_fixture():
    return Crawl4AIToolkit(timeout=600)


@pytest.mark.asyncio
async def test_scrape_success(toolkit_fixture):
    url = "https://github.com/camel-ai/camel/blob/master/LICENSE"
    result = await toolkit_fixture.scrape(url)
    assert len(result) > 0
