# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 8 Assignment 1

with open ("input.txt", 'r') as file_object:
    data_list  = []
    for line in file_object:
        line = line.strip()
        data_list.append(line)
print(f"Here are the Users Agent:")
for data in data_list: 
    if data.startswith('User-agent'):
        print(data)
print(f"Here are the sitemaps ")
for site in data_list:
    if site.startswith('Sitemap'):
        print(site)
print(f"Here are the crawl delays:")
for crawl in data_list:
    if crawl.startswith('Crawl-Delay'):
        print(crawl)