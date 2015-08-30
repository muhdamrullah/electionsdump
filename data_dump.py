import subprocess

subprocess.call('scrapy runspider woru.py -o input.csv', shell=True)
subprocess.call('python remove_blank.py', shell=True)

print "WIN!"
