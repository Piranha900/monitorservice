import os
while True:
    for file in os.listdir("/home/piranha900/test"):
        if file.endswith(".gz"):
           os.system('zcat -d /home/piranha900/test/'+ file +' | split -l 1  - "/home/piranha900/test/'+file+'-part"')
           os.system('rm -rf /home/piranha900/test/'+ file)
