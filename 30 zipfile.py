import zipfile
zip_file = zipfile.ZipFile('temp1.zip','w')
zip_file.write('SPIDEY.mp4', compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()