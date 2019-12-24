import util
import pandas as pd

def test_location_tier():
    assert util.get_location_tier('kothanur') == 'tier1'
    assert util.get_location_tier('Lingadheeranahalli') == 'tier2'

def test_home_prediction():
    model = util.get_saved_model()

    location = 'Electronic City Phase II'
    tier = util.get_location_tier(location)

    X = [
        [
            1056,
            2, # bath
            2, # bhk
            1 if tier == 'tier1' else 0,
            1 if tier == 'tier2' else 0,
            1 if tier == 'tier3' else 0,
            1 if tier == 'tier4' else 0,
            1 if tier == 'tier5' else 0
        ]
    ]

    y_truth = 39.07

    result = model.predict(X)

    # 20% above and below truth value is assumed to be okay prediction
    assert result[0] <= y_truth*(1+0.2) and result[0]>=y_truth*(1-0.2)
