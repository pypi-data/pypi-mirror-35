# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from moto import mock_s3
import boto3

import json


from taar.recommenders import LocaleRecommender
from taar.recommenders.lazys3 import LazyJSONLoader
from taar.recommenders.locale_recommender import ADDON_LIST_BUCKET, ADDON_LIST_KEY


FAKE_LOCALE_DATA = {
    "te-ST": [
        "{1e6b8bce-7dc8-481c-9f19-123e41332b72}", "some-other@nice-addon.com",
        "{66d1eed2-a390-47cd-8215-016e9fa9cc55}", "{5f1594c3-0d4c-49dd-9182-4fbbb25131a7}"
    ],
    "en": [
        "some-uuid@test-addon.com", "other-addon@some-id.it"
    ]
}


def install_mock_data(ctx):
    ctx = ctx.child()
    conn = boto3.resource('s3', region_name='us-west-2')

    conn.create_bucket(Bucket=ADDON_LIST_BUCKET)
    conn.Object(ADDON_LIST_BUCKET, ADDON_LIST_KEY).put(Body=json.dumps(FAKE_LOCALE_DATA))
    ctx['locale_mock_data'] = LazyJSONLoader(ctx,
                                             ADDON_LIST_BUCKET,
                                             ADDON_LIST_KEY)

    return ctx


@mock_s3
def test_can_recommend(test_ctx):
    ctx = install_mock_data(test_ctx)
    r = LocaleRecommender(ctx)

    # Test that we can't recommend if we have not enough client info.
    assert not r.can_recommend({})
    assert not r.can_recommend({"locale": []})

    # Check that we can recommend if the user has at least an addon.
    assert r.can_recommend({"locale": "en"})


@mock_s3
def test_can_recommend_no_model(test_ctx):
    ctx = install_mock_data(test_ctx)
    r = LocaleRecommender(ctx)

    # We should never be able to recommend if something went
    # wrong with the model.
    assert not r.can_recommend({})
    assert not r.can_recommend({"locale": []})
    assert not r.can_recommend({"locale": "it"})


@mock_s3
def test_recommendations(test_ctx):
    """Test that the locale recommender returns the correct
    locale dependent addons.

    The JSON output for this recommender should be a list of 2-tuples
    of (GUID, weight).
    """
    ctx = install_mock_data(test_ctx)
    r = LocaleRecommender(ctx)
    recommendations = r.recommend({"locale": "en"}, 10)

    # Make sure the structure of the recommendations is correct and that we
    # recommended the the right addon.
    assert isinstance(recommendations, list)
    assert len(recommendations) == len(FAKE_LOCALE_DATA["en"])

    # Make sure that the reported addons are the one from the fake data.
    for (addon_id, weight) in recommendations:
        assert 1 == weight
        assert addon_id in FAKE_LOCALE_DATA["en"]


@mock_s3
def test_recommender_extra_data(test_ctx):
    # Test that the recommender uses locale data from the "extra"
    # section if available.
    def validate_recommendations(data, expected_locale):
        # Make sure the structure of the recommendations is correct and that we
        # recommended the the right addon.
        assert isinstance(data, list)
        assert len(data) == len(FAKE_LOCALE_DATA[expected_locale])

        # Make sure that the reported addons are the one from the fake data.
        for (addon_id, weight) in data:
            assert addon_id in FAKE_LOCALE_DATA[expected_locale]
            assert 1 == weight

    ctx = install_mock_data(test_ctx)
    r = LocaleRecommender(ctx)
    recommendations = r.recommend({}, 10, extra_data={"locale": "en"})
    validate_recommendations(recommendations, "en")

    # Make sure that we favour client data over the extra data.
    recommendations = r.recommend({"locale": "en"}, 10, extra_data={"locale": "te-ST"})
    validate_recommendations(recommendations, "en")
