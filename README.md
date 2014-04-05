ceiloplot ALPHA
===============

Create a [gnuplot](http://www.gnuplot.info/) from a
[OpenStack Ceilometer](https://wiki.openstack.org/wiki/Heat) metric.

Please keep in mind that this script is in an early alpha stage, so use this tool with care.

## Example 

Assuming that the openstack credentials have been set as environment
variables (see 'Usage' for further details).

`$ python ceiloplot.py -m network.incoming.packets.rate --gnuplot-terminal "pngcairo" --gnuplot-output "packet_rate.png" | gnuplot`

And voilà: Here we have a nice plot of our data.

![Sample plot network.incoming.packets.rate](http://i.imgur.com/eqpdt3u.png)

Ceiloplot will create a line for each resource.

## Usage

    usage: ceiloplot [-h] [--os-username OS_USERNAME] [--os-password OS_PASSWORD]
                     [--os-tenant-id OS_TENANT_ID]
                     [--os-tenant-name OS_TENANT_NAME] [--os-auth-url OS_AUTH_URL]
                     --meter METER [--limit LIMIT]
                     [--gnuplot-terminal GNUPLOT_TERMINAL]
                     [--gnuplot-output GNUPLOT_OUTPUT] [-o OUTPUT]

    Creates a gnuplot from ceilometer

    optional arguments:
      -h, --help            show this help message and exit
      --os-username OS_USERNAME
                            Defaults to env[OS_USERNAME].
      --os-password OS_PASSWORD
                            Defaults to env[OS_PASSWORD].
      --os-tenant-id OS_TENANT_ID
                            Defaults to env[OS_TENANT_ID].
      --os-tenant-name OS_TENANT_NAME
                            Defaults to env[OS_TENANT_NAME].
      --os-auth-url OS_AUTH_URL
                            Defaults to env[OS_AUTH_URL].
      --meter METER, -m METER
                            The meter to use.
      --limit LIMIT, -l LIMIT
                            The maximum number of samples.
      --gnuplot-terminal GNUPLOT_TERMINAL, -t GNUPLOT_TERMINAL
                            terminal options passed to gnuplot.
      --gnuplot-output GNUPLOT_OUTPUT, -g GNUPLOT_OUTPUT
                            output options passed to gnuplot.
      -o OUTPUT, --output OUTPUT
                            Redirect the gnuplot script to the specified file.
