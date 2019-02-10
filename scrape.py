import requests
#import dhooks


counter = 11
pool = []
anonfile = 'https://anonfile.com/'

#hook = dhooks.Webhook('DISCORD_WEBHOOK_HERE')



while True:
    counter += 10
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&qs=n&sp=-1&pq=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&sc=0-48&sk=&cvid=ED277F82EB8B4BC9A980947F0F13CBC1&first='+str(counter)).text
    links = src.split('<a href="https://')
    for link in links:
        if 'anonfile.com/' in link:
            fileurl = requests.get(anonfile+link)
            url = fileurl.url[:44]
            url = url[10:]
            url = url[:34]
            url = url[24:]
            url = (anonfile)+(url)
            validator = requests.get(url)
            if validator.status_code == 200:
                #print (counter)
                print(url)
                #hook.send (url) #enable if you want to send links through webhook
                with open('filelinks.txt','a') as handle:
                    handle.write(url+'\n')
            else:
                print ("")
                
            

                

