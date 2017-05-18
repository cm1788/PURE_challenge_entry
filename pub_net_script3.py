import graphlab
import pickle
from graphlab import aggregate as agg
import itertools

authors=graphlab.SFrame('./170331_PURE_Data_Challenge/PURE Data Challenge/authors.csv')
pub_authors = authors.groupby(key_columns='PUBLICATION_ID', operations={'authors':agg.CONCAT('PERSON_ID')})


f=open('./publication_net_links_dict.pkl', 'rb')
_pub_links = pickle.load(f)
f.close()

#weights = [len([author for author in pub_authors.filter_by(column_name='PUBLICATION_ID',values=link)['authors'][0] if author in pub_authors.filter_by(column_name='PUBLICATION_ID',values=link)['authors'][1]]) for link in _pub_links]

weights = [len([author for author in pub_authors[pub_authors['PUBLICATION_ID']==link[0]] if author in pub_authors[pub_authors['PUBLICATION_ID']==link[1]]]) for link in _pub_links]


f = open('publication_net_links_weights.pkl', 'wb')
pickle.dump(file=f,obj=weights)
f.close()

links = dict(zip(_pub_links, weights))

f = open('publication_net_links_dict_comp.pkl', 'wb')
pickle.dump(file=f,obj=links)
f.close()
