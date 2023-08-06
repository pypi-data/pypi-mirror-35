name = "pyajax"

def buildscript(config):
    script  = "<script type='text/javascript'>"
    script += "$(function() {"

    for callback in config:
        uinputs = list(("'%s': $('#%s').val()" % (key, val)) for key, val in callback['handler']['input'].items())
        actions = list(("$('#%s').html(response.%s);" % (key, val)) for key, val in callback['handler']['action'].items())

        script += """
        $('#%s').bind('%s', function() {
            $.getJSON('%s', %s).done(function(response){%s});
            return false;
        });
        """ % (callback['handler']['event']['target'], 
               callback['handler']['event']['method'], 
               callback['handler']['event']['url'],
               "{"+",".join(uinputs)+"}",
               "".join(actions))

    script += "});" 
    script += "</script>" 

    return script