def uniprot_sequence_fetch(uni_ids):
    '''
    Takes dataframe from Prothermdb tsv.
    fetches sequences from UniProt by
    UniProt_ID and returns datafame with
    sequences added and any UniProt_ID's
    that sequences were not found. 
    '''
    
    df2 = uni_ids.copy()
    bad_link = []
        
        
    for ind in uni_ids.index:
        url = 'https://rest.uniprot.org/uniprotkb/' + str(uni_ids.loc[ind, 'UniProt_ID'])
            
        # fetch the json response
        data = requests.get(url).json()
        
        try:
            # pick needed data e.g. 
            sequence = data['sequence']['value']
            length = data['sequence']['length']
            
            df2.loc[ind, 'Sequence'] = sequence
            df2.loc[ind, 'Sequence_length'] = length
        
        except KeyError:
            bad_link.append(uni_ids.loc[ind, 'UniProt_ID'])
        
            
    return df2, bad_link