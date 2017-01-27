Feature: Allow to apply various corrections to unreduced data

    One example is parallax correction.
    Since such correction will affect the value of pixel coordinates
    the correction should be apply before the reduction of the data by space

    The correction or flagging is done in satpy readers


    Scenario: Apply parallax correction
        Given We have a file with cloud top height data available
        When the file is loaded
        Then parallax correction is applied

    Scenario: Apply custom quality flags
        Given We have a file with quality flags is available
        When the file is loaded
        Then quality flags are applied
