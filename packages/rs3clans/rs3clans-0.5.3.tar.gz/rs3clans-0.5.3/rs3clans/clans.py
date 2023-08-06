# Standard Imports
import csv
import requests


class ClanNotFoundError(Exception):
    """
    Error exception to be called when a clan is not found when trying to read the clan's URL using Rs3's Official API.

    Correct error handling when reading a clan:

    >>> import rs3clans
    >>> try:
    ...     clan_name = "=nfnewweunfiwnfskdnfjnwui"  # Invalid clan name
    ...     clan = rs3clans.Clan("name=clan_name")
    ... except rs3clans.ClanNotFoundError:
    ...     print("Exception encountered!")  # Handle error here
    Exception encountered!
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))


class Clan:

    def __init__(self, name, set_exp=False, set_dict=True, rank_key='rank', exp_key='exp'):
        """
        self.name = The name of the clan. Set when creating object.
        self.exp = The total Exp of the clan.
        self.member = Gets all the info from members of the clan in the dictionary format below:
        self.count = The number of members in the Clan.
        self.avg_exp = The average clan exp per member in the Clan.

        self.member = {
                'player_1': {
                    exp_key: 225231234,
                    rank_key: 'Leader'
                },
                'player_2': {
                    exp_key: 293123082,
                    rank_key: 'Overseer'
                }
            }

        For self.exp to be calculated, argument set_exp has to be True. (False by default)
        For self.member and self.coun to be made, argument set_dict has to be True. (True by default)
        For self.avg_exp both set_exp and set_dict have to be True
        """
        self.name = name
        self.exp = None
        self.member = None

        if set_exp is True:
            self.exp = self.list_sum()
        if set_dict is True:
            self.member = self.dict_lookup()
            self.count = len(self.member)
        if set_exp is True and set_dict is True:
            self.avg_exp = self.exp / self.count

    def list_lookup(self):
        """
        Used for getting all information available from a clan using Rs3's Clan API.

        Returns it with a list format.

        Mainly used for calculating the total exp of a clan manually.

        Look at dict_lookup() and self.member for info from specific members of the clan.
        """
        clan_url = f'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={self.name}'

        with requests.Session() as session:
            download = session.get(clan_url)
            decoded = download.content.decode('windows-1252')
            return list(csv.reader(decoded.splitlines(), delimiter=','))

    def dict_lookup(self, rank_key="rank", exp_key="exp"):
        """
        Used for getting all information available from a clan using Rs3's Clan API.

        Contrary to list_lookup() it returns it as a Dictionary format instead.
        The dictformat makes easier to find info specific to certain members of the Clan instead of looping over it.

        It's used for making self.member dictionary when set_dict argument is passed as true when creating a Clan object.
        """
        clan_list = self.list_lookup()
        clan_dict = {}

        for row in clan_list[1:]:
            user_rank = row[1]
            username = row[0]
            user_exp = int(row[2])

            clan_dict[username] = {
                rank_key: user_rank,
                exp_key: user_exp
            }
        return clan_dict

    def list_sum(self):
        """
        Sums the total exp of a clan.
        It's used for making self.exp when set_exp argument is passed as true when creating a Clan object.
        """
        clan_list = self.list_lookup()
        return sum(int(row[2]) for row in clan_list[1:])

    def dict_sum(self):
        """
        Deprecated. Use list_sum() instead. It's faster.
        """
        clan_dict = self.dict_lookup()
        return sum(members['exp'] for members in clan_dict.values())


if __name__ == '__main__':
    # Create Clan with the name "Atlantis"
    clan = Clan("Atlantis", set_exp=True)

    # Info from member "NRiver" (case-sensitive)
    print(clan.member['NRiver'])

    # Total Exp of the clan
    print(clan.exp)

    # Average Clan Exp per Member of the clan
    print(clan.avg_exp)

    # Clan Name as passed when creating object Clan
    print(clan.name)

    # Number of members in clan
    print(clan.count)
