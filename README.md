# CartoonDB
## Description of this App

This is an app for creating lists of cartoon characters and respective voice actors as well as shows.

### Routes Table
| Verb      | URI Pattern | Controller#Action    |
| :---        |    :----:   |          ---: |
| POST      | `characters/`  | `characters#create`   |
| GET     |    `characters/`   | `characters#index`  |
| PUT      | `characters/<int:pk>/`       | `characters#show`  |
| DELETE  |  `characters/<int:pk>/`        | `characters#delete`      |
| POST      | `voice-actors/`  | `voice-actors#create`   |
| GET     |    `voice-actors/`   | `characters#index`  |
| PUT      | `voice-actors/<int:pk>/`       | `voice-actors#show`  |
| DELETE  |  `voice-actors/<int:pk>/`        | `voice-actors#delete`      |
| POST      | `shows/`  | `shows#create`   |
| GET     |    `shows/`   | `shows#index`  |
| PUT      | `shows/<int:pk>/`       | `shows#show`  |
| DELETE  |  `shows/<int:pk>/`        | `shows#delete`      |




### Starting Instructions
#### Requirements
- Python3
- PIPenv
- Postgresql
- Django / Django REST Frameworks

To use this application, you will need the requirements listed above.
