Feature: Match measurements with different temporal and spatial properties

    Matched measurements might have different geometry, it can be:
        * point
        * transect
        * vertical profile
        * single layer 2d swath or geostationary field
        * multi-layer 2d swath or geostationary field

    Common scenarios include scenarios when observations "A" might have
    different amount of pixels matching single pixel of observations "B".

    Matched measurements might have different temporal resolution, meaning that
    for a single FOV of measurement "A" we want to match a series of
    observations "B", taken within the certain time window.

    Scenario: Ground 3hr precipitation measurements matched with two orbits
        When we match a measurement made every three hours
        And we match a series of instanteneous satellite observation
        Then we can aggregate all available satellite observations within 200 minutes interval

    Scenario: Match coarse observations with fine observations
        Given we match a measurement with coarse spatial resolution
        When we match a measurement with 10x finer spatial resolution
        Then we receive a matchup with a ratio of ~ 1 to 10 observation length

    Scenario: Match measurements with different temporal and spatial resolution
        Given we have point measurement with fine temporal resolution
        When we match a measurement with coarse temporal resolution
        Then we receive a matchup with a ratio of 1 to 10 observations length in time
        Then we receive a matchup with a ration of 10 to 1 observations length in space
