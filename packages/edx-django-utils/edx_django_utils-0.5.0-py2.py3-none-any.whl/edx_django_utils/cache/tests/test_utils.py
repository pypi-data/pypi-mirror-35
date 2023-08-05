"""
Tests for the request cache.
"""
# pylint: disable=missing-docstring

from unittest import TestCase

import mock
from edx_django_utils.cache.utils import (
    DEFAULT_REQUEST_CACHE_NAMESPACE,
    SHOULD_FORCE_CACHE_MISS_KEY,
    CachedResponse,
    CachedResponseError,
    RequestCache,
    TieredCache
)

TEST_KEY = "clobert"
TEST_KEY_2 = "clobert2"
EXPECTED_VALUE = "bertclob"
EXPECTED_VALUE_2 = "bertclob2"
TEST_NAMESPACE = "test_namespace"
TEST_DJANGO_TIMEOUT_CACHE = 1


class TestRequestCache(TestCase):
    def setUp(self):
        RequestCache.clear_all_namespaces()
        self.request_cache = RequestCache()
        self.other_request_cache = RequestCache(TEST_NAMESPACE)

    def test_get_cached_response_hit(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)
        cached_response = self.other_request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

        self.other_request_cache.set(TEST_KEY_2, EXPECTED_VALUE)
        cached_response = self.request_cache.get_cached_response(TEST_KEY_2)
        self.assertTrue(cached_response.is_miss)
        cached_response = self.other_request_cache.get_cached_response(TEST_KEY_2)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)

    def test_get_cached_response_hit_with_cached_none(self):
        self.request_cache.set(TEST_KEY, None)
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertFalse(cached_response.is_miss)
        self.assertEqual(cached_response.value, None)

    def test_get_cached_response_miss(self):
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

    def test_get_cached_response_with_default(self):
        self.request_cache.setdefault(TEST_KEY, EXPECTED_VALUE)
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)

    def test_get_cached_response_with_default_after_set(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE_2)
        self.request_cache.setdefault(TEST_KEY, EXPECTED_VALUE)
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE_2)

    def test_get_cached_response_iter(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.request_cache.set(TEST_KEY_2, EXPECTED_VALUE_2)
        cached_responses = {}
        for cached_response in self.request_cache.items():
            cached_responses[cached_response.key] = cached_response
        self.assertTrue(TEST_KEY in cached_responses)
        self.assertTrue(cached_responses[TEST_KEY].is_hit)
        self.assertEqual(cached_responses[TEST_KEY].value, EXPECTED_VALUE)
        self.assertTrue(TEST_KEY_2 in cached_responses)
        self.assertTrue(cached_responses[TEST_KEY_2].is_hit)
        self.assertEqual(cached_responses[TEST_KEY_2].value, EXPECTED_VALUE_2)

    def test_clear(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.other_request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.request_cache.clear()
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)
        cached_response = self.other_request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)

    def test_clear_all_namespaces(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.other_request_cache.set(TEST_KEY, EXPECTED_VALUE)
        RequestCache.clear_all_namespaces()
        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

        cached_response = self.other_request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

    def test_delete(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.request_cache.set(TEST_KEY_2, EXPECTED_VALUE)
        self.other_request_cache.set(TEST_KEY, EXPECTED_VALUE)
        self.request_cache.delete(TEST_KEY)

        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)
        cached_response = self.request_cache.get_cached_response(TEST_KEY_2)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)
        cached_response = self.other_request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)

    def test_delete_missing_key(self):
        try:
            self.request_cache.delete(TEST_KEY)
        except KeyError:
            self.fail('Deleting a missing key from the request cache should not cause an error.')

    def test_create_request_cache_with_default_namespace(self):
        with self.assertRaises(AssertionError):
            RequestCache(DEFAULT_REQUEST_CACHE_NAMESPACE)


class TestTieredCache(TestCase):
    def setUp(self):
        self.request_cache = RequestCache()
        TieredCache.dangerous_clear_all_tiers()

    def test_get_cached_response_all_tier_miss(self):
        cached_response = TieredCache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

    def test_get_cached_response_request_cache_hit(self):
        self.request_cache.set(TEST_KEY, EXPECTED_VALUE)
        cached_response = TieredCache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)

    @mock.patch('django.core.cache.cache.get')
    def test_get_cached_response_django_cache_hit(self, mock_cache_get):
        mock_cache_get.return_value = EXPECTED_VALUE
        cached_response = TieredCache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)

        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_hit, 'Django cache hit should cache value in request cache.')

    @mock.patch('django.core.cache.cache.get')
    def test_get_cached_response_force_django_cache_miss(self, mock_cache_get):
        self.request_cache.set(SHOULD_FORCE_CACHE_MISS_KEY, True)
        mock_cache_get.return_value = EXPECTED_VALUE
        cached_response = TieredCache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss)

        cached_response = self.request_cache.get_cached_response(TEST_KEY)
        self.assertTrue(cached_response.is_miss, 'Forced Django cache miss should not cache value in request cache.')

    @mock.patch('django.core.cache.cache.set')
    def test_set_all_tiers(self, mock_cache_set):
        mock_cache_set.return_value = EXPECTED_VALUE
        TieredCache.set_all_tiers(TEST_KEY, EXPECTED_VALUE, TEST_DJANGO_TIMEOUT_CACHE)
        mock_cache_set.assert_called_with(TEST_KEY, EXPECTED_VALUE, TEST_DJANGO_TIMEOUT_CACHE)
        self.assertEqual(self.request_cache.get_cached_response(TEST_KEY).value, EXPECTED_VALUE)

    @mock.patch('django.core.cache.cache.clear')
    def test_dangerous_clear_all_tiers_and_namespaces(self, mock_cache_clear):
        TieredCache.set_all_tiers(TEST_KEY, EXPECTED_VALUE)
        TieredCache.dangerous_clear_all_tiers()
        self.assertTrue(self.request_cache.get_cached_response(TEST_KEY).is_miss)
        mock_cache_clear.assert_called_once_with()

    @mock.patch('django.core.cache.cache.delete')
    def test_delete(self, mock_cache_delete):
        TieredCache.set_all_tiers(TEST_KEY, EXPECTED_VALUE)
        TieredCache.set_all_tiers(TEST_KEY_2, EXPECTED_VALUE)
        TieredCache.delete_all_tiers(TEST_KEY)
        self.assertTrue(self.request_cache.get_cached_response(TEST_KEY).is_miss)
        self.assertEqual(self.request_cache.get_cached_response(TEST_KEY_2).value, EXPECTED_VALUE)
        mock_cache_delete.assert_called_with(TEST_KEY)


class CacheResponseTests(TestCase):
    def test_is_miss(self):
        is_miss = True
        cached_response = CachedResponse(is_miss, TEST_KEY, EXPECTED_VALUE)
        self.assertTrue(cached_response.is_miss)
        self.assertFalse(cached_response.is_hit)
        self.assertEqual(cached_response.key, TEST_KEY)
        with self.assertRaises(AttributeError):
            cached_response.value  # pylint: disable=pointless-statement
        self.assertEqual(cached_response.get_value_or_default(EXPECTED_VALUE_2), EXPECTED_VALUE_2)
        self.assertIn('CachedResponse(is_miss={}, key={}'.format(True, TEST_KEY), cached_response.__repr__())

    def test_is_hit(self):
        is_miss = False
        cached_response = CachedResponse(is_miss, TEST_KEY, EXPECTED_VALUE)
        self.assertFalse(cached_response.is_miss)
        self.assertTrue(cached_response.is_hit)
        self.assertEqual(cached_response.key, TEST_KEY)
        self.assertEqual(cached_response.value, EXPECTED_VALUE)
        self.assertEqual(cached_response.get_value_or_default(EXPECTED_VALUE_2), EXPECTED_VALUE)
        self.assertIn('CachedResponse(is_miss={}, key={}'.format(False, TEST_KEY), cached_response.__repr__())

    def test_cached_response_equals(self):
        self.assertEqual(
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE),
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE),
        )
        self.assertEqual(
            CachedResponse(True, TEST_KEY, EXPECTED_VALUE),
            CachedResponse(True, TEST_KEY, EXPECTED_VALUE),
        )

        self.assertNotEqual(
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE),
            CachedResponse(True, TEST_KEY, EXPECTED_VALUE),
        )
        self.assertNotEqual(
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE),
            CachedResponse(False, TEST_KEY_2, EXPECTED_VALUE),
        )
        self.assertNotEqual(
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE),
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE_2),
        )

    def test_cached_response_not_equals(self):
        self.assertTrue(
            CachedResponse(False, TEST_KEY, EXPECTED_VALUE) != CachedResponse(False, TEST_KEY, EXPECTED_VALUE_2)
        )

    def test_cached_response_misuse(self):
        cached_response = CachedResponse(False, TEST_KEY, EXPECTED_VALUE)

        with self.assertRaises(CachedResponseError):
            bool(cached_response)

        with self.assertRaises(CachedResponseError):
            # For Python 3
            cached_response.__bool__()

        with self.assertRaises(CachedResponseError):
            other_object = object()
            cached_response == other_object  # pylint: disable=pointless-statement
