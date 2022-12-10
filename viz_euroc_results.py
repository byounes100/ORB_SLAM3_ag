import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
  traj_filename = 'f_dataset-CMU_mono_flying_only.txt'
  traj_data = np.loadtxt(traj_filename)

  keypts_filename = 'kf_dataset-CMU_mono_flying_only.txt'
  keypts_data = np.loadtxt(keypts_filename)

  ax = plt.axes(projection='3d')
  xdata_keypts = keypts_data[:,1]
  ydata_keypts = keypts_data[:,2]
  zdata_keypts = keypts_data[:,3]
  ax.scatter3D(xdata_keypts, ydata_keypts, zdata_keypts, color='red', s=80)

  xdata = traj_data[:,1]
  ydata = traj_data[:,2]
  zdata = traj_data[:,3]
  ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='ocean')


  plt.show()