import requests
import json


class Player():
    '''
    A player in a fixture
    '''

    def __init__(self, object):
        self.dvp_rank = object['first_name']
        self.first_name = object['first_name']
        self.fppg = object['fppg']
        self.id = object['id']
        self.fixture = object['fixture']
        self.images = object['images']
        self.injured = object['injured']
        self.injury_details = object['injury_details']
        self.injury_severity = object['injury_severity']
        self.injury_status = object['injury_status']
        self.jersey_number = object['jersey_number']
        self.known_name = object['known_name']
        self.last_name = object['last_name']
        self.max_rank = object['max_rank']
        self.news = object['news']
        self.played = object['played']
        self.news = object['news']
        self.player_card_url = object['player_card_url']
        self.player_info = object['player_info']
        self.position = object['position']
        self.positions = object['positions']
        self.projected_fantasy_points = object['projected_fantasy_points']
        self.projected_starting_order = object['projected_starting_order']
        self.rank = object['rank']
        self.recent_games_played_stats = object['recent_games_played_stats']
        self.removed = object['removed']
        self.roster_position_stats = object['roster_position_stats']
        self.salary = object['salary']
        self.sport_specific = object['sport_specific']
        self.starting_order = object['starting_order']
        self.swappable = object['swappable']
        self.team = object['team']
        self.tier = object['tier']
        self.videos = object['videos']


class Contest():
    '''
    A Fanduel contest
    '''

    def __init__(self, object):
        self.id = object["id"]
        self._url = object["_url"]
        self.invite_url = object["invite_url"]
        self.sport = object["sport"]
        self.name = object['name']
        self.display_name = object['display_name']
        self.label = object['label']
        self.salary_cap = object['salary_cap']
        self.start_date = object['start_date']
        self.entry_fee = object['entry_fee']
        self.entry_fee_fdp = object['entry_fee_fdp']
        self.guaranteed = object['guaranteed']
        self.max_entries_per_user = object['max_entries_per_user']
        self.private = object['private']
        self.made_free = object['made_free']
        self.prizes = object['prizes']
        self.fixture_list = object['fixture_list']
        self.entries = object['entries']
        self.size = object['size']
        self.user_created = object['user_created']
        self.h2h = object['h2h']
        self.started = object['started']
        self.final = object['final']
        self.cancellation = object['cancellation']
        self.features = object['features']
        self.notice = object['notice']
        self.score_to_beat = object['score_to_beat']
        self.score_to_beat_pot = object['score_to_beat_pot']
        self.season_long_info = object['season_long_info']
        self.draft_specification = object['draft_specification']


class UpdateEntryInput():
    '''
    User input required to update a set Fanduel entries

    Attributes
    ----------
    id : str
        the id of the entry which you are modifying
    lineup : list[Player]
        list of Player Objects to populate this entry's lineup
    '''

    def __init__(self, object):
        self.id = object["id"]
        self.lineup: list[Player] = object["lineup"]

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Entry():
    '''
    An entry in a Fanduel contest
    '''

    def __init__(self, object):
        self.id = object["id"]
        self._url = object["id"]
        self.entry_currency = object["entry_currency"]
        self.cancelable = object["cancelable"]
        self.index = object["index"]
        self.rank = object["rank"]
        self.user_id = object["user"]["_members"][0]
        self.has_lineup = object["has_lineup"]
        self.fixture_list_id = object["fixture_list"]["_members"][0]
        self.contest_id = object["contest"]["_members"][0]
        self.prizes = object["prizes"]
        self.roster_id = object["roster"]["_members"][0]
        self.code = object["code"]

    def __str__(self):
        return 'Entry: {self.id}'.format(self=self)


class Fixture():
    '''
    An individual 'game' in a Fanduel contest (i.e. NFL game, UFC fight)
    '''

    def __init__(self, object):
        self.id = object["id"]
        self.start_date = object["start_date"]
        self.sport = object["sport"]
        self.type = object["type"]
        self.home_team = object["home_team"]
        self.away_team = object["away_team"]
        self.weather = object["weather"]
        self.status = object["status"]
        self.name = object["name"]
        self.target_periods = object["target_periods"]
        self.home_player: object = object['home_player']
        self.away_player: object = object['away_player']

    def __str__(self):
        return 'Fixture: {self.id}'.format(self=self)


class FixtureList():
    '''
    A list of the individual 'games' that make up a Fanduel contest
    '''

    def __init__(self, object):
        self.id = object["id"]
        self._url = object["_url"]
        self.sport = object["sport"]
        self.salary_cap = object["salary_cap"]
        self.start_date = object["start_date"]
        self.label = object["label"]
        self.status = object["status"]
        self.fixture_counts = object["fixture_counts"]
        self.players = object["players"]
        self.selection_priority = object["selection_priority"]
        self.notices = object["notices"]
        self.is_season_long = object["is_season_long"]
        self.game_description_name = object["game_description_name"]
        self.game_description = object["game_description"]
        self.late_swap = object["late_swap"]

    def __str__(self):
        return 'FixtureList: {self.id}'.format(self=self)


class GameDescription():
    '''
    Details associated with a fixture list
    '''

    def __init__(self, object):
        self.id = object["id"]
        self.name = object["name"]
        self.short_description = object["short_description"]
        self.long_description = object["long_description"]
        self.image_url = object["image_url"]
        self.display_priority = object["display_priority"]
        self.display_label = object["display_label"]
        self.roster_format = object["roster_format"]
        self.tag = object["tag"]
        self.only_score_top = object["only_score_top"]
        self.roster_restrictions = object["roster_restrictions"]

    def __str__(self):
        return 'GameDescription: {self.id}'.format(self=self)


class Roster():
    '''
    A collection of players as a lineup
    '''

    def __init__(self, object):
        self.id = object["id"]
        self._url = object["_url"]
        self.score = object["score"]
        self.ppr = object["ppr"]
        self.total_periods = object["total_periods"]
        self.name = object["name"]
        self.fixture_list = object["fixture_list"]
        self.has_lineup = object["has_lineup"]
        self.draft_type = object["draft_type"]
        self.season_long_roster_info = object["season_long_roster_info"]
        self.last_used = object["last_used"]
        self.entries = object["entries"]
        self.grouped_entries = object["grouped_entries"]
        self.lineup = object["lineup"]
        self.best_ball_lineup = object["best_ball_lineup"]

    def __str__(self):
        return 'Roster: {self.id}'.format(self=self)


class UserAuth():
    def __init__(self, user_id, session_token, basic_auth_token):
        self.user_id = user_id
        self.session_token = session_token
        self.basic_auth_token = basic_auth_token


class PlayerList():
    '''
    List of players mapped to a fixture list id
    '''

    def __init__(self, object):
        self.fixture_list_id = object['fixture_list_id']
        self.players: list[Player] = object['players']


class Upcoming():
    '''
    All of the upcoming data for a user
    '''

    def __init__(self, object):
        self.entries: list[Entry] = object['entries']
        self.rosters: list[Roster] = object['rosters']
        self.contests: list[Contest] = object['contests']
        self.fixtures: list[Fixture] = object['fixtures']
        self.fixture_lists: list[FixtureList] = object['fixture_lists']
        self.game_descriptions: list[GameDescription] = object['game_descriptions']
        self.player_lists: list[PlayerList] = object['player_lists']

    def __str__(self):
        return 'Upcoming Summary:\nEntries: {0}\nRosters: {1}\nContests: {2}\nFixtures: {3}\nFixtureLists: {4}\nGameDescriptions: {5}\nPlayer Lists: {6}'.format(len(self.entries), len(self.rosters), len(self.contests), len(self.fixtures), len(self.fixture_lists), len(self.game_descriptions), len(self.player_lists))


class Fanduel():
    '''
    The driver for accessing the Fanduel API
    '''

    def __init__(self, fanduel_email, fanduel_password, basic_auth_token, session_auth_token):
        self.fanduel_email = fanduel_email
        self.fanduel_password = fanduel_password
        self.basic_auth_token = basic_auth_token
        self.session_auth_token = session_auth_token
        self.user_auth = UserAuth(
            None, self.session_auth_token, self.basic_auth_token)
        self.fanduel_headers = self.__create_fanduel_headers()
        self.__authenticate()
        self.upcoming = self.__get_upcoming_data()

    def easy_get_contests(self):
        """Easy Mode for getting currently entered contests and basic relevant info
        
        :return: An array of contests in the following heirarchy: 
            contests [
                ...contest details
                entries [
                    ...entry details
                    available_players [
                        ...player details
                    ]
                ]
            ]
        """        
        contests = [{"id": contest.id, "name": contest.name, "sport": contest.sport, "entries": [{"id": entry.id, "has_lineup": entry.has_lineup, "available_players": [player.__dict__ for player in self.get_player_list(entry.fixture_list_id).players]} for entry in self.upcoming.entries if entry.contest_id == contest.id]} for contest in self.upcoming.contests]
        print("Southpaw: Contests Fetched:", len(contests))
        return contests

    def get_upcoming(self):
        """Retrieve all upcoming data
        """
        return self.upcoming

    def get_entries(self):
        """Retrieve all upcoming entries
        """
        return self.upcoming.entries

    def get_entry(self, entry_id):
        """Retrieve entry by id
        """
        return next((entry for entry in self.upcoming.entries if entry.id == entry_id), None)

    def get_rosters(self):
        """Retrieve all upcoming rosters
        """
        return self.upcoming.rosters

    def get_roster(self, roster_id):
        """Retrieve roster by id
        """
        return next((roster for roster in self.upcoming.rosters if roster.id == roster_id), None)

    def get_contests(self):
        """Retrieve all upcoming contests
        """
        return self.upcoming.contests

    def get_contest(self, contest_id):
        """Retrieve contest by id
        """
        return next((contest for contest in self.upcoming.contests if contest.id == contest_id), None)

    def get_fixtures(self):
        """Retrieve all upcoming fixtures
        """
        return self.upcoming.fixtures

    def get_fixture(self, fixture_id):
        """Retrieve fixture by id
        """
        return next((fixture for fixture in self.upcoming.fixtures if fixture.id == fixture_id), None)

    def get_fixture_lists(self):
        """Retrieve all upcoming fixture lists
        """
        return self.upcoming.fixture_lists

    def get_fixture_list(self, fixture_list_id):
        """Retrieve fixture list by id
        """
        return next((fixture_list for fixture_list in self.upcoming.fixture_lists if fixture_list.id == fixture_list_id), None)

    def get_game_descriptions(self):
        """Retrieve all upcoming game descriptions
        """
        return self.upcoming.game_descriptions

    def get_game_description(self, game_description_id):
        """Retrieve game description by id
        """
        return next((game_description for game_description in self.upcoming.game_descriptions if game_description.id == game_description_id), None)

    def get_player_lists(self):
        """Retrieve all upcoming player lists
        """
        return self.upcoming.player_lists

    def get_player_list(self, fixture_list_id):
        """Retrieve player list given a fixture list id
        """
        return next((player_list for player_list in self.upcoming.player_lists if player_list.fixture_list_id == fixture_list_id), None)

    def get_players_in_entry(self, entry_id):
        """Retrieve all players available to use in a given entry
        """
        entry = self.get_entry(entry_id)
        fixture_list_id = entry.fixture_list_id
        return self.get_player_list(fixture_list_id)

    def get_roster_format_in_entry(self, entry_id):
        """Retrieve roster format of given entry

        Parameters
        ----------
        entry_id : str
            id of entry to get roster format for
        """
        entry = self.get_entry(entry_id)
        print(entry)
        fixture_list = self.get_fixture_list(entry.fixture_list_id)
        print(fixture_list)
        game_description_id = fixture_list.game_description['_members'][0]
        game_description = self.get_game_description(game_description_id)
        return game_description.roster_format

    def update_entries(self, update_entry_inputs):
        """Update a given set of Fanduel entries with new rosters

        Parameters
        ----------
        update_entry_inputs : list[UpdateEntryInput]
            Required input to update a set of entries
        """
        entries = []
        for entry_input in update_entry_inputs:
            entry_id = entry_input.id
            roster_format = self.get_roster_format_in_entry(entry_id)

            # Ensure lineup length == length of game description slots
            if (len(entry_input.lineup) != len(roster_format)):
                raise Exception(
                    'Given lineup does not have the same amount of slots as the selected entry')

            # Match up each roster slot with the player in the lineup
            slot_counter = 0
            lineup = []
            for roster_slot in roster_format:
                corresponding_player = entry_input.lineup[slot_counter]
                # Make sure the player's position matches up
                if corresponding_player.position in roster_slot["player_positions"]:
                    lineup.append({"position": roster_slot["name"], "player": {
                                  "id": corresponding_player.id}})
                else:
                    raise Exception(
                        'Selected player has invalid position')
                slot_counter += 1
            entries.append({"id": entry_id, "roster": {"lineup": lineup}})
        update_entries_json = {"entries": entries}
        update_entries_response = requests.put(
            'https://api.fanduel.com/users/' + self.user_auth.user_id + '/entries',
            headers=self.fanduel_headers, json=update_entries_json).json()
        success_count = update_entries_response['_meta']['operations']['success_count']
        failure_count = update_entries_response['_meta']['operations']['failure_count']
        print('Update Entries Result:\nSuccess Count:{0}\nFailure Count:{1}'.format(
            success_count, failure_count))
        return update_entries_response

    def __authenticate(self):
        """Create UserAuth object to use when communicating with Fanduel API
        """
        body = {"email": self.fanduel_email,
                "password": self.fanduel_password, "product": "DFS"}
        current_response_json = requests.get(
            'https://api.fanduel.com/users/current',
            headers=self.fanduel_headers).json()
        if current_response_json and len(current_response_json['users']) > 0:
            # Succesfully sent off a request with the given credentials
            user = current_response_json['users'][0]
            self.user_auth.user_id = user['id']
            print("#######################\nLogged in Fanduel user: ",
                  user['username'], "\n#######################\n")
        else:
            raise Exception(
                '#######################\nError Authenticating Fanduel User\n#######################\n')

    def __create_fanduel_headers(self):
        headers = {'authority': 'api.fanduel.com',
                   'accept': 'application/json',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                   'content-type': 'application/json',
                   'origin': 'https://www.fanduel.com',
                   'sec-fetch-site': 'same-site',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-dest': 'empty',
                   'referer': 'https://www.fanduel.com/',
                   'accept-language': 'en-US,en;q=0.9'
                   }

        if(self.user_auth):
            headers['x-auth-token'] = self.user_auth.session_token
            headers['authorization'] = self.user_auth.basic_auth_token
        else:
            raise Exception('Error refreshing fanduel headers')
        return headers

    def __get_upcoming_data(self):
        """Retrieve all of user's upcoming data from Fanduel API
        """
        # Get all upcoming entries
        entries_response = requests.get(
            'https://api.fanduel.com/users/' +
            self.user_auth.user_id + '/entries?status=upcoming',
            headers=self.fanduel_headers).json()
        # Get list of players for each fixture list
        player_lists = []
        for i in entries_response['fixture_lists']:
            players_response = requests.get(
                i['players']['_url'],
                headers=self.fanduel_headers).json()
            player_lists.append(PlayerList({"fixture_list_id": i["id"], "players": [Player(player)
                                                                                    for player in players_response['players']]}))
        return Upcoming({"entries": [Entry(entry)
                                     for entry in entries_response['entries']],
                        "contests": [Contest(contest)
                                     for contest in entries_response['contests']],
                         "fixtures": [Fixture(fixture)
                                      for fixture in entries_response['fixtures']],
                         "rosters": [Roster(roster)
                                     for roster in entries_response['rosters']],
                         "game_descriptions": [GameDescription(game_description)
                                               for game_description in entries_response['game_descriptions']],
                         "fixture_lists": [FixtureList(fixture_list)
                                           for fixture_list in entries_response['fixture_lists']],
                         "player_lists": player_lists
                         })
