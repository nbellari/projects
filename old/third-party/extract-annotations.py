#!/usr/bin/env python

# see http://socialdatablog.com/extract-pdf-annotations.html

myxkfolder="/home/steve/xk/" #you need to set this to where you want your to-dos to appear

import poppler, os.path, os, time, datetime

for root, dirs, files in os.walk('./'):
    for lpath in files:
		fullpath=os.path.realpath(os.path.join(root, lpath))
		mtime=os.path.getmtime(fullpath)
		# print("Opening: ..."+fullpath)

		##  check if size is not less than 0 bytes
		## needs to be TOLOWER

		if lpath.endswith('.pdf') :#& os.stat(fullpath).st_size>0: 

			x=''	
			path = 'file://%s' % fullpath
			myino=os.stat(fullpath).st_ino
			# print("Found PDF:..."+fullpath)
			# print "Size: ... "+os.stat(fullpath).st_size
			try:
				doc = poppler.document_new_from_file(path, None)
			except:
			  print "some pdf problem"
			else:
				pages = [doc.get_page(i) for i in range(doc.get_n_pages())]

				for page_no, page in enumerate(pages):
				    items = [i.annot.get_contents() for i in page.get_annot_mapping()]
				    items = [i for i in items if i]
				    for j in items:
						# print "Found annotation: ... " + j 
						print path	
						j = j.replace("\r\n"," ")
						j = j.replace("\r\n"," ")
						x= x+"\n\n"+"'%s' (page %s)" % (j,page_no + 1)
						# print xk
						if "xk" in j:
							#xk= xk+"\n\n"+"'%s' (page %s)" % (j,page_no + 1)
							print j	
							g = open(myxkfolder+j+" "+lpath+" p. "+str(page_no)+'.txt', 'w')
							g.write(j)
							g.close()

				if x!='':
					f = open(os.path.splitext(fullpath)[0]+'.annotations.txt', 'w')
					f.write(x)
					f.close()
					os.utime(os.path.splitext(fullpath)[0]+'.annotations.txt', (mtime,mtime))



# This is based on code from Marwan Alsabbagh, https://stackoverflow.com/questions/13748242/extracting-pdf-annotations-comments, thanks
