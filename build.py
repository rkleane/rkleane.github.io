#!/usr/bin/python

header_r = file("src/header.html", "r")
head_r = file("src/head.html", "r")
footer_r = file("src/footer.html", "r")

home_r = file("src/home.html", "r")
research_r = file("src/research.html", "r")
cv_r = file("src/cv.html", "r")
talks_r = file("src/talks.html", "r")
about_r = file("src/about.html", "r")
contact_r = file("src/contact.html", "r")

input_rs = []
input_rs.append(home_r)
input_rs.append(research_r)
input_rs.append(cv_r)
input_rs.append(talks_r)
input_rs.append(about_r)
input_rs.append(contact_r)

home_w = file("index.html", "w")
research_w = file("Research.html", "w")
cv_w = file("CV.html", "w")
talks_w = file("Talks.html", "w")
about_w = file("About.html", "w")
contact_w = file("Contact.html", "w")

output_ws = []
output_ws.append(home_w)
output_ws.append(research_w)
output_ws.append(cv_w)
output_ws.append(talks_w)
output_ws.append(about_w)
output_ws.append(contact_w)

for f_w in output_ws:
	f_w.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n")

for line in head_r.readlines():
	for f_w in output_ws:
		f_w.write(line)

for f_w in output_ws:
	f_w.write("</head>\n<body>\n<div id=\"container\">\n")

for line in header_r.readlines():
	for f_w in output_ws:
		f_w.write(line)

for i in xrange(len(input_rs)):
	for line in input_rs[i].readlines():
		output_ws[i].write(line)

for f_w in output_ws:
	f_w.write("<div id=\"push\"></div>\n</div>\n")

for line in footer_r.readlines():
	for f_w in output_ws:
		f_w.write(line)

for f_w in output_ws:
	f_w.write("</body>\n</html>")

header_r.close()
head_r.close()
footer_r.close()

for i in xrange(len(input_rs)):
	input_rs[i].close()
	output_ws[i].close()

