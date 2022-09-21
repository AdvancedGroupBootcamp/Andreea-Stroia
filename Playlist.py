
track_count1=0
track_count2=0
track_count3=0
track_count4=0
track_count5=0
track_count6=0
track_count7=0
track_count8=0
track_count9=0
track_count10=0
track_count11=0
track_count12=0

duration1=0
duration2=0
duration3=0
duration4=0
duration5=0
duration6=0
duration7=0
duration8=0
duration9=0
duration10=0
duration11=0
duration12=0

playlist_count1=0
playlist_count2=0
playlist_count3=0
playlist_count4=0
playlist_count5=0
playlist_count6=0
playlist_count7=0
playlist_count8=0
playlist_count9=0
playlist_count10=0
playlist_count11=0
playlist_count12=0

import json
import os

path_to_json = 'E:\Playlist\Try'
json_files=[pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

Lista=['Zaz','Oumou', 'Kendrick Lamar', 'Pink', 'Muse', 'The Killers', 'Eminem',
       'Taylor Swift', 'Harry Styles', 'Lara Fabian', 'Andrea Bocelli', 'Laurent Garnier']
for i, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text=json.load(json_file)
        for j in json_text['playlists']:
            for f in (j['tracks']):
                if f['artist_name'] == Lista[0]:
                    track_count1 +=1
                    duration1 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count1 += 1
                if f['artist_name'] == Lista[1]:
                    track_count2 +=1
                    duration2 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count2 += 1
                if f['artist_name'] == Lista[2]:
                    track_count3 +=1
                    duration3 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count3 += 1
                if f['artist_name'] == Lista[3]:
                    track_count4 +=1
                    duration4 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count4 += 1
                if f['artist_name'] == Lista[4]:
                    track_count5 +=1
                    duration5 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count5 += 1
                if f['artist_name'] == Lista[5]:
                    track_count6 +=1
                    duration6 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count6 += 1
                if f['artist_name'] == Lista[6]:
                    track_count7 +=1
                    duration7 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count7 += 1
                if f['artist_name'] == Lista[7]:
                    track_count8 +=1
                    duration8 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count8 += 1
                if f['artist_name'] == Lista[8]:
                    track_count9 +=1
                    duration9 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count9 += 1
                if f['artist_name'] == Lista[9]:
                    track_count1 +=1
                    duration10 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count10 += 1
                if f['artist_name'] == Lista[10]:
                    track_count11 +=1
                    duration11 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count11 += 1
                if f['artist_name'] == Lista[11]:
                    track_count12 +=1
                    duration12 += f['duration_ms']
                    for z in json_text['playlists']:
                        playlist_count12 += 1

Dict_count_tracks={ 'Zaz': track_count1, 'Oumou':track_count2,'Kendrick Lamar': track_count3,'Pink': track_count4,
                    'Muse': track_count5, 'The Killers': track_count6,
                    'Eminem':track_count7, 'Taylor Swift': track_count8,'Harry Styles': track_count9,
                    'Lara Fabian':track_count10,'Andrea Bocelli': track_count11, 'Laurent Garnier' :track_count12 }

Dict_duration={ 'Zaz': round(duration1/6000), 'Oumou':round(duration2/6000),'Kendrick Lamar': round(duration3/6000),'Pink': round(duration4/6000),
                    'Muse': round(duration5/6000), 'The Killers': round(duration6/6000),
                    'Eminem':round(duration7/6000), 'Taylor Swift': round(duration8/6000),'Harry Styles': round(duration9/6000),
                    'Lara Fabian':round(duration10/6000),'Andrea Bocelli': round(duration11/6000), 'Laurent Garnier' :round(duration12/6000) }

Dict_playlists={ 'Zaz': playlist_count1, 'Oumou':playlist_count2,'Kendrick Lamar': playlist_count3,'Pink': playlist_count4,
                    'Muse': playlist_count5, 'The Killers': playlist_count6,
                    'Eminem':playlist_count7, 'Taylor Swift': playlist_count8,'Harry Styles': playlist_count9,
                    'Lara Fabian':playlist_count10,'Andrea Bocelli': playlist_count11, 'Laurent Garnier' :playlist_count12 }

print(Dict_count_tracks)
print(Dict_duration)
print(Dict_playlists)
