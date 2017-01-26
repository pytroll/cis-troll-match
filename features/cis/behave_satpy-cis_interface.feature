Feature:  Provide interface between CIS and Satpy

    Use satpy to read datasets and pass it to CIS for collocation and exporting the
    resulting matchups with CIS as a CF compliant NetCDF file.

    @cis
    Scenario: Pass satpy scene object to CIS
        When there satpy scene is available
        And satpy scene contains dataset
        Then make CIS Ungridded dataset out of it


