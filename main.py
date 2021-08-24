import iucn
import match

if __name__ == '__main__':
    afj = []
    ans = input(
'''This is the IUCN Personal Database from Jett, copyright (c) openwld.com 2019-2021, all rights reserved.
Welcome! Would you like to update the database first (y/n) (this will take up to 5 minutes)? ''').lower()
    if ans == 'y':
        iucn.getjson()
        print('Done!')
    ans = ''
    while True:
        ans = input('''All right now, what do you want to search on this database (enter q to quit): ''').lower()
        if ans == 'q':
            print('''Goodbye! See you next time!''')
            exit(0)
        else:
            print('Searching for you (this may take up to 15 seconds)...')
            ret = match.search(ans, afj)
            afj = ret[1]
            if ret[0] == False:
                print('''Oops, seems like there is no match for you, maybe you should try the following:
1.Change your wording
2.Try to refresh your database
3.Run this program again''')
else:
    print('ERROR: this should be ran as the top level program')
    exit(255)