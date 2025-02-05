import pytest
from freezegun import freeze_time
from google.appengine.ext import ndb
from pyre_extensions import none_throws

from backend.common.helpers.event_team_updater import EventTeamUpdater
from backend.common.models.event import Event
from backend.common.models.event_team import EventTeam
from backend.common.models.team import Team


@pytest.fixture(autouse=True)
def auto_add_ndb_stub(ndb_stub, memcache_stub, test_data_importer) -> None:
    test_data_importer.import_event(__file__, "data/2012ct.json")
    test_data_importer.import_match_list(__file__, "data/2012ct_matches.json")


@freeze_time("2010-01-01")
def test_update_future() -> None:
    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert et_keys_to_delete == set()

    event_team = EventTeam(
        id="%s_%s" % ("2012ct", "frc9999"),
        event=ndb.Key(Event, "2012ct"),
        team=ndb.Key(Team, "frc9999"),
        year=2012,
    )
    event_team.put()

    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert set([et_key.id() for et_key in et_keys_to_delete]) == set()


@freeze_time("2012-06-01")
def test_update_past() -> None:
    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert et_keys_to_delete == set()

    event_team = EventTeam(
        id="%s_%s" % ("2012ct", "frc9999"),
        event=ndb.Key(Event, "2012ct"),
        team=ndb.Key(Team, "frc9999"),
        year=2012,
    )
    event_team.put()

    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert (
        set([et_key.string_id() for et_key in et_keys_to_delete]).symmetric_difference(
            {"2012ct_frc9999"}
        )
        == set()
    )


@freeze_time("2015-01-01")
def test_update_pastyear() -> None:
    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert et_keys_to_delete == set()

    event_team = EventTeam(
        id="%s_%s" % ("2012ct", "frc9999"),
        event=ndb.Key(Event, "2012ct"),
        team=ndb.Key(Team, "frc9999"),
        year=2012,
    )
    event_team.put()

    teams, event_teams, et_keys_to_delete = EventTeamUpdater.update("2012ct")
    assert (
        set([team.team_number for team in teams]).symmetric_difference(
            {
                95,
                178,
                176,
                1922,
                173,
                2785,
                228,
                177,
                1099,
                175,
                1027,
                3017,
                1493,
                118,
                229,
                2791,
                155,
                549,
                195,
                4134,
                20,
                2836,
                869,
                1665,
                4055,
                3555,
                126,
                1699,
                1559,
                3464,
                2168,
                3461,
                1991,
                3467,
                2067,
                230,
                1124,
                3104,
                236,
                237,
                1511,
                250,
                1880,
                558,
                694,
                571,
                3634,
                3525,
                999,
                181,
                1073,
                3146,
                1071,
                1740,
                3719,
                3718,
                2170,
                663,
                4122,
                3182,
                839,
                1784,
                3654,
                743,
            }
        )
        == set()
    )
    assert (
        set([et.key_name for et in none_throws(event_teams)]).symmetric_difference(
            {
                "2012ct_frc95",
                "2012ct_frc178",
                "2012ct_frc176",
                "2012ct_frc1922",
                "2012ct_frc173",
                "2012ct_frc2785",
                "2012ct_frc228",
                "2012ct_frc177",
                "2012ct_frc1099",
                "2012ct_frc175",
                "2012ct_frc1027",
                "2012ct_frc3017",
                "2012ct_frc1493",
                "2012ct_frc118",
                "2012ct_frc229",
                "2012ct_frc2791",
                "2012ct_frc155",
                "2012ct_frc549",
                "2012ct_frc195",
                "2012ct_frc4134",
                "2012ct_frc20",
                "2012ct_frc2836",
                "2012ct_frc869",
                "2012ct_frc1665",
                "2012ct_frc4055",
                "2012ct_frc3555",
                "2012ct_frc126",
                "2012ct_frc1699",
                "2012ct_frc1559",
                "2012ct_frc3464",
                "2012ct_frc2168",
                "2012ct_frc3461",
                "2012ct_frc1991",
                "2012ct_frc3467",
                "2012ct_frc2067",
                "2012ct_frc230",
                "2012ct_frc1124",
                "2012ct_frc3104",
                "2012ct_frc236",
                "2012ct_frc237",
                "2012ct_frc1511",
                "2012ct_frc250",
                "2012ct_frc1880",
                "2012ct_frc558",
                "2012ct_frc694",
                "2012ct_frc571",
                "2012ct_frc3634",
                "2012ct_frc3525",
                "2012ct_frc999",
                "2012ct_frc181",
                "2012ct_frc1073",
                "2012ct_frc3146",
                "2012ct_frc1071",
                "2012ct_frc1740",
                "2012ct_frc3719",
                "2012ct_frc3718",
                "2012ct_frc2170",
                "2012ct_frc663",
                "2012ct_frc4122",
                "2012ct_frc3182",
                "2012ct_frc839",
                "2012ct_frc1784",
                "2012ct_frc3654",
                "2012ct_frc743",
            }
        )
        == set()
    )
    assert et_keys_to_delete == set()
