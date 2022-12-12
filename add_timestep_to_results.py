import numpy as np
import glob

timestamped = []

results_file = 'f_dataset-CMU_collect1_mono_closestdt2.txt'
final_results_file = 'CMU_collect1_mono_closestdt2_openvins_est.txt'
with open(results_file) as f:
    contents = f.readlines()

timestamps_file = '/Users/alexpletta/SLAM/Project/ORB_SLAM3_ag/Examples/Stereo/CMU_TimeStamps/CMU_site_Oporto_clearing_2022_08_17_collect1_processed1_stereo_closestdt.txt'
timestamps = []
with open(timestamps_file) as f:
    time_names = f.readlines()

for filename in time_names:
  img_name = (filename.split('.')[0] + '.' + filename.split('.')[1]).split('/')[-1]
  timestamp = float(img_name.split('_')[1])
  timestamps.append(timestamp)

final_lines = [["# timestamp", "tx", "ty", "tz", "qx", "qy", "qz", "qw"]]
for line,time in zip(contents, timestamps):
  line = line.split(' ')
  line[0] = str(time)
  line[-1] = line[-1].split('\n')[0]

  for i,val in enumerate(line):
    line[i] = np.format_float_scientific(float(val))

  final_lines.append(line)


np.savetxt(final_results_file, final_lines, fmt='%s')
