# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
from pyVmomi import vim

from datadog_checks.vsphere.constants import (
    HISTORICAL,
    REALTIME,
)

# https://code.vmware.com/apis/358/vsphere/doc/cpu_counters.html

# Set of metrics that are emitted as percentages between 0 and 100. For those metrics, we divide the value by 100
# to get a float between 0 and 1.
PERCENT_METRICS = {
    'cpu.capacity.contention.avg',
    'cpu.coreUtilization.avg',
    'cpu.corecount.contention.avg',
    'cpu.demandEntitlementRatio.latest',
    'cpu.latency.avg',
    'cpu.readiness.avg',
    'cpu.usage.avg',
    'cpu.usage.vcpus.avg',
    'cpu.utilization.avg',
    'datastore.siocActiveTimePercentage.avg',
    'disk.capacity.contention.avg',
    'disk.scsiReservationCnflctsPct.avg',
    'gpu.mem.usage.avg',
    'gpu.utilization.avg',
    'mem.capacity.contention.avg',
    'mem.latency.avg',
    'mem.reservedCapacityPct.avg',
    'mem.usage.avg',
    'mem.vmfs.pbc.capMissRatio.latest',
    'power.capacity.usagePct.avg',
    'rescpu.actav1.latest',
    'rescpu.actav15.latest',
    'rescpu.actav5.latest',
    'rescpu.actpk1.latest',
    'rescpu.actpk15.latest',
    'rescpu.actpk5.latest',
    'rescpu.maxLimited1.latest',
    'rescpu.maxLimited15.latest',
    'rescpu.maxLimited5.latest',
    'rescpu.runav1.latest',
    'rescpu.runav15.latest',
    'rescpu.runav5.latest',
    'rescpu.runpk1.latest',
    'rescpu.runpk15.latest',
    'rescpu.runpk5.latest',
    'storageAdapter.OIOsPct.avg',
    'sys.diskUsage.latest',
    'sys.resourceCpuAct1.latest',
    'sys.resourceCpuAct5.latest',
    'sys.resourceCpuMaxLimited1.latest',
    'sys.resourceCpuMaxLimited5.latest',
    'sys.resourceCpuRun1.latest',
    'sys.resourceCpuRun5.latest',
    'vcResources.priviledgedcpuusage.avg',
    'vcResources.processcpuusage.avg',
    'vcResources.systemcpuusage.avg',
    'vcResources.systemnetusage.avg',
    'vcResources.usercpuusage.avg',
    'vsanDomObj.readCacheHitRate.latest',
}

VSAN_PERCENT_METRICS = {
    'congestion',
    'coreUtilPct',
    'pcpuUsedPct',
    'pcpuUtilPct',
}

# All metrics that can be collected from VirtualMachines.
VM_METRICS = {
    REALTIME: [
        'cpu.costop.sum',
        'cpu.demand.avg',
        'cpu.demandEntitlementRatio.latest',
        'cpu.entitlement.latest',
        'cpu.idle.sum',
        'cpu.latency.avg',
        'cpu.maxlimited.sum',
        'cpu.overlap.sum',
        'cpu.readiness.avg',
        'cpu.ready.sum',
        'cpu.run.sum',
        'cpu.swapwait.sum',
        'cpu.system.sum',
        'cpu.usage.avg',
        'cpu.usage.vcpus.avg',
        'cpu.usagemhz.avg',
        'cpu.used.sum',
        'cpu.wait.sum',
        'cpu.capacity.demand.avg',
        'cpu.capacity.usage.avg',
        'cpu.capacity.contention.avg',
        'datastore.maxTotalLatency.latest',
        'datastore.numberReadAveraged.avg',
        'datastore.numberWriteAveraged.avg',
        'datastore.read.avg',
        'datastore.totalReadLatency.avg',
        'datastore.totalWriteLatency.avg',
        'datastore.write.avg',
        'disk.busResets.sum',
        'disk.commands.sum',
        'disk.commandsAborted.sum',
        'disk.commandsAveraged.avg',
        'disk.maxTotalLatency.latest',
        'disk.numberRead.sum',
        'disk.numberReadAveraged.avg',
        'disk.numberWrite.sum',
        'disk.numberWriteAveraged.avg',
        'disk.read.avg',
        'disk.usage.avg',
        'disk.write.avg',
        'hbr.hbrNetRx.avg',
        'hbr.hbrNetTx.avg',
        'mem.active.avg',
        'mem.activewrite.avg',
        'mem.compressed.avg',
        'mem.compressionRate.avg',
        'mem.consumed.avg',
        'mem.decompressionRate.avg',
        'mem.entitlement.avg',
        'mem.granted.avg',
        'mem.latency.avg',
        'mem.llSwapInRate.avg',
        'mem.llSwapOutRate.avg',
        'mem.llSwapUsed.avg',
        'mem.overhead.avg',
        'mem.overheadMax.avg',
        'mem.overheadTouched.avg',
        'mem.shared.avg',
        'mem.swapin.avg',
        'mem.swapinRate.avg',
        'mem.swapout.avg',
        'mem.swapoutRate.avg',
        'mem.swapped.avg',
        'mem.swaptarget.avg',
        'mem.usage.avg',
        'mem.vmmemctl.avg',
        'mem.vmmemctltarget.avg',
        'mem.zero.avg',
        'mem.zipSaved.latest',
        'mem.zipped.latest',
        'mem.capacity.usage.avg',
        'mem.capacity.contention.avg',
        'net.broadcastRx.sum',
        'net.broadcastTx.sum',
        'net.bytesRx.avg',
        'net.bytesTx.avg',
        'net.droppedRx.sum',
        'net.droppedTx.sum',
        'net.multicastRx.sum',
        'net.multicastTx.sum',
        'net.packetsRx.sum',
        'net.packetsTx.sum',
        'net.pnicBytesRx.avg',
        'net.pnicBytesTx.avg',
        'net.received.avg',
        'net.throughput.usage.avg',
        'net.transmitted.avg',
        'net.usage.avg',
        'power.energy.sum',
        'power.power.avg',
        'rescpu.actav1.latest',
        'rescpu.actav15.latest',
        'rescpu.actav5.latest',
        'rescpu.actpk1.latest',
        'rescpu.actpk15.latest',
        'rescpu.actpk5.latest',
        'rescpu.maxLimited1.latest',
        'rescpu.maxLimited15.latest',
        'rescpu.maxLimited5.latest',
        'rescpu.runav1.latest',
        'rescpu.runav15.latest',
        'rescpu.runav5.latest',
        'rescpu.runpk1.latest',
        'rescpu.runpk15.latest',
        'rescpu.runpk5.latest',
        'rescpu.sampleCount.latest',
        'rescpu.samplePeriod.latest',
        'sys.heartbeat.latest',
        'sys.heartbeat.sum',
        'sys.osUptime.latest',
        'sys.uptime.latest',
        'virtualDisk.busResets.sum',
        'virtualDisk.commandsAborted.sum',
        'virtualDisk.largeSeeks.latest',
        'virtualDisk.mediumSeeks.latest',
        'virtualDisk.numberReadAveraged.avg',
        'virtualDisk.numberWriteAveraged.avg',
        'virtualDisk.read.avg',
        'virtualDisk.readIOSize.latest',
        'virtualDisk.readLatencyUS.latest',
        'virtualDisk.readLoadMetric.latest',
        'virtualDisk.readOIO.latest',
        'virtualDisk.smallSeeks.latest',
        'virtualDisk.totalReadLatency.avg',
        'virtualDisk.totalWriteLatency.avg',
        'virtualDisk.write.avg',
        'virtualDisk.writeIOSize.latest',
        'virtualDisk.writeLatencyUS.latest',
        'virtualDisk.writeLoadMetric.latest',
        'virtualDisk.writeOIO.latest',
    ],
    HISTORICAL: ['disk.used.latest', 'disk.provisioned.latest', 'disk.unshared.latest'],
}

# All metrics that can be collected from ESXi Hosts.
HOST_METRICS = {
    REALTIME: [
        'cpu.coreUtilization.avg',
        'cpu.costop.sum',
        'cpu.demand.avg',
        'cpu.idle.sum',
        'cpu.latency.avg',
        'cpu.readiness.avg',
        'cpu.ready.sum',
        'cpu.reservedCapacity.avg',
        'cpu.swapwait.sum',
        'cpu.totalCapacity.avg',
        'cpu.usage.avg',
        'cpu.usagemhz.avg',
        'cpu.used.sum',
        'cpu.utilization.avg',
        'cpu.wait.sum',
        'cpu.capacity.usage.avg',
        'cpu.capacity.contention.avg',
        'datastore.datastoreIops.avg',
        'datastore.datastoreMaxQueueDepth.latest',
        'datastore.datastoreNormalReadLatency.latest',
        'datastore.datastoreNormalWriteLatency.latest',
        'datastore.datastoreReadBytes.latest',
        'datastore.datastoreReadIops.latest',
        'datastore.datastoreReadLoadMetric.latest',
        'datastore.datastoreReadOIO.latest',
        'datastore.datastoreVMObservedLatency.latest',
        'datastore.datastoreWriteBytes.latest',
        'datastore.datastoreWriteIops.latest',
        'datastore.datastoreWriteLoadMetric.latest',
        'datastore.datastoreWriteOIO.latest',
        'datastore.maxTotalLatency.latest',
        'datastore.numberReadAveraged.avg',
        'datastore.numberWriteAveraged.avg',
        'datastore.read.avg',
        'datastore.siocActiveTimePercentage.avg',
        'datastore.sizeNormalizedDatastoreLatency.avg',
        'datastore.totalReadLatency.avg',
        'datastore.totalWriteLatency.avg',
        'datastore.write.avg',
        'disk.busResets.sum',
        'disk.commands.sum',
        'disk.commandsAborted.sum',
        'disk.commandsAveraged.avg',
        'disk.deviceLatency.avg',
        'disk.deviceReadLatency.avg',
        'disk.deviceWriteLatency.avg',
        'disk.kernelLatency.avg',
        'disk.kernelReadLatency.avg',
        'disk.kernelWriteLatency.avg',
        'disk.maxQueueDepth.avg',
        'disk.maxTotalLatency.latest',
        'disk.numberRead.sum',
        'disk.numberReadAveraged.avg',
        'disk.numberWrite.sum',
        'disk.numberWriteAveraged.avg',
        'disk.queueLatency.avg',
        'disk.queueReadLatency.avg',
        'disk.queueWriteLatency.avg',
        'disk.read.avg',
        'disk.scsiReservationCnflctsPct.avg',
        'disk.scsiReservationConflicts.sum',
        'disk.totalLatency.avg',
        'disk.totalReadLatency.avg',
        'disk.totalWriteLatency.avg',
        'disk.usage.avg',
        'disk.write.avg',
        'hbr.hbrNetRx.avg',
        'hbr.hbrNetTx.avg',
        'hbr.hbrNumVms.avg',
        'mem.active.avg',
        'mem.activewrite.avg',
        'mem.compressed.avg',
        'mem.compressionRate.avg',
        'mem.consumed.avg',
        'mem.consumed.userworlds.avg',
        'mem.consumed.vms.avg',
        'mem.decompressionRate.avg',
        'mem.granted.avg',
        'mem.heap.avg',
        'mem.heapfree.avg',
        'mem.latency.avg',
        'mem.llSwapIn.avg',
        'mem.llSwapInRate.avg',
        'mem.llSwapOut.avg',
        'mem.llSwapOutRate.avg',
        'mem.llSwapUsed.avg',
        'mem.lowfreethreshold.avg',
        'mem.overhead.avg',
        'mem.reservedCapacity.avg',
        'mem.shared.avg',
        'mem.sharedcommon.avg',
        'mem.state.latest',
        'mem.swapin.avg',
        'mem.swapinRate.avg',
        'mem.swapout.avg',
        'mem.swapoutRate.avg',
        'mem.swapused.avg',
        'mem.sysUsage.avg',
        'mem.totalCapacity.avg',
        'mem.unreserved.avg',
        'mem.usage.avg',
        'mem.vmfs.pbc.capMissRatio.latest',
        'mem.vmfs.pbc.overhead.latest',
        'mem.vmfs.pbc.size.latest',
        'mem.vmfs.pbc.sizeMax.latest',
        'mem.vmfs.pbc.workingSet.latest',
        'mem.vmfs.pbc.workingSetMax.latest',
        'mem.vmmemctl.avg',
        'mem.zero.avg',
        'mem.capacity.usage.avg',
        'mem.capacity.contention.avg',
        'net.broadcastRx.sum',
        'net.broadcastTx.sum',
        'net.bytesRx.avg',
        'net.bytesTx.avg',
        'net.droppedRx.sum',
        'net.droppedTx.sum',
        'net.errorsRx.sum',
        'net.errorsTx.sum',
        'net.multicastRx.sum',
        'net.multicastTx.sum',
        'net.packetsRx.sum',
        'net.packetsTx.sum',
        'net.received.avg',
        'net.transmitted.avg',
        'net.unknownProtos.sum',
        'net.usage.avg',
        'net.throughput.usage.avg',
        'power.energy.sum',
        'power.power.avg',
        'power.powerCap.avg',
        'rescpu.actav1.latest',
        'rescpu.actav15.latest',
        'rescpu.actav5.latest',
        'rescpu.actpk1.latest',
        'rescpu.actpk15.latest',
        'rescpu.actpk5.latest',
        'rescpu.maxLimited1.latest',
        'rescpu.maxLimited15.latest',
        'rescpu.maxLimited5.latest',
        'rescpu.runav1.latest',
        'rescpu.runav15.latest',
        'rescpu.runav5.latest',
        'rescpu.runpk1.latest',
        'rescpu.runpk15.latest',
        'rescpu.runpk5.latest',
        'rescpu.sampleCount.latest',
        'rescpu.samplePeriod.latest',
        'storageAdapter.commandsAveraged.avg',
        'storageAdapter.maxTotalLatency.latest',
        'storageAdapter.numberReadAveraged.avg',
        'storageAdapter.numberWriteAveraged.avg',
        'storageAdapter.outstandingIOs.avg',
        'storageAdapter.queueDepth.avg',
        'storageAdapter.queueLatency.avg',
        'storageAdapter.queued.avg',
        'storageAdapter.read.avg',
        'storageAdapter.totalReadLatency.avg',
        'storageAdapter.totalWriteLatency.avg',
        'storageAdapter.write.avg',
        'storagePath.busResets.sum',
        'storagePath.commandsAborted.sum',
        'storagePath.commandsAveraged.avg',
        'storagePath.maxTotalLatency.latest',
        'storagePath.numberReadAveraged.avg',
        'storagePath.numberWriteAveraged.avg',
        'storagePath.read.avg',
        'storagePath.totalReadLatency.avg',
        'storagePath.totalWriteLatency.avg',
        'storagePath.write.avg',
        'sys.resourceCpuAct1.latest',
        'sys.resourceCpuAct5.latest',
        'sys.resourceCpuAllocMax.latest',
        'sys.resourceCpuAllocMin.latest',
        'sys.resourceCpuAllocShares.latest',
        'sys.resourceCpuMaxLimited1.latest',
        'sys.resourceCpuMaxLimited5.latest',
        'sys.resourceCpuRun1.latest',
        'sys.resourceCpuRun5.latest',
        'sys.resourceCpuUsage.avg',
        'sys.resourceFdUsage.latest',
        'sys.resourceMemAllocMax.latest',
        'sys.resourceMemAllocMin.latest',
        'sys.resourceMemAllocShares.latest',
        'sys.resourceMemConsumed.latest',
        'sys.resourceMemCow.latest',
        'sys.resourceMemMapped.latest',
        'sys.resourceMemOverhead.latest',
        'sys.resourceMemShared.latest',
        'sys.resourceMemSwapped.latest',
        'sys.resourceMemTouched.latest',
        'sys.resourceMemZero.latest',
        'sys.uptime.latest',
        'virtualDisk.busResets.sum',
        'virtualDisk.commandsAborted.sum',
    ],
    HISTORICAL: [],
}

VSAN_CLUSTER_METRICS = {
    'vsan.cluster.congestion',
    'vsan.cluster.dedupRatio',
    'vsan.cluster.free',
    'vsan.cluster.health.count',
    'vsan.cluster.health.statsdb.count',
    'vsan.cluster.health.masterexist.count',
    'vsan.cluster.health.collection.count',
    'vsan.cluster.health.hostsmissing.count',
    'vsan.cluster.health.renameddirs.count',
    'vsan.cluster.iopsRead',
    'vsan.cluster.iopsWrite',
    'vsan.cluster.latencyAvgRead',
    'vsan.cluster.latencyAvgWrite',
    'vsan.cluster.oio',
    'vsan.cluster.savedByDedup',
    'vsan.cluster.throughputRead',
    'vsan.cluster.throughputWrite',
    'vsan.cluster.total',
    'vsan.cluster.used',
}


VSAN_HOST_METRICS = {
    'vsan.host.clientCacheHitRate',
    'vsan.host.clientCacheHits',
    'vsan.host.congestion',
    'vsan.host.coreUtilPct',
    'vsan.host.iopsRead',
    'vsan.host.iopsUnmap',
    'vsan.host.iopsWrite',
    'vsan.host.latencyAvgRead',
    'vsan.host.latencyAvgUnmap',
    'vsan.host.latencyAvgWrite',
    'vsan.host.oio',
    'vsan.host.pcpuUsedPct',
    'vsan.host.pcpuUtilPct',
    'vsan.host.readCount',
    'vsan.host.throughputRead',
    'vsan.host.throughputUnmap',
    'vsan.host.throughputWrite',
    'vsan.host.writeCount',
}

CLUSTER_DOMCLIENT = {
    'iopsRead',
    'throughputRead',
    'latencyAvgRead',
    'iopsWrite',
    'throughputWrite',
    'latencyAvgWrite',
    'congestion',
    'oio',
}

VSAN_CLUSTER_CAPACITY = {'total', 'used', 'free', 'savedByDedup', 'dedupRatio'}

HOST_DOMCLIENT = {
    'iopsRead',
    'throughputRead',
    'latencyAvgRead',
    'readCount',
    'iopsWrite',
    'throughputWrite',
    'latencyAvgWrite',
    'writeCount',
    'congestion',
    'oio',
    'clientCacheHits',
    'clientCacheHitRate',
    'iopsUnmap',
    'throughputUnmap',
    'latencyAvgUnmap',
}

HOST_CPU = {'coreUtilPct', 'pcpuUtilPct', 'pcpuUsedPct'}

ENTITY_REMAPPER = {
    'cluster-domclient:': CLUSTER_DOMCLIENT,
    'vsan-cluster-capacity:': VSAN_CLUSTER_CAPACITY,
    'host-domclient:': HOST_DOMCLIENT,
    'host-cpu:': HOST_CPU,
}

# All metrics that can be collected from Datastores.
DATASTORE_METRICS = {
    REALTIME: [],
    HISTORICAL: [
        'datastore.busResets.sum',
        'datastore.commandsAborted.sum',
        'datastore.numberReadAveraged.avg',
        'datastore.numberWriteAveraged.avg',
        'datastore.throughput.contention.avg',
        'datastore.throughput.usage.avg',
        'disk.busResets.sum',
        'disk.capacity.contention.avg',
        'disk.capacity.latest',
        'disk.capacity.provisioned.avg',
        'disk.capacity.usage.avg',
        'disk.numberReadAveraged.avg',
        'disk.numberWriteAveraged.avg',
        'disk.provisioned.latest',
        'disk.unshared.latest',
        'disk.used.latest',
    ],
}

ALLOWED_METRICS_FOR_VSAN = {
    'cluster': VSAN_CLUSTER_METRICS,
    'host': VSAN_HOST_METRICS,
}

# All metrics that can be collected from Datacenters.
DATACENTER_METRICS = {
    'realtime': [],
    'historical': [
        'vmop.numChangeDS.latest',
        'vmop.numChangeHost.latest',
        'vmop.numChangeHostDS.latest',
        'vmop.numClone.latest',
        'vmop.numCreate.latest',
        'vmop.numDeploy.latest',
        'vmop.numDestroy.latest',
        'vmop.numPoweroff.latest',
        'vmop.numPoweron.latest',
        'vmop.numRebootGuest.latest',
        'vmop.numReconfigure.latest',
        'vmop.numRegister.latest',
        'vmop.numReset.latest',
        'vmop.numSVMotion.latest',
        'vmop.numShutdownGuest.latest',
        'vmop.numStandbyGuest.latest',
        'vmop.numSuspend.latest',
        'vmop.numUnregister.latest',
        'vmop.numVMotion.latest',
        'vmop.numXVMotion.latest',
    ],
}

# All metrics that can be collected from Clusters.
CLUSTER_METRICS = {
    # clusterServices are only available for DRS and HA clusters, and can cause errors that are caught down
    # the line by the integration. That means some API calls are unnecessary.
    # TODO: Look if we can prevent those unnecessary API calls
    REALTIME: [],
    HISTORICAL: [
        'clusterServices.cpufairness.latest',
        'clusterServices.effectivecpu.avg',
        'clusterServices.effectivemem.avg',
        'clusterServices.failover.latest',
        'clusterServices.memfairness.latest',
        'cpu.totalmhz.avg',
        'cpu.usage.avg',
        'cpu.usagemhz.avg',
        'cpu.capacity.usage.avg',
        'cpu.capacity.contention.avg',
        'mem.consumed.avg',
        'mem.overhead.avg',
        'mem.totalmb.avg',
        'mem.usage.avg',
        'mem.vmmemctl.avg',
        'mem.capacity.usage.avg',
        'mem.capacity.contention.avg',
        'vmop.numChangeDS.latest',
        'vmop.numChangeHost.latest',
        'vmop.numChangeHostDS.latest',
        'vmop.numClone.latest',
        'vmop.numCreate.latest',
        'vmop.numDeploy.latest',
        'vmop.numDestroy.latest',
        'vmop.numPoweroff.latest',
        'vmop.numPoweron.latest',
        'vmop.numRebootGuest.latest',
        'vmop.numReconfigure.latest',
        'vmop.numRegister.latest',
        'vmop.numReset.latest',
        'vmop.numSVMotion.latest',
        'vmop.numShutdownGuest.latest',
        'vmop.numStandbyGuest.latest',
        'vmop.numSuspend.latest',
        'vmop.numUnregister.latest',
        'vmop.numVMotion.latest',
        'vmop.numXVMotion.latest',
    ],
}

ALLOWED_METRICS_FOR_MOR = {
    vim.VirtualMachine: VM_METRICS,
    vim.HostSystem: HOST_METRICS,
    vim.Datacenter: DATACENTER_METRICS,
    vim.Datastore: DATASTORE_METRICS,
    vim.ClusterComputeResource: CLUSTER_METRICS,
}

ALL_METRIC_GROUPS = [VM_METRICS, HOST_METRICS, DATACENTER_METRICS, DATASTORE_METRICS, CLUSTER_METRICS]

RESOURCES_WITH_HISTORICAL_METRICS = [
    group for group, metrics in ALLOWED_METRICS_FOR_MOR.items() if len(metrics[HISTORICAL]) > 0
]
RESOURCES_WITH_REALTIME_METRICS = [
    group for group, metrics in ALLOWED_METRICS_FOR_MOR.items() if len(metrics[REALTIME]) > 0
]
