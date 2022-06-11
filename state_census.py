import csv
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
INDIAN_CENSUS_DATA = BASE_DIR / "indian_census_data.csv"


class StateCensusAnalyser:
    """Contains varies method like check no of records in file, check file name, check file extension etc"""

    @staticmethod
    def check_no_of_record_from_file(file_name):
        """Checks number of records in the file"""

        with open(file_name) as my_file:
            count = 0
            for i in my_file:
                count += 1
        return count


def check_file_extension(file_name):
    """Check for file extension is invalid"""
    try:
        if pathlib.Path(file_name).suffix == ".csv":
            print("Valid file extension")
    except Exception as e:
        print("Incorrect file header")


def check_delimeter(file_name, delimeter_input):
    """Check for file delimeter is invalid"""
    try:
        sniffer = csv.Sniffer()
        # dialect = sniffer.sniff(file_name, delimiters=',')
        with open(file_name) as file:
            delimeter = sniffer.sniff(file.readline(1)).delimiter
        if delimeter == delimeter_input:
            return "Valid file delimeter"
    except Exception as e:
        print("Invalid file delimeter")


def check_file_header(file_header, file_name):
    """Check for file header is invalid"""
    try:
        with open(file_name) as my_file:
            for i in my_file:
                if i.__contains__(file_header):
                    return "Header is correct"
    except Exception as e:
        print("Incorrect company name ", e)


def check_file_name(file, file_name):
    """Checks for file name is invalid"""
    try:
        # with open(INDIAN_CENSUS_DATA) as my_file:
        name, ext = file.name.split('.')
        if name == file_name:
            return "Valid file name"
    except Exception as e:
        print("Invalid file name")


if __name__ == '__main__':
    try:
        print(StateCensusAnalyser.check_no_of_record_from_file(INDIAN_CENSUS_DATA))
        print(check_file_name(INDIAN_CENSUS_DATA, "indian_census_data"))
        print(check_file_extension(INDIAN_CENSUS_DATA))
        print(check_delimeter(INDIAN_CENSUS_DATA, ','))
        print(check_file_header("State,Population,AreaInSqKm,DensityPerSqKm,StateCode",
                                                    INDIAN_CENSUS_DATA))
    except Exception as e:
        print(e)
