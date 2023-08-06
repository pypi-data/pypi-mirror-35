# Standard Imports
import urllib.request
import json


class Player:
    """Class with attributes of a Runescape Player using Jagex's RS3 API

    Most of Runescape 3's API can be accessed at: http://runescape.wikia.com/wiki/Application_programming_interface

    ...

    Parameters:
    ----------
    name : str
        Name of the Player, gets set to case-sensitive name later if his RuneMetrics profile is
        not private. If you're also working with clans, the player's RuneMetrics profile is private, his name should be
        passed case-sensitively. Otherwise some clan attributes will not be available.

    Attributes:
    ----------
    name : str
        Name of the Player, gets set to case-sensitive name later if his RuneMetrics profile is not private.
    exp : int or None
        Total Exp of the player, or None if private_profile is True.
    combat_level : int or None
        Total Combat Level of the player, or None if private_profile is True.
    total_level : int or None
        Total Skill Level of the player, or None if private_profile is True.
    private_profile : bool
        If the player has a private RuneMetrics profile or not.
    exists : bool
        If the player exists or not.
    """

    def __init__(self, name: str):

        self.name = name
        self.metrics_info = None
        self.exp = None
        self.combat_level = None
        self.total_level = None
        self.private_profile = True
        self.exists = True

        # If user's runemetrics profile is private, self.name will be the same as passed when creating object.
        # Otherwise it will get the correct case-sensitive name from his runemetrics profile.
        # Some other info like Total exp, Combat level and Total level will be created as well.
        if self.runemetrics_info():
            self.metrics_info = self.runemetrics_info()
            self.name = self.metrics_info['name']
            self.exp = self.metrics_info['totalxp']
            self.combat_level = self.metrics_info['combatlevel']
            self.total_level = self.metrics_info['totalskill']
        self.info = self._dict_info()
        self.suffix = self.info['is_suffix']
        self.title = self.info['title']
        try:
            self.clan = self.info['clan']
        except KeyError:
            self.clan = None

    def _raw_info(self):
        """
        Gets JsonP information on a player, in string format.

        Returns
        ------
        str
            JsonP information on player, converted to string.

        ------
        .. note:: Has to be formatted correctly into Json or other formats to be worked with properly first.
        """

        info_url = (f"http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22{self.name}"
                    f"%22%5D&callback=jQuery000000000000000_0000000000&_=0")
        client = urllib.request.urlopen(info_url)
        return str(client.read())

    def _dict_info(self):
        """
        Gets the raw string info from self._raw_info() and formats it into Dictionary format.:
        Used to set self.info.

        Returns
        ------
        dict
            Dictionary is formatted as follows::
                >>> player_info = {
                ... 'is_suffix': True,
                ... 'recruiting': True,
                ... 'name': 'nriver',
                ... 'clan': 'Atlantis',
                ... 'title': 'the Liberator'
                ... }
            is_suffix : bool
                If the player's title is a Suffix or not
            recruiting : bool
                If the player's clan is set as Recruiting or not
            name : str
                The player's name, passed as is when creating object Player
            clan : str
                The player's clan name
            title : str
                The player's current title
        """
        str_info = self._raw_info()
        info_list = []
        # str_info[36] = Start of json format in URL '{'
        for letter in str_info[36:]:
            info_list.append(letter)
            if letter == '}':
                break
        info_list = ''.join(info_list)
        info_dict = json.loads(info_list)
        info_dict['is_suffix'] = info_dict['isSuffix']
        del info_dict['isSuffix']
        return info_dict

    def runemetrics_info(self):
        """
        Gets player info from Runemetrics' API.
        Sets self.private_profile to True if his Runemetrics profile is found to be Private.

        Returns
        ------
        dict or bool
            Runemetrics player info if the player profile is public, or False if it is Private.
        """
        user_name = self.name.replace(' ', '%20')
        info_url = f"https://apps.runescape.com/runemetrics/profile/profile?user={user_name}&activities=0"
        client = urllib.request.urlopen(info_url)
        info = client.read()
        json_info = json.loads(info)
        try:
            if json_info['error'] == 'PROFILE_PRIVATE':
                self.private_profile = True
                return False
            if json_info['error'] == 'NO_PROFILE':
                self.private_profile = False
                self.exists = False
                return False
        except KeyError:
            self.private_profile = False
            return json_info


if __name__ == '__main__':
    # Creating Player with the name "nriver"
    player = Player("nriver")

    # Player name (Actual case-sensitive name if Runemetrics profile isn't private, otherwise it will be as passed)
    print(player.name)

    # Player info
    print(player.info)

    # Player clan
    print(player.clan)

    # Player title
    print(player.title)

    # If the player's title is a suffix or not
    print(player.suffix)

    # Prints the total player exp (if his Runemetrics profile is private it will output 0)
    print(player.exp)

    # Prints the Combat level of player (if his Runemetrics profile is private it will output 0)
    print(player.combat_level)

    # Prints the Total level of player (if his Runemetrics profile is private it will output 0)
    print(player.total_level)
