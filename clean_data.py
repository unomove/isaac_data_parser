import cv2
import os
import csv

def isValid(path1, path2, path3):
	if os.path.isfile(path1)  == False or os.path.isfile(path2) == False or os.path.isfile(path3) == False:
		# print("invalid",  count, i)
		# count = count+1
		return False
	return True

f=open('/home/nusai/spot-project/spot_data_v2/parsed/label.txt')

labels=f.readlines()

fout = open(os.path.join('/home/nusai/spot-project/spot_data_v2/parsed/', 'label02.txt'), 'w')
labelwriter = csv.writer(fout, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
labelwriter.writerow(['frame', 'intention_type', 'current_velocity', 'steering_wheel_angle', 'dlm'])
    

count  = 0
for i in range(0, len(labels)):
	# print(i)
	if i > 1:
		path1 = '/home/nusai/spot-project/spot_data_v2/parsed/rgb_m/'+labels[i].strip().split()[0]+'.jpg'
		path2 = '/home/nusai/spot-project/spot_data_v2/parsed/rgb_l/'+labels[i].strip().split()[0]+'.jpg'
		path3 = '/home/nusai/spot-project/spot_data_v2/parsed/rgb_r/'+labels[i].strip().split()[0]+'.jpg'
		# path = labels[i].strip().split(",")[0]

		if isValid(path1, path2, path3):
			labelwriter.writerow([labels[i].strip().split()[0], labels[i].strip().split()[1], labels[i].strip().split()[2], labels[i].strip().split()[3], labels[i].strip().split()[4]])
		else:
			labelwriter.writerow([labels[i].strip().split()[0], labels[i].strip().split()[1], labels[i].strip().split()[2], labels[i].strip().split()[3], 'Junk'])

