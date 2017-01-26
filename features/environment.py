# use environment.py for seting up and tearing down scenarios

def after_step(context, step):
    if step.status == "failed":
        # WORKMARK: Start the debugger here.
        # -- LIKE: But need to refocus on error position (missing here).
        import ipdb
        ipdb.set_trace()
        ipdb.pm()
