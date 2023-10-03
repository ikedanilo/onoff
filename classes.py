def junta1(cpc_profile_dic, cec_lpar_dic, cpc_list):
    for k, v in cpc_profile_dic.items():
        for x, y in cec_lpar_dic.items():
            if k == x:
                v[0]['lpar_info_capacity'] = y
    for k, v in cpc_profile_dic.items():
        for d in cpc_list:
            if d['cpcName'] == k:
                for z, w in v[0].items():
                    d[f'{z}'] = w
    return cpc_list
