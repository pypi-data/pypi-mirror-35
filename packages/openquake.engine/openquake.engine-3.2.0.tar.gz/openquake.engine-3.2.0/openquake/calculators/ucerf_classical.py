# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2018 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
import logging
import operator

from openquake.baselib import parallel
from openquake.hazardlib.calc.hazard_curve import classical
from openquake.commonlib import source

from openquake.calculators import base
from openquake.calculators.classical import ClassicalCalculator
from openquake.calculators.ucerf_base import UcerfFilter
# FIXME: the counting of effective ruptures has to be revised


@base.calculators.add('ucerf_classical')
class UcerfClassicalCalculator(ClassicalCalculator):
    """
    UCERF classical calculator.
    """
    def pre_execute(self):
        super().pre_execute()
        self.csm_info = self.csm.info
        self.src_filter = UcerfFilter(
            self.sitecol, self.oqparam.maximum_distance)
        for sm in self.csm.source_models:  # one branch at the time
            [grp] = sm.src_groups
            for src in grp:
                self.csm.infos[src.source_id] = source.SourceInfo(src)
                grp.tot_ruptures += src.num_ruptures

    def execute(self):
        """
        Run in parallel `core_task(sources, sitecol, monitor)`, by
        parallelizing on the sources according to their weight and
        tectonic region type.
        """
        monitor = self.monitor(self.core_task.__name__)
        oq = self.oqparam
        acc = self.zerodict()
        self.nsites = []  # used in agg_dicts
        param = dict(imtls=oq.imtls, truncation_level=oq.truncation_level,
                     filter_distance=oq.filter_distance)
        for sm in self.csm.source_models:  # one branch at the time
            [grp] = sm.src_groups
            gsims = self.csm.info.get_gsims(sm.ordinal)
            acc = parallel.Starmap.apply(
                classical, (grp, self.src_filter, gsims, param, monitor),
                weight=operator.attrgetter('weight'),
                concurrent_tasks=oq.concurrent_tasks,
            ).reduce(self.agg_dicts, acc)
            ucerf = grp.sources[0].orig
            logging.info('Getting background sources from %s', ucerf.source_id)
            srcs = ucerf.get_background_sources(self.src_filter)
            for src in srcs:
                self.csm.infos[src.source_id] = source.SourceInfo(src)
            acc = parallel.Starmap.apply(
                classical, (srcs, self.src_filter, gsims, param, monitor),
                weight=operator.attrgetter('weight'),
                concurrent_tasks=oq.concurrent_tasks,
            ).reduce(self.agg_dicts, acc)

        with self.monitor('store source_info', autoflush=True):
            self.store_source_info(self.csm.infos, acc)
        return acc  # {grp_id: pmap}
