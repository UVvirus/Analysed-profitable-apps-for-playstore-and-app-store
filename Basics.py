#!/usr/bin/env python
# coding: utf-8

# #type of apps are likely to attract more users#
# 

# In[1]:


from csv import reader

### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]


# In[2]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

print(android_header)
print('\n')
explore_data(android, 0, 3, True)


# In[3]:


print(ios_header)
print('\n')
explore_data(ios, 0, 3, True)


# In[4]:


print(android[10472])  # incorrect row
print('\n')
print(android_header)  # header
print('\n')
print(android[0])      # correct row


# In[5]:


print(len(android))
del android[10472]  # don't run this more than once
print(len(android))


# In[6]:


for app in android:
    name=app[0]
    if name=='Instagram':
        print(app)


# In[7]:


duplicate_apps=[]
unique_apps=[]

for app in android:
    name=app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        
print('Number of duplicate apps:',len(duplicate_apps))
print('\n')
print('Examples of duplicate_apps:',duplicate_apps[:15])


# In[8]:


reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews


# In[9]:


android_clean=[]
already_added=[]
for app in android:
    name=app[0]
    n_reviews=float(app[3])
    if (reviews_max[name]==n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name)


# In[10]:


explore_data(android_clean,0,3,True)


# In[11]:


print(ios[813][1])
print(ios[6731][1])
print('\n')
print(android_clean[4412][0])
print(android_clean[4412][0])


# In[12]:


def non_eng(string):
    non_ascii=0
    
    for character in string:
        
         if ord(character)>127:
            non_ascii+=1
    if non_ascii > 3:
        return False
    else:
            return True
    


# In[13]:


print(non_eng('Instagram'))
print(non_eng('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print(non_eng('Docs To Go™ Free Office Suite'))
print(non_eng('Instachat 😜'))
print(ord('™'))


# In[14]:


android_english=[]
ios_english=[]

for app in android_clean:
    name=app[0]
    if non_eng(name):
        android_english.append(app)
        
for app in ios:
    name=app[1]
    if non_eng(name):
        ios_english.append(app)
        
explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)


# In[15]:


free_app_android=[]
free_app_ios=[]
for app in android_english:
    price=app[7]
    if price=='0':
        free_app_android.append(app)
        
for app in ios_english:
    price=app[4]
    if price=='0.0':
        free_app_ios.append(app)
        
print(len(free_app_android))
print(len(free_app_ios))


# In[16]:


def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_percent(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


# In[17]:


display_percent(ios,-5)
print('\n')
display_percent(android,1)
print('\n')
display_percent(android, -4)


# In[18]:


genres_ios = freq_table(free_app_ios, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


# In[19]:


for app in ios:
    if app[-5] == 'Navigation':
        print(app[1], ':', app[5]) # print name and number of ratings


# In[20]:


for app in ios:
    if app[-5] == 'Reference':
        print(app[1], ':', app[5])


# In[21]:


display_percent(android, 5) # the Installs columns


# In[22]:


categories_android = freq_table(android, 1)

for category in categories_android:
    total = 0
    len_category = 0
    for app in android:
        category_app = app[1]
        if category_app == category:            
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)


# In[23]:


for app in android_final:
    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])


# In[ ]:


under_100_m = []

for app in android:
    n_installs = app[5]
    n_installs = n_installs.replace(',', '')
    n_installs = n_installs.replace('+', '')
    if (app[1] == 'COMMUNICATION') and (float(n_installs) < 100000000):
        under_100_m.append(float(n_installs))
        
sum(under_100_m) / len(under_100_m)

