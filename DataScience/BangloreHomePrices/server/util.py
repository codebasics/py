import pickle

__tier_df = None
__model = None

def __get_saved_model():
    global __model
    if __model is None:
        with open('../model/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    return __model

def __get_saved_tier_df():
    global __tier_df
    if __tier_df is None:
        with open('../model/location_tiers.pickle','rb') as f:
            __tier_df = pickle.load(f)
    return __tier_df

def get_estimated_price(sqft,location,bhk,bath):
    model = __get_saved_model()

    tier = get_location_tier(location)

    X = [
        [
            sqft,
            bath,
            bhk,
            1 if tier == 'tier1' else 0,
            1 if tier == 'tier2' else 0,
            1 if tier == 'tier3' else 0,
            1 if tier == 'tier4' else 0,
            1 if tier == 'tier5' else 0
        ]
    ]

    result = model.predict(X)
    return result[0]


def get_location_tier(location):
    df = __get_saved_tier_df()
    return df.loc[location.lower()].values[0]

def get_location_names():
    df = __get_saved_tier_df()
    return list(df.index)

if __name__ == '__main__':
    n=get_location_tier('kothanur')
    print(get_location_names())
    pass