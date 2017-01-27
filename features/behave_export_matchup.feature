Feature: Export resulting matchups

  After collocation is complete the resulting object should contain data
  It should be possible to save the data by simply calling a "export" method

  The output format should either be guessed from the file extension or
  "format" string should be provided

  Scenario: Export netcdf matchups
    Given a matchup object is available
    When export command is called
    And the output format is "netcdf"
    Then a netcdf file should be saved on the disk
