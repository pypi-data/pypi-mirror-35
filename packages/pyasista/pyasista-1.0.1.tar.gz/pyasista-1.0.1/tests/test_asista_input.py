# -*- coding: utf-8 -*-
from pyasista import AsistaInput
from pyasista import Environment

import pytest


def dummy_event():
    return {
        'environment': 'PROD',
        'language': 'TR'
    }


def event_without_session():
    return {
        'environment': 'PROD',
        'language': 'TR',
        'ext_node_id': 'EXT_NODE_ID',
        'serial_number': 'SERIAL_NUMBER',
        'slot_values': [
            '@key=value',
            '@parseocommaoandodoto=ocommaoodoto',
            '@list_slot=1',
            '@list_slot=2'
        ]
    }


def event_with_session():
    return {
        'environment': 'PROD',
        'language': 'TR',
        'session': {
            'key': 'value'
        },
        'is_customer_confirmed': True
    }


def event_with_token():
    return {
        'environment': 'PROD',
        'language': 'TR',
        'token': {
            'access_token': 'ACCESS_TOKEN',
            'asista_refresh_data': 'REFRESH_DATA',
            'asista_refresh_token_uri': 'https://dummy.co/dummy',
            'asista_client_key': 'CLIENT_KEY'
        }
    }


def event_with_token_invalid_url():
    return {
        'environment': 'PROD',
        'language': 'TR',
        'token': {
            'access_token': 'ACCESS_TOKEN',
            'asista_refresh_data': 'REFRESH_DATA',
            'asista_refresh_token_uri': 'INVALID_URL',
            'asista_client_key': 'CLIENT_KEY'
        }
    }


def test_parse_no_dict():
    with pytest.raises(TypeError):
        AsistaInput('Invalid')


def test_parse_event():
    asista_input = AsistaInput(dummy_event())
    assert asista_input.environment == Environment.PROD


def test_parse_with_extra_required():
    required = ['ext_node_id', 'serial_number']
    with pytest.raises(KeyError):
        AsistaInput(dummy_event(), required_parameters=required)

    asista_input = AsistaInput(event_without_session(),
                               required_parameters=required)

    assert asista_input.ext_node_id == 'EXT_NODE_ID'
    assert asista_input.serial_number == 'SERIAL_NUMBER'
    assert isinstance(asista_input.slot_values, dict)

    parameters = asista_input.slot_values
    assert '@key' in parameters
    assert len(parameters['@key']) == 1
    assert parameters['@key'].pop() == 'value'
    assert '@parse,and.' in parameters
    assert parameters['@parse,and.'].pop() == ',.'
    assert '@list_slot' in parameters
    assert len(parameters['@list_slot']) == 2
    assert parameters['@list_slot'].pop() == '2'
    assert parameters['@list_slot'].pop() == '1'

    assert isinstance(asista_input.session, dict)
    assert len(asista_input.session) == 0

    assert asista_input.customer_confirmed is None


def test_parse_with_session():
    asista_input = AsistaInput(event_with_session())

    assert isinstance(asista_input.session, dict)
    assert len(asista_input.session) == 1
    assert 'key' in asista_input.session
    assert asista_input.session['key'] == 'value'

    assert asista_input.customer_confirmed


def test_parse_with_token():
    asista_input = AsistaInput(event_with_token())
    token = asista_input.token

    assert token.is_valid()
    assert token.access_token == 'ACCESS_TOKEN'


def test_parse_with_token_invalid_uri():
    asista_input = AsistaInput(event_with_token_invalid_url())
    token = asista_input.token

    assert not token.is_valid()
