import pytest
import module.spotify_tools as spotify

def test_module():
    assert spotify.get_related_artists_dict("test")
    