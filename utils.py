import numpy as np

def onehotCategorical(req, limit, store=0):
    if req < 5:
        req = 5
    if req > 24:
        req = 24
    arr = np.zeros((limit,))
    arr[req-5] = 1.
    return arr

def onehotState(st):
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    st_indext= states.index(st)

    arr = np.zeros(51)
    arr[st_indext] = 1.
    return arr
