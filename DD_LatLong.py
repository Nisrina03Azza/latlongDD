
# Latitude coordinate as Degree Decimals (DD) format ex = 9.77637527 N
def latdd(d,m,s,p):
    lat_degreedecimal = int(d) + (int(m))/60 + (float(s))/3600
    print(f'Your latitude coordinate in Degree Decimals is {lat_degreedecimal:.5f} {p}')

# Longitude coordinate as Degree Decimals (DD) format ex = 9.77637527 N
def longdd(d,m,s,p):
    long_degreedecimal = int(d) + (int(m))/60 + (float(s))/3600
    print(f'Your longitude coordinate in Degree Decimals is {long_degreedecimal:.5f} {p}')

# Asking for the latitude coordinate in second, minute, degree 
def lat():
    print('Input your latitude coordinates!')
    lat_second = input('second: ')
    lat_minute = input('minute: ')
    lat_degree = input('degree: ')
    lat_pole = input('North(N)/South(S) of the Equator? ').capitalize()
    print('Your latitude coordinates is ' + str(int(lat_degree)) + ' degree ' + str(int(lat_minute)) + ' minute ' + str(float(lat_second)) + ' second ' + lat_pole)
    latdd(lat_degree, lat_minute, lat_second, lat_pole)
    
# Asking for the longitude coordinate in second, minute, degree 
def long():
    print('Input your longitude coordinates!')
    long_second = input('second: ')
    long_minute = input('minute: ')
    long_degree = input('degree: ')
    long_pole = input('East(E)/West(W) of the Meridian? ').capitalize()
    print('Your longitude coordinates is ' + str(int(long_degree)) + ' degree ' + str(int(long_minute)) + ' minute ' + str(float(long_second)) + ' second ' + long_pole)
    longdd(long_degree, long_minute, long_second, long_pole)


# Asking the user's name
print('What can i call you?')  
name = input().capitalize()
print(f'Welcome, {name}!')

while True:
# Ask user if they want to calculate latitude or langitude
    latlong = input('Do you want to calculate Latitude or Longitude? ').title()
    # if user want to calculate just the latitude
    if (latlong == 'Latitude') or (latlong =='Lat'):
        lat()
    # if user want to calculate just the latitude
    elif (latlong == 'Longitude') or (latlong == 'Long'):
        long()
    # if user want to calculate both the latitude and longitude
    elif (latlong in ['Both','Lat Long', 'Latitude Longitude']):
        lat()
        long()
    else:
        print('Good to see you!')

# Ask user if they want to calculate latitude or langitude again
    choice = input('Continue (y/n)? '.lower())
    # if user want to stop (n), if not (y) it will loop
    if choice.lower() == 'n':
        print('See you!')
        break