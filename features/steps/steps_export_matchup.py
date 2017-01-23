import os
from trollmatch import match

@given(u'a matchup object is available')
def step_impl(context):
    context.matchup = match.Matchup()

@when(u'the output format is "netcdf"')
def step_impl(context):
    context.matchup.output_format = "netcdf"

@when(u'export command is called')
def step_impl(context):
    context.matchup.output_filepath = '/tmp/o.nc4'
    context.matchup.export(context.matchup.output_filepath)

@then(u'a netcdf file should be saved on the disk')
def step_impl(context):
    os.path.exists(context.matchup.output_filepath)
    raise NotImplementedError(u'STEP: Then a netcdf file should be saved on the disk')
