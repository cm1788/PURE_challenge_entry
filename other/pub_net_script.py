import graphlab
import pickle
from graphlab import aggregate as agg
import itertools

authors=graphlab.SFrame('./170331_PURE_Data_Challenge/PURE Data Challenge/authors.csv')

pub_authors = authors.groupby(key_columns='PERSON_ID', operations={'publications':agg.CONCAT('PUBLICATION_ID')})

solo_count = 0
links = dict()
for ci,pub in enumerate(pub_authors):
    
    if len(pub['publications'])==1:
        solo_count += 1
    else:
        _links = itertools.combinations(pub['publications'],2)
        for l in _links:
            if l not in links.keys():
                links[l] = 1
            else:
                links[l] +=1
                
    if ci%100==0:
        print ci

print "Established %d links in the publication network." %len(links)
print "%d authors publish only a single paper." %solo_count

f = open('publication_net_links_dict.pkl', 'wb')
pickle.dump(file=f,obj=links)
f.close()
