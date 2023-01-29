'''Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  k members per group where  k≠1 .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear k times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of k and the room number list.'''

k = int(input())        # no of rooms
rooms = list(map(int, input().split()))    # room numbers  
roomSet = set(rooms)         # duplicate entries will be eliminated
roomSum = sum(rooms)
roomSetSum = sum(roomSet) * k    # total number of rooms assuming that eac room number is repeated except for the captains room
captiansRoom = (roomSetSum - roomSum) // (k - 1)
print(captiansRoom)


'''
rooms = list(map(int, input().split()))

input()="1223344"
.split()-['1','2','2','3','3','4','4']
map-maps the strings in the list to integer- [1,2,2,3,3,4,4]

'''