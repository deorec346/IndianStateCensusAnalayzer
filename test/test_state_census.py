import pytest

from state_census import StateCensusAnalyser
from state_census_exception import StateCensusException


class TestIndianCensus:

    @pytest.fixture
    def state(self):
        state = StateCensusAnalyser()
        return state

    def test_check_number_of_records_matches(self, state):
        result = state.check_no_of_record_from_file()
        assert result == 30

    def test_check_file_name_is_invalid(self, state):
        with pytest.raises(StateCensusException) as exception:
            check_file_name("indian_census_data.csv")
        assert "Invalid file name" == exception.value.message

    def test_check_file_extension_is_invalid(self, state):
        with pytest.raises(StateCensusException) as exception:
            state.check_file_extension("indian_census_data.csv")
        assert "Invalid file extension" == exception.value.message


