""" Creates a gnuplot from ceilometer
"""
from ceilometerclient import client as ceiloclient
import argparse
import sys
import os


class Ceiloplot():

    API_VERSION = "2"

    def get_ceilometer_client(self):
        return ceiloclient.get_client(
            Ceiloplot.API_VERSION,
            os_username=self.args.os_username,
            os_password=self.args.os_password,
            os_auth_url=self.args.os_auth_url,
            os_tenant_id=self.args.os_tenant_id
        )

    def parse_args(self, argv):
        parser = argparse.ArgumentParser(
            prog='ceiloplot',
            description=__doc__.strip(),
            add_help=True
        )

        parser.add_argument('--os-username',
                            default=os.environ.get('OS_USERNAME'),
                            help='Defaults to env[OS_USERNAME].')

        parser.add_argument('--os-password',
                            default=os.environ.get('OS_PASSWORD'),
                            help='Defaults to env[OS_PASSWORD].')

        parser.add_argument('--os-tenant-id',
                            default=os.environ.get('OS_TENANT_ID'),
                            help='Defaults to env[OS_TENANT_ID].')

        parser.add_argument('--os-tenant-name',
                            default=os.environ.get('OS_TENANT_NAME'),
                            help='Defaults to env[OS_TENANT_NAME].')

        parser.add_argument('--os-auth-url',
                            default=os.environ.get('OS_AUTH_URL'),
                            help='Defaults to env[OS_AUTH_URL].')
        parser.add_argument('--meter', '-m',
                            required=True,
                            help='The meter to use')

        parser.add_argument('--limit', '-l',
                            help='The maximum number of samples.')

        parser.add_argument('-o', '--output',
                            default='ceiloplot.gp',
                            help='Filename of the gnuplot file')

        self.args = parser.parse_args(argv)

    def main(self, argv):
        self.parse_args(argv)
        client = self.get_ceilometer_client()
        unit = None
        samples = client.samples.list(
            meter_name=self.args.meter,
            limit=self.args.limit
        )

        if len(samples) == 0:
            print "warning: empty dataset"

        units = set([])
        resources = set([])

        for sample in samples:
            units.add(sample.counter_unit)
            resources.add(sample.resource_id)

        print "info: this dataset contains %d resources" % len(resources)

        if len(units) > 1:
            raise Exception("You cannot mix different units.")

        with file(self.args.output, "w") as w:
            if len(units) == 1:
                w.write('set ylabel "%s"\n' % units.pop())
            plots = []

            for resource in resources:
                plots.append('"-" using 1:2 with lines title "%s"' % resource)

            w.write('set title "%s"\n' % self.args.meter)
            w.write('set xtics rotate by -90\n')
            w.write('set xdata time\n')
            w.write('set timefmt \'%Y-%m-%dT%H:%M:%S\'\n')
            w.write('plot %s\n' % ",".join(plots))

            for resource in resources:
                for i in reversed(range(0, len(samples))):
                    if samples[i].resource_id == resource:
                        w.write('%s %s\n' % (
                            samples[i].recorded_at,
                            samples[i].counter_volume)
                        )
                w.write('EOF\n')

            print "file with %d samples written to %s" % (
                len(samples),
                self.args.output
            )

if __name__ == "__main__":
    Ceiloplot().main(sys.argv[1:])
