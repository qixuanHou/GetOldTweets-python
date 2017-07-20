field = open("field.txt", "r")
ls = field.readlines()
field = {}
for l in ls:
	key = l.split("[")[1].split("]")[0]
	value = l.split("\"")[1]
	if key in field.keys():
		field[key] = field[key] + [value,]
	else:
		field[key] = [value,]
print field


for key in field.keys():

	f = open("2015/sh/" + key + "2015run.sh", "w")
	count = 0
	for value in field[key]:
		count = count + 1
		for i in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
			if (i == "01"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "02"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-28 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "03"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "04"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-30 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "05"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "06"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-30 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "07"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "08"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "09"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-30 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "10"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "11"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-30 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))
			if (i == "12"):
				f.write("python Exporter.py --querysearch \"%s\" --since 2015-%s-01 --until 2015-%s-31 --output 2015/%s/%d_2015%s.txt\n"%(value,i, i, key, count, i))







# python Exporter.py --querysearch "intestinal sickness" --since 2015-01-01 --until 2015-01-31 --output 12201501.txt

# f = open("2016run.sh", "w")
# for i in range(1, 25):
# 	f.write("sh /Users/houqixuan/Documents/Health/Twizard/GetOldTweets-python/2016/sh/%d2016run.sh\n"%i)
# # sh /Users/houqixuan/Documents/Health/Twizard/GetOldTweets-python/2014/sh/12014run.sh