ceiloplot
=========

Create a [gnuplot](http://www.gnuplot.info/) from a
[OpenStack Ceilometer](https://wiki.openstack.org/wiki/Heat) metric.

## Example 

Assuming that the openstack credentials have been set as environment
variables (see 'Usage' for further details).

`$ python ceiloplot.py -m network.incoming.packets.rate`

Ceiloplot created an output file `ceiloplot.gp` which we now can run with gnuplot:

`gnuplot -p ceiloplot.gp`

And voilà: Here we have a nice plot of our data

[Imgur](http://i.imgur.com/eqpdt3u.png)

## Usage

    usage: python ceiloplot.py [-h] [--os-username OS_USERNAME] [--os-password OS_PASSWORD]
                     [--os-tenant-id OS_TENANT_ID]
                     [--os-tenant-name OS_TENANT_NAME] [--os-auth-url OS_AUTH_URL]
                     --meter METER [--limit LIMIT] [-o OUTPUT]
    
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
                            The meter to use
      --limit LIMIT, -l LIMIT
                            The maximum number of outputs.
      -o OUTPUT, --output OUTPUT
                            Filename of the gnuplot file
