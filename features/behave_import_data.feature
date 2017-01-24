Feature: Input formats

    The software should be able to read certain number of data products
    (observatons)/formats:

    1st priority
    ------------
        * MODIS L1B (indicate the sensor or product)
        * AVHRR L1B (GAC and LAC)
        * VIIRS SDR
        * MSG
        * HIMAWARI
        * GOES-R,
        * NWC SAF PPS products (v2014 and v2018)
        * GEO NWC SAF products (cloud products only)
        * CM SAF (cloud products), # indicate
        * MODIS L2 (collection 5 (priority 2) and 6 (priority 1)):
             * cloud products # indicate
             * aerosol products
        * OCA format (discuss with Phil to identify the format version)

    2nd priority
    ------------
        * AMSR(E/2)
        * IASI
        * HIRS
        * AMSU
        * MHS
        * CrIS
        * AIRS
        * CryoSAT
        * Sentinel(1,2,3)
        * A-Train products L2 (prio 1)
        * Caliop
        * CloudSat (CMR) products (L2)
        * Dardar

    Data with different geometries
    ------------------------------
        * Points
        * profiles
        * transects (priority 2)
        * SYNOP
        * Aeronet
        * buoys
        * aerial transects

    PPS intermediate output format (Nina)
    -------------------------------------


    TODO: add instruments please if there are satellite names only
    TODO: add scenarios
