
 (c) Matteo Corti, ETH Zurich, 2009-2012
 (c) Matteo Corti, 2009-2021

  see AUTHORS for the complete list of contributors

# check_procs_multi

check_procs_multi is a Nagios plugin similar to check_procs able to
check several processes at once.

## Installation

Installation instructions are contained in the INSTALL file

## Nagiosgrapher

Some hints and comments about the usage of the plugin with
Nagiosgrapher

1. plugin name

   Beware that if you are using Nagiosgrapher, the tool is not able to
   distinguish between check_procs and check_procs_multi (since it looks
   for PROCS in the plugin name).

   To avoid the problem you can just rename the name of the plugin in the
   output:

   ```
   $ check_procs_multi [arguments] | sed -e 's/CHECK_PROCS_MULTI/MULTIPROC/g'
   ```

2. adding and removing checks

   If you change the monitored processes and change the corresponding
   Nagiosgrapher template the data file (RRD) will not be updated. You
   will have to delete the .rrd file (losing all the data) or modify it
   (e.g., by using a Perl script and ```RRD::Simple```).

   Example script (by Marcus Schopen):

   ```
   #!/usr/bin/perl

   use strict;
   use warnings;

   use RRD::Simple;

   my $rrd = RRD::Simple->new();

   $rrd->add_source( '/path/file.rrd', 'APACHE2' => 'GAUGE' );
   ```