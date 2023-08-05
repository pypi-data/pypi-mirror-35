import json

import pytest
import requests_mock

from django.core.cache import caches

from directory_cms_client import DirectoryCMSClient
from directory_cms_client.version import __version__
from directory_cms_client import helpers


@pytest.fixture
def default_client():
    return DirectoryCMSClient(
        base_url='http://example.com',
        api_key='debug',
        sender_id='test-sender',
        timeout=5,
        service_name='foo'
    )


@pytest.fixture
def cms_cache():
    return caches['cms_fallback']


@pytest.fixture(autouse=True)
def clear_cms_cache(cms_cache):
    cms_cache.clear()


def test_cms_client_list_by_page_type_draft(default_client):
    with requests_mock.mock() as mock:
        mock.get('http://example.com/api/pages/')
        default_client.list_by_page_type('thing', draft_token='draft-token')
        request = mock.request_history[0]

        assert request.qs == {
            'draft_token': ['draft-token'],
            'fields': ['*'],
            'type': ['thing'],
        }


def test_cms_client_lookup_by_slug_language(default_client):
    with requests_mock.mock() as mock:
        mock.get('http://example.com/api/pages/lookup-by-slug/thing/')
        default_client.lookup_by_slug('thing', language_code='de')
        request = mock.request_history[0]

        assert request.qs == {
            'service_name': ['foo'],
            'lang': ['de'],
            'fields': ['*'],
        }


def test_cms_client_lookup_by_slug_draft(default_client):
    with requests_mock.mock() as mock:
        mock.get('http://example.com/api/pages/lookup-by-slug/thing/')
        default_client.lookup_by_slug('thing', draft_token='draft-token')
        request = mock.request_history[0]

        assert request.qs == {
            'service_name': ['foo'],
            'draft_token': ['draft-token'],
            'fields': ['*'],
        }


def test_cms_client_lookup_by_slug(default_client):
    with requests_mock.mock() as mock:
        mock.get('http://example.com/api/pages/lookup-by-slug/thing/')
        default_client.lookup_by_slug('thing')
        request = mock.request_history[0]

        assert request.qs == {
            'service_name': ['foo'],
            'fields': ['*'],
        }


def test_timeout(default_client):
    assert default_client.timeout == 5


def test_sender_id(default_client):
    assert default_client.request_signer.sender_id == 'test-sender'


def test_version():
    assert DirectoryCMSClient.version == __version__


def test_good_response_cached(default_client, cms_cache):
    expected_data = bytes(json.dumps({'key': 'value'}), 'utf8')
    path = '/api/pages/lookup-by-slug/thing/'

    with requests_mock.mock() as mock:
        mock.get('http://example.com' + path, content=expected_data)
        default_client.lookup_by_slug('thing')

    cache_key = path + '?fields=%5B%27%2A%27%5D&service_name=foo'
    assert cms_cache.get(cache_key) == expected_data


def test_bad_resonse_cache_hit(default_client, caplog):
    path = '/api/pages/lookup-by-slug/thing/'
    expected_data = bytes(json.dumps({'key': 'value'}), 'utf8')
    url = 'http://example.com' + path

    with requests_mock.mock() as mock:
        mock.get(url, content=expected_data)
        response_one = default_client.lookup_by_slug('thing')

    with requests_mock.mock() as mock:
        mock.get(url, status_code=400)
        response_two = default_client.lookup_by_slug('thing')

    assert response_one.status_code == 200
    assert response_one.content == expected_data
    assert isinstance(response_one, helpers.CMSLiveResponse)

    assert response_two.status_code == 200
    assert response_two.content == expected_data
    assert isinstance(response_two, helpers.CMSCacheResponse)

    log = caplog.records[-1]
    assert log.levelname == 'WARNING'
    assert log.msg == helpers.MESSAGE_CACHE_HIT
    assert log.status_code == 400
    assert log.url == path


def test_bad_response_cache_miss(default_client, caplog):
    path = '/api/pages/lookup-by-slug/thing/'
    url = 'http://example.com' + path

    with requests_mock.mock() as mock:
        mock.get(url, status_code=400)
        response = default_client.lookup_by_slug('thing')

    assert response.status_code == 400
    assert isinstance(response, helpers.CMSFailureResponse)

    log = caplog.records[-1]
    assert log.levelname == 'ERROR'
    assert log.msg == helpers.MESSAGE_CACHE_MISS
    assert log.status_code == 400
    assert log.url == path


def test_cache_querystrings(default_client, cms_cache):
    expected_data = bytes(json.dumps({'key': 'value'}), 'utf8')
    path = '/api/pages/lookup-by-slug/thing/'

    with requests_mock.mock() as mock:
        mock.get('http://example.com' + path, content=expected_data)
        default_client.lookup_by_slug(
            'thing',
            language_code='de',
            draft_token='2'
        )

    cache_key = (
        path + '?draft_token=2&fields=%5B%27%2A%27%5D&lang=de&service_name=foo'
    )
    assert cms_cache.get(cache_key) == expected_data
