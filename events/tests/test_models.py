#test_models.py

import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestJourney:
    def test_init(self):
        obj = mixer.blend('events.Journey')
        assert obj.pk == 1, 'Should save an instance'
