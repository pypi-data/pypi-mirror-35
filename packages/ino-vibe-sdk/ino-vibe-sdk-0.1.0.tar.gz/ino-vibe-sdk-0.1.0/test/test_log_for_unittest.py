from datetime import datetime

import pytest

from inovibe import log
from inovibe.log import GCloudInstances


@pytest.fixture()
def testing():
    log.testing = True
    yield
    log.testing = False


def test_log_info(testing, mocker):
    mock_logger = mocker.patch.object(GCloudInstances, 'logger')

    rand_value = datetime.now().timestamp()
    log.info(label='unittest',
             data={'type': 'random_log', 'msg': rand_value})

    mock_logger.assert_not_called()


def test_log_wrong_format(testing, mocker):
    mock_logger = mocker.patch.object(GCloudInstances, 'logger')

    rand_value = datetime.now().timestamp()
    log.info(label='unittest', data=str(rand_value))

    mock_logger.assert_not_called()


def test_trace(testing, mocker):
    mock_tracer = mocker.patch.object(GCloudInstances, 'tracer')

    @log.trace_subcall()
    def function2():
        return 'world'

    @log.trace_entry()
    def function1():
        function2()
        return 'hello'

    function1()

    mock_tracer.assert_not_called()
