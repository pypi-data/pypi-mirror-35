
import sys
#sys.path.insert(0,"/Users/enielse/research/old-pyGSTi/packages")

import pygsti
print("PYGSTI FILe = ",pygsti.__file__)
from pygsti.construction import std1Q_XYI as std
import os
import numpy as np

print("CWD = ",os.getcwd())

#ds = pygsti.objects.DataSet(fileToLoadFrom="../cmp_chk_files" + "/drivers.datasetv3")

germs = std.germs
fiducials = std.fiducials
maxLens = [1]
gateLabels = list(std.gs_target.gates.keys())

lsgstStrings = pygsti.construction.make_lsgst_lists(
    gateLabels, fiducials, fiducials, germs, maxLens )

datagen_gateset = std.gs_target.depolarize(gate_noise=0.05, spam_noise=0.1)
ds = pygsti.construction.generate_fake_data(
    datagen_gateset, lsgstStrings[-1],
    nSamples=1000,sampleError='binomial', seed=100)
print("Expected 2DeltaLogL = ", 2*(pygsti.tools.logl_max(datagen_gateset, ds)-pygsti.tools.logl(datagen_gateset, ds)))


gs_target = std.gs_target.copy()
gs_target.set_all_parameterizations("H+S+A")

print(gs_target.num_params(), " params")
#v = gs_target.to_vector()
#for lbl,obj in gs_target.iter_objs():
#    print(lbl,":",obj.gpindices)
#    start,stop = obj.gpindices.start, obj.gpindices.stop
#    assert(stop-start == 12) # 1Q Lindblad gate
#    v[start+3] = v[start+3+4] = v[start+3+8] = 0.005 # just add diagonal *stochastic* noise
#gs_target.from_vector(v)    
#
#effects = gs_target.povms['Mdefault'].compile_effects('Mdef')
#for lbl,e in effects.items():
#    print(lbl,":",e.gpindices)
    

#sys.exit(0)

#Set random starting point?
#randv = 0.005*(np.random.random( gs_target.num_params() ) - 0.5)
#gs_target.from_vector(randv)

maxLens = [1]
result = pygsti.do_long_sequence_gst(
    ds, gs_target, std.fiducials, std.fiducials,
    std.germs, maxLens, verbosity=4)

gs_final = result.estimates['default'].gatesets['final iteration estimate']
print("Final 2DeltaLogL = ", pygsti.tools.two_delta_logl(gs_final, ds, dof_calc_method="nongauge"))
print("Compare w/datagen 2DeltaLogL = ", pygsti.tools.two_delta_logl(datagen_gateset, ds, dof_calc_method="nongauge"))


#pygsti.report.create_standard_report(result, "debugReport",
#                                     "Std Practice Test Report", verbosity=2,
#                                     advancedOptions={'errgen_type': "logTiG",
#                                                      'precision': 2, #just a single int
#                                                      'resizable': False,
#                                                      'autosize': 'none'})

