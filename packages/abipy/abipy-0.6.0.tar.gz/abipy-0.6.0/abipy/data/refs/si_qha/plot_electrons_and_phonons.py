#!/usr/bin/env python
r"""
Band structure plot
===================

This example shows how to plot a band structure
using the eigenvalues stored in the GSR file
produced at the end of the GS run.
"""
from abipy import abilab
import abipy.data as abidata
import os

dirpath = "."

gsr_paths = [os.path.join(dirpath, fname) for fname in ("mp-149_+0_GSR.nc", "mp-149_+2_GSR.nc")]
phbst_paths = [os.path.join(dirpath, fname) for fname in ("mp-149_+0_PHBST.nc", "mp-149_+2_PHBST.nc")]

nrows = len(gsr_paths)
ncols =  3
ax_mat, fig, plt = abilab.get_axarray_fig_plt(None, nrows=nrows, ncols=ncols,
                                              sharex=False, sharey=False, squeeze=False)

gsr_files = [abilab.abiopen(p) for p in gsr_paths]
phbst_files = [abilab.abiopen(p) for p in phbst_paths]

for i, (gsr, phbst) in enumerate(zip(gsr_files, phbst_files)):
    max_phfreq = phbst.phbands.maxfreq
    gsr.ebands.plot(ax=ax_mat[i, 0], with_gaps=True, max_phfreq=max_phfreq, show=False)
    gsr.ebands.interpolate(line_density=20).ebands_kpath.plot(ax=ax_mat[i, 1], with_gaps=True, max_phfreq=max_phfreq, show=False)
    phbst.phbands.plot(ax=ax_mat[i, 2], show=False)

plt.show()

# Here we use one of the GSR files shipped with abipy.
# Replace filename with the path to your GSR file or your WFK file.
#filename = abidata.ref_file("si_nscf_GSR.nc")

# Open the GSR file and extract the band structure.
# (alternatively one can use the shell and `abiopen.py OUT_GSR.nc -nb`
# to open the file in a jupyter notebook.
#with abiopen(filename) as ncfile:
#    ebands = ncfile.ebands

# Plot the band energies. Note that the labels for the k-points
# are found automatically in an internal database.
# Show fundamental and direct gaps.
#ebands.plot(with_gaps="fd", title="Silicon band structure")
#ebands.plot(with_gaps=True, title="Silicon band structure")

# Plot the BZ and the k-point path.
#ebands.kpoints.plot()
