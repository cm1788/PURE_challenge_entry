import graphlab
import pickle
from graphlab import aggregate as agg
import itertools

authors=graphlab.SFrame('./170331_PURE_Data_Challenge/PURE Data Challenge/authors.csv')

pub_authors = authors.groupby(key_columns='PERSON_ID', operations={'publications':agg.CONCAT('PUBLICATION_ID')})

solo_count = 0
#links = dict()

links = [l for pub in pub_authors for l in itertools.combinations(pub['publications'],2)]
print "Established %d links in the publication network." %len(links)

f = open('publication_net_links_dict.pkl', 'wb')
pickle.dump(file=f,obj=links)
f.close()
