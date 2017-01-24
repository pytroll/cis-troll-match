Feature: Reduce the amount of measurements used to find matchups

    Before getting to actual matchup lookup the original data should be
    reduced to the minimum. It can be achived by both, limiting the amount of
    observations by time interval as well as to limiting the amount of data by
    space (e.g. excluding everything outside the intersection of data bounding
    boxes

    Scenario: Reduce data by time
        Given we mach <observation1> with <observation2>
        When we want to limit observations to time interval <interval>
        When we call the reduce_by_time method
        Then the data points with timestamps outside the interval <interval> is omitted

    Scenario: Reduce data by bounding box
        Given we mach <observation1> with <observation2>
        When we want to limit observations to bounding box <bbox>
        When we call the reduce_by_space method
        Then the data points outside the <bbox> is omitted

    Scenario: Reduce to overlapping data
        Given we mach <observation1> with <observation2>
        When we want to limit observations to overlapping observations
        When we call the reduce_by_space method
        Then the data points outside the overlapping area is omitted
