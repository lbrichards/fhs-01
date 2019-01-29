import pandas
from path import Path
from functions import lat_lon_to_xyz, distance

CWD = Path.getcwd()

DATA_DIR = CWD.parent
f = DATA_DIR / 'fukushima_latlong.csv'



def main(my_postcode):
    df = pandas.read_csv(f)
    # df = df.dropna()
    df = df[[
            'pc',
            'place_name',
            'admin_name3',
            'latitude',
            'longitude'
        ]]
    df = df.rename(columns = {
        'pc': 'postcode',
        'place_name': 'address',
        'latitude': 'Lat',
        'longitude': 'Long'})
    df = calc_xyz(df)
    calc_dist(df, reference_postcode= my_postcode)
    

    
    
def calc_xyz(df):
    # df['xyz'] = df.apply(
    #    lambda row: lat_lon_to_xyz(
    #        row.Lat, row.Long), axis = 1)
    
    df['x'], df['y'], df['z'] = list(zip(*(df.apply(
        lambda row: lat_lon_to_xyz(
            row.Lat, row.Long), axis = 1))))    
    
    # df['x'], df['y'], df['z'] =list(zip(*((x[0], x[1], x[2]) for x in df['xyz'].values)))
    
    # print(df[['x', 'y', 'z']])
    
    return df



def calc_dist(df, reference_postcode):
    df2 = df.loc[df['postcode']==reference_postcode]
    x1, y1, z1 = df2[['x', 'y', 'z']].values.flatten().tolist()
    
    df['distance'] = df.apply(lambda row: distance(x1, y1, z1, row.x, row.y, row.z),
                              axis = 1)
    df = df.sort_values(by = 'distance')
    df = df[df.distance == df.distance.max()]
    print(df.address, df.admin_name3, df.postcode)
    # print(df.columns)
    # print(df[['admin_name3', 'address', 'distance']])
    
    
    
    





if __name__ == '__main__':
    main('960-8143')

