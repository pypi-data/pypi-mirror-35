from inovibe import notification as notif


TEST_DEVID = 'test_devid'
TEST_ALIAS = 'hello_world'


def test_power_up_msg():
    msg = notif.PowerUpMessage(devid=TEST_DEVID, alias=TEST_ALIAS)

    assert msg.msg_type == 'power_up'
    assert msg.devid == TEST_DEVID
    assert msg.alias == TEST_ALIAS


def test_power_off_msg():
    msg = notif.PowerOffMessage(devid=TEST_DEVID, alias=TEST_ALIAS)

    assert msg.msg_type == 'power_off'
    assert msg.devid == TEST_DEVID
    assert msg.alias == TEST_ALIAS


def test_install_complete_msg():
    msg = notif.InstallCompleteMessage(devid=TEST_DEVID, alias=TEST_ALIAS)

    assert msg.msg_type == 'complete'
    assert msg.devid == TEST_DEVID
    assert msg.alias == TEST_ALIAS


def test_excavation_msg():
    msg = notif.ExcavationMessage(devid=TEST_DEVID, alias=TEST_ALIAS)

    assert msg.msg_type == 'alert'
    assert msg.devid == TEST_DEVID
    assert msg.alias == TEST_ALIAS


def test_inclination_msg():
    msg = notif.InclinationMessage(devid=TEST_DEVID, alias=TEST_ALIAS)

    assert msg.msg_type == 'inclination'
    assert msg.devid == TEST_DEVID
    assert msg.alias == TEST_ALIAS


def test_send_notif():
    msg = notif.InclinationMessage(devid=TEST_DEVID, alias=TEST_ALIAS)
    notif.send_by_tokens(message=msg, tokens=['invalid_token'])
