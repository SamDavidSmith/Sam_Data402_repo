from csv_intro import *

def test_is_transformed():
    csv1 = csv_reader()
    actual = csv_reader.transform_csv(csv1, cols=['firstName', 'lastName', 'email'])
    expected = pd.read_csv("user_details.csv", usecols=['firstName', 'lastName', 'email'])
    for i in range(transform_csv("user_details.csv").shape[0]):
        for j in range(transform_csv("user_details.csv").shape[1]):
            assert (actual.iloc[i, j] == expected.iloc[i, j])
