Feature: Simulate granules coverage to find granules for downloading

    When users have a set of coordinates (point, transect, 2d measurement)
    we need to find out the granules with overlapping observations
    For that we need to compute the coverage based on online TLE information
    Once the coverage is computed return the list of files which can be
    downloaded using and API provided by the user. The same list of files
    is useful in case the granules are available on users' disk locally.

    @wip
    Scenario: Get filename for a single granule over a single point
        When we have a single point measurement
        And we have an object that describes satellite observations
        And we look for the closest overpass to the current timestamp
        Then we receive a list of overpassing granule filenames

    # Scenario: Get filename for a single granule over a transect
    #     When we have a transect measurement
    #     And we look for the closest overpass to the particular timestamp
    #     Then we receive a filename
    #
    # Scenario: Get filename for a single granule over a polygon
    #     When we have a rectangular measurement
    #     And we look for the closest overpass to the particular timestamp
    #     Then we receive a filename
