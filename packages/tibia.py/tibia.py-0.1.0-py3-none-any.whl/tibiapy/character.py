import datetime
import json
import re
import urllib.parse
from collections import OrderedDict
from typing import Optional, List

import bs4

from . import abc
from .const import CHARACTER_URL
from .utils import parse_tibia_datetime

deleted_regexp = re.compile(r'([^,]+), will be deleted at (.*)')
# Extracts the death's level and killers.
death_regexp = re.compile(r'Level (?P<level>\d+) by (?P<killers>.*)\.</td>')
# From the killers list, filters out the assists.
death_assisted = re.compile(r'(?P<killers>.+)\.<br/>Assisted by (?P<assists>.+)')
# From a killer entry, extracts the summoned creature
death_summon = re.compile(r'(?P<summon>.+) of <a[^>]+>(?P<name>[^<]+)</a>')
# Extracts the contents of a tag
link_content = re.compile(r'>([^<]+)<')

house_regexp = re.compile(r'paid until (.*)')
guild_regexp = re.compile(r'([\s\w]+)\sof the\s(.+)')


class Character(abc.Character):
    """Represents a Tibia character

    Attributes
    ---------------
    name: :class:`str`
        The name of the character.

    deletion_date: Optional[:class:`datetime.datetime`]
        The date where the character will be deleted if it is scheduled for deletion.

    former_names: List[:class:`str`]
        Previous names of this character.

    sex: :class:`str`
        The character's gender, either "male" or "female"

    vocation: :class:`str`
        The character's vocation.

    level: :class:`int`
        The character's level.

    achievement_points: :class:`int`
        The total of points the character has.

    world: :class:`str`
        The character's current world

    former_world: Optional[:class:`str`]
        The previous world where the character was in, in the last 6 months.

    residence: :class:`str`
        The current hometown of the character.

    married_to: Optional[:class:`str`]
        The name of the character's spouse/husband.

    house: Optional[:class:`dict`]
        The house currently owned by the character.

    guild_membership: Optional[:class:`dict`]
        The guild the character is a member of. The dictionary contains a key for the rank and a key for the name.

    last_login: Optional[:class:`datetime.datetime`]
        The last time the character logged in. It will be None if the character has never logged in.

    comment: Optional[:class:`str`]
        The displayed comment.

    account_status: :class:`str`
        Whether the character's account is Premium or Free.

    achievements: List[:class:`dict`]
        The achievements chosen to be displayed.

    deaths: List[:class:`Death`]
        The character's recent deaths.

    account_information: :class:`dict`
        The character's account information, if visible.

    other_characters: List[:class:`OtherCharacter`]
        Other characters in the same account, if visible.
    """
    __slots__ = ("former_names", "sex", "vocation", "level", "achievement_points", "world", "former_world", "residence",
                 "married_to", "house", "guild_membership", "last_login", "account_status", "comment", "achievements",
                 "deaths", "account_information", "other_characters", "deletion_date")

    def __init__(self, name=None, world=None, vocation=None, level=0, sex=None, **kwargs):
        self.name = name
        self.former_names = kwargs.get("former_names", [])
        self.sex = sex
        self.vocation = vocation
        self.level = level
        self.achievement_points = kwargs.get("achievement_points", 0)
        self.world = world
        self.former_world = kwargs.get("former_world")
        self.residence = kwargs.get("residence")
        self.married_to = kwargs.get("married_to")
        self.house = kwargs.get("house")
        self.guild_membership = kwargs.get("guild_membership")
        self.last_login = kwargs.get("last_login")
        self.account_status = kwargs.get("account_status")
        self.comment = kwargs.get("comment")
        self.achievements = kwargs.get("achievements",[])
        self.deaths = kwargs.get("deaths", [])
        self.account_information = kwargs.get("account_information")
        self.other_characters = kwargs.get("other_characters", [])
        self.deletion_date = kwargs.get("deletion_date")

    @property
    def guild_name(self):
        """Optional[:class:`str`]: The name of the guild the character belongs to, or `None`."""
        return self.guild_membership["guild"] if self.guild_membership else None

    @property
    def guild_rank(self):
        """Optional[:class:`str`]: The character's rank in the guild they belong to, or `None`."""
        return self.guild_membership["rank"] if self.guild_membership else None

    @staticmethod
    def _beautiful_soup(content):
        """
        Parses HTML content into a BeautifulSoup object.
        Parameters
        ----------
        content: :class:`str`
            The HTML content.

        Returns
        -------
        :class:`bs4.BeautifulSoup`: The parsed content.
        """
        return bs4.BeautifulSoup(content, 'html.parser', parse_only=bs4.SoupStrainer("div", class_="BoxContent"))

    @staticmethod
    def _parse(content):
        """
        Parses the character's page HTML content into a dictionary.

        Parameters
        ----------
        content: :class:`str`
            The HTML content of the character's page.

        Returns
        -------
        :class:`dict[str, Any]`
            A dictionary containing all the character's information.
        """
        parsed_content = Character._beautiful_soup(content)
        tables = Character._parse_tables(parsed_content)
        char = {}
        if "Character Information" in tables.keys():
            Character._parse_character_information(char, tables["Character Information"])
        else:
            return {}
        Character._parse_achievements(char, tables.get("Account Achievements", []))
        Character._parse_deaths(char, tables.get("Character Deaths", []))
        Character._parse_account_information(char, tables.get("Account Information", []))
        Character._parse_other_characters(char, tables.get("Characters", []))
        return char

    @staticmethod
    def _parse_account_information(char, rows):
        """
        Parses the character's account information

        Parameters
        ----------
        char: :class:`dict`[str,Any]
            Dictionary where information will be stored.
        rows: List[:class:`bs4.Tag`]
            A list of all rows contained in the table.
        """
        char["account_information"] = {}
        for row in rows:
            cols_raw = row.find_all('td')
            cols = [ele.text.strip() for ele in cols_raw]
            field, value = cols
            field = field.replace("\xa0", "_").replace(" ", "_").replace(":", "").lower()
            value = value.replace("\xa0", " ")
            char["account_information"][field] = value

    @staticmethod
    def _parse_achievements(char, rows):
        """
        Parses the character's displayed achievements

        Parameters
        ----------
        char: :class:`dict`[str,Any]
            Dictionary where information will be stored.
        rows: List[:class:`bs4.Tag`]
            A list of all rows contained in the table.
        """
        achievements = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) != 2:
                continue
            field, value = cols
            grade = str(field).count("achievement-grade-symbol")
            achievement = value.text.strip()
            achievements.append({
                "grade": grade,
                "name": achievement
            })
        char["achievements"] = achievements

    @staticmethod
    def _parse_character_information(char, rows):
        """
        Parses the character's basic information.

        Parameters
        ----------
        char: :class:`dict`[str,Any]
            Dictionary where information will be stored.
        rows: List[:class:`bs4.Tag`]
            A list of all rows contained in the table.
        """
        int_rows = ["level", "achievement_points"]
        for row in rows:
            cols_raw = row.find_all('td')
            cols = [ele.text.strip() for ele in cols_raw]
            field, value = cols
            field = field.replace("\xa0", "_").replace(" ", "_").replace(":", "").lower()
            value = value.replace("\xa0", " ")
            # This is a special case cause we need to see the link
            if field == "house":
                house_text = value
                paid_until = house_regexp.search(house_text).group(1)
                house_link = cols_raw[1].find('a')
                url = urllib.parse.urlparse(house_link["href"])
                query = urllib.parse.parse_qs(url.query)
                char["house"] = {
                    "town": query["town"][0],
                    "id": int(query["houseid"][0]),
                    "name": house_link.text.strip(),
                    "paid_until": paid_until
                }
                continue
            if field in int_rows:
                value = int(value)
            char[field] = value
        m = deleted_regexp.match(char["name"])
        if m:
            char["name"] = m.group(1)
            char["deletion_date"] = m.group(2)
        else:
            char["deletion_date"] = None

        if "guild_membership" in char:
            m = guild_regexp.match(char["guild_membership"])
            char["guild_membership"] = {
                'rank': m.group(1),
                'guild': m.group(2)
            }
        else:
            char["guild_membership"] = None

        if "former_names" in char:
            former_names = [fn.strip() for fn in char["former_names"].split(",")]
            char["former_names"] = former_names
        else:
            char["former_names"] = []

        if "married_to" not in char:
            char["married_to"] = None

    @staticmethod
    def _parse_deaths(char, rows):
        """
        Parses the character's recent deaths

        Parameters
        ----------
        char: :class:`dict`[str,Any]
            Dictionary where information will be stored.
        rows: List[:class:`bs4.Tag`]
            A list of all rows contained in the table.
        """
        deaths = []
        for row in rows:
            cols = row.find_all('td')
            death_time = cols[0].text.strip()
            death = str(cols[1]).replace("\xa0", " ")
            death_time = death_time.replace("\xa0", " ")
            death_info = death_regexp.search(death)
            if death_info:
                level = int(death_info.group("level"))
                killers_str = death_info.group("killers")
            else:
                continue
            assists = []
            # Check if the killers list contains assists
            assist_match = death_assisted.search(killers_str)
            if assist_match:
                # Filter out assists
                killers_str = assist_match.group("killers")
                # Split assists into a list.
                assists = Character._split_list(assist_match.group("assists"))
            killers = Character._split_list(killers_str)
            for (i, killer) in enumerate(killers):
                # If the killer contains a link, it is a player.
                if "href" in killer:
                    killer_dict = {"name": link_content.search(killer).group(1), "player": True}
                else:
                    killer_dict = {"name": killer, "player": False}
                # Check if it contains a summon.
                m = death_summon.search(killer)
                if m:
                    killer_dict["summon"] = m.group("summon")
                killers[i] = killer_dict
            for (i, assist) in enumerate(assists):
                # Extract names from character links in assists list.
                assists[i] = {"name": link_content.search(assist).group(1), "player": True}
            try:
                deaths.append({'time': death_time, 'level': level, 'killers': killers, 'assists': assists})
            except ValueError:
                # Some pvp deaths have no level, so they are raising a ValueError, they will be ignored for now.
                continue
        char["deaths"] = deaths

    @staticmethod
    def _parse_other_characters(char, rows):
        """
        Parses the character's other visible characters.

        Parameters
        ----------
        char: :class:`dict`[str,Any]
            Dictionary where information will be stored.
        rows: List[:class:`bs4.Tag`]
            A list of all rows contained in the table.
        """
        char["other_characters"] = []
        for row in rows:
            cols_raw = row.find_all('td')
            cols = [ele.text.strip() for ele in cols_raw]
            if len(cols) != 5:
                continue
            _name, world, status, __, __ = cols
            _name = _name.replace("\xa0", " ").split(". ")[1]
            char["other_characters"].append(
                {'name': _name, 'world': world, 'online': status == "online", 'deleted': status == "deleted"})

    @staticmethod
    def _parse_tables(parsed_content):
        """
        Parses the information tables contained in a character's page.

        Parameters
        ----------
        parsed_content: :class:`bs4.BeautifulSoup`
            A :class:`BeautifulSoup` object containing all the content.

        Returns
        -------
        :class:`OrderedDict`[str, List[:class:`bs4.Tag`]]
            A dictionary containing all the table rows, with the table headers as keys.
        """
        tables = parsed_content.find_all('table', attrs={"width": "100%"})
        output = OrderedDict()
        for table in tables:
            title = table.find("td").text
            output[title] = table.find_all("tr")[1:]
        return output

    @staticmethod
    def _split_list(items, separator=",", last_separator=" and "):
        """
        Splits a string listing elements into an actual list.

        Parameters
        ----------
        items: :class:`str`
            A string listing elements.
        separator: :class:`str`
            The separator between each item. A comma by default.
        last_separator: :class:`str`
            The separator used for the last item. ' and ' by default.

        Returns
        -------
        List[:class:`str`]
            A list containing each one of the items.
        """
        if items is None:
            return None
        items = items.split(separator)
        last_item = items[-1]
        last_split = last_item.split(last_separator)
        if len(last_split) > 1:
            items[-1] = last_split[0]
            items.append(last_split[1])
        return [e.strip() for e in items]

    @staticmethod
    def get_url(name):
        """Gets the Tibia.com URl for a given character name.

        Parameters
        ------------
        name: str
            The name of the character

        Returns
        --------
        str
            The URL to the character's page"""
        return CHARACTER_URL + urllib.parse.quote(name.encode('iso-8859-1'))

    @staticmethod
    def from_content(content) -> Optional['Character']:
        """Creates an instance of the class from the html content of the character's page.

        Parameters
        -----------
        content: :class:`str`
            The HTML content of the page.

        Returns
        ----------
        Optional[:class:`Character`]
            The character contained in the page, or None if the character doesn't exist.
        """
        char_json = Character._parse(content)
        if not char_json:
            return None
        try:
            if char_json["deletion_date"]:
                char_json["deletion_date"] = parse_tibia_datetime(char_json["deletion_date"])
            else:
                char_json["deletion_date"] = None

            # Some attributes require converting
            if "never" in char_json["last_login"]:
                char_json["last_login"] = None
            else:
                char_json["last_login"] = parse_tibia_datetime(char_json["last_login"])
            deaths = []
            for d in char_json["deaths"]:
                death = Death(**d)
                death.name = char_json["name"]
                deaths.append(death)
            char_json["deaths"] = deaths
            other_characters = []
            if char_json["other_characters"]:
                for o_char in char_json["other_characters"]:
                    other_characters.append(OtherCharacter(**o_char))
            char_json["other_characters"] = other_characters

            char = Character(**char_json)

        except KeyError as e:
            print(e)
            return None

        return char

    @staticmethod
    def parse_to_json(content, indent=None):
        """Static method that creates a JSON string from the html content of the character's page.

        Parameters
        -------------
        content: :class:`str`
            The HTML content of the page.
        indent: :class:`int`
            The number of spaces to indent the output with.

        Returns
        ------------
        :class:`str`
            A string in JSON format.
        """
        char_dict = Character._parse(content)
        return json.dumps(char_dict, indent=indent)


class Death:
    """
    Represents a death by a character

    Attributes
    -----------
    name: :class:`str`
        The name of the character this death belongs to.

    level: :class:`int`
        The level at which the death occurred.

    killers: List[:class:`Killer`]
        A list of all the killers involved.

    assists: List[:class:`Killer`]
        A list of characters that were involved, without dealing damage.

    time: :class:`datetime.datetime`
        The time at which the death occurred.
    """
    __slots__ = ("level", "killers", "time", "assists", "name")

    def __init__(self, name=None, level=0, **kwargs):
        self.name = name
        self.level = level
        self.killers = kwargs.get("killers", [])
        if self.killers and isinstance(self.killers[0], dict):
            self.killers = [Killer(**k) for k in self.killers]
        self.assists = kwargs.get("assists", [])
        if self.assists and isinstance(self.assists[0], dict):
            self.assists = [Killer(**k) for k in self.assists]
        time = kwargs.get("time")
        if isinstance(time, datetime.datetime):
            self.time = time
        elif isinstance(time, str):
            self.time = parse_tibia_datetime(time)
        else:
            self.time = None

    def __repr__(self):
        attributes = ""
        for attr in self.__slots__:
            if attr in ["name", "level"]:
                continue
            v = getattr(self, attr)
            if isinstance(v, int) and v == 0 and not isinstance(v, bool):
                continue
            if isinstance(v, list) and len(v) == 0:
                continue
            if v is None:
                continue
            attributes += ",%s=%r" % (attr, v)
        return "{0.__class__.__name__}({0.name!r},{0.level!r}{1})".format(self, attributes)

    @property
    def killer(self):
        """Optional[:class:`Killer`]: The first killer in the list.

        This is usually the killer that gave the killing blow."""
        return self.killers[0] if self.killers else None

    @property
    def by_player(self):
        """:class:`bool`: Whether the kill involves other characters."""
        return any([k.player and self.name != k.name for k in self.killers])


class Killer:
    """
    Represents a killer.

    A killer can be:

    a) Another character.
    b) A creature.
    c) A creature summoned by a character.

    Attributes
    -----------
    name: :class:`str`
        The name of the killer.
    player: :class:`bool`
        Whether the killer is a player or not.
    summon: Optional[:class:`str`]
        The name of the summoned creature, if applicable.
    """
    __slots__ = ("name", "player", "summon")

    def __init__(self, name=None, player=False, summon=None):
        self.name = name
        self.player = player
        self.summon = summon

    def __repr__(self):
        attributes = ""
        for attr in self.__slots__:
            if attr in ["name"]:
                continue
            v = getattr(self, attr)
            if isinstance(v, int) and v == 0 and not isinstance(v, bool):
                continue
            if isinstance(v, list) and len(v) == 0:
                continue
            if v is None:
                continue
            attributes += ",%s=%r" % (attr, v)
        return "{0.__class__.__name__}({0.name!r}{1})".format(self, attributes)

    @property
    def url(self):
        """
        Optional[:class:`str`]: The URL of the character’s information page on Tibia.com, if applicable.
        """
        return Character.get_url(self.name) if self.player else None


class OtherCharacter(abc.Character):
    """
    Represents other character's displayed in the Character's information page.

    Attributes
    ----------
    name: :class:`str`
        The name of the character.

    world: :class:`str`
        The name of the world.

    online: :class:`bool`
        Whether the character is online or not.

    deleted: :class:`bool`
        Whether the character is scheduled for deletion or not.
    """
    __slots__ = ("world", "online", "deleted")

    def __init__(self, name=None, world=None, online = False, deleted = False):
        self.name = name
        self.world = world
        self.online = online
        self.deleted = deleted

