cities = ['TEHRAN', 'MASHHAD', 'TABRIZ', 'ISFAHAN', 'YAZD', 'KARAJ', 'AHVAZ', 'KERMAN', \
    'BOJNORD', 'SARI', 'BIRJAND', 'HAMADAN', 'ARAK', 'GORGAN', 'RASHT', 'ORUMIEH', 'BUSHEHR', \
    'SHAHR KORD', 'SANANDAJ', 'ZAHEDAN', 'BANDAR ABBAS', 'KERMANSHAH', 'SHIRAZ', 'KARAJ']

companies = ['SONY', 'MICROSOFT', 'ELECTRONIC ARTS', 'UBISOFT', 'SQUARE ENIX', 'CAPCOM', \
    'BLIZZARD', 'ACTIVISION', '2K GAMES', '505 GAMES', 'BETHESDA', 'SEGA', 'VALVE', 'ATARI' \
    'BANDAI NAMCO', 'DEEP SILVER', 'DIVOLVER DIGITAL', 'EPIC GAMES', 'GEARBOX', 'id SOFTWARE', \
    'KONAMI', 'NINTENDO', 'RIOT GAMES', 'ROCKSTAR', 'FROM SOFTWARE']

departments = ['SANTAMONICA', 'THERAN', 'MASHHAD', 'AUSTIN', 'CALIFORNIA', 'PARIS', 'TOKYO', 'BEIJING', 'DOHA']

games = [ {
        'brand': 'sony',
        'name': 'Bloodborne',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'sony',
        'name': 'Uncharted 4',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'sony',
        'name': 'God of War',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'sony',
        'name': 'The Last of Us',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'sony',
        'name': 'Horizon',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'sony',
        'name': 'Crash Bandicoot',
        'ptype': 'video_game',
        'gtype': 'action'
    }, {
        'brand': 'microsoft',
        'name': 'Forza Horizon',
        'ptype': 'video_game',
        'gtype': 'racing'
    }, {
        'brand': 'microsoft',
        'name': 'Gears of War',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'microsoft',
        'name': 'Halo',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Nintendo',
        'name': 'The Legend of Zelda',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Nintendo',
        'name': 'Super Mario',
        'ptype': 'video_game',
        'gtype': 'platformer'
    }
    , {
        'brand': 'Nintendo',
        'name': 'Mario Cart',
        'ptype': 'video_game',
        'gtype': 'racing'
    }
    , {
        'brand': 'EA',
        'name': 'FIFA',
        'ptype': 'video_game',
        'gtype': 'sports'
    }
    , {
        'brand': 'EA',
        'name': 'Dragon Age',
        'ptype': 'video_game',
        'gtype': 'action_adeventure'
    }
    , {
        'brand': 'EA',
        'name': 'Titanfall',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'EA',
        'name': 'Dead Space',
        'ptype': 'video_game',
        'gtype': 'horror'
    }
    , {
        'brand': 'EA',
        'name': 'Mass Effect',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'EA',
        'name': 'Battlefield',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'EA',
        'name': 'Sims',
        'ptype': 'video_game',
        'gtype': 'simulation'
    }
    , {
        'brand': 'Ubisoft',
        'name': "Assassin's Creed",
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Ubisoft',
        'name': 'Farcdy',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Ubisoft',
        'name': 'Sims',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Ubisoft',
        'name': 'Tom Clancy\'s',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Blizzard',
        'name': 'Warcraft',
        'ptype': 'video_game',
        'gtype': 'strategy'
    }
    , {
        'brand': 'Blizzard',
        'name': 'Starcraft',
        'ptype': 'video_game',
        'gtype': 'strategy'
    }
    , {
        'brand': 'Blizzard',
        'name': 'Diablo',
        'ptype': 'video_game',
        'gtype': 'hack_and_slash'
    }
    , {
        'brand': 'Blizzard',
        'name': 'Overwatch',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Activision',
        'name': 'Sekiro',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Activision',
        'name': 'Call of Duty',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Squre Enix',
        'name': 'Final Fantasy',
        'ptype': 'video_game',
        'gtype': 'role_playing'
    }
    , {
        'brand': 'Capcom',
        'name': 'Street Fighter',
        'ptype': 'video_game',
        'gtype': 'fighting'
    }
    , {
        'brand': 'Capcom',
        'name': 'Monster Hunter',
        'ptype': 'video_game',
        'gtype': 'role_playing'
    }
    , {
        'brand': 'Capcom',
        'name': 'Resident Evil',
        'ptype': 'video_game',
        'gtype': 'horror'
    }
    , {
        'brand': 'Capcom',
        'name': 'Devil May Cry',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Bethesda',
        'name': 'Fallout',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Bethesda',
        'name': 'Dishonored',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Bethesda',
        'name': 'Doom',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Bethesda',
        'name': 'Wolfenstain',
        'ptype': 'video_game',
        'gtype': 'action'
    }
    , {
        'brand': 'Bethesda',
        'name': 'The Elder Scrolls',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Bethesda',
        'name': 'The Evil Within',
        'ptype': 'video_game',
        'gtype': 'horror'
    }
    , {
        'brand': 'Rockstar',
        'name': 'Grand Theft Auto',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
    , {
        'brand': 'Rockstar',
        'name': 'Red Dead Redemption',
        'ptype': 'video_game',
        'gtype': 'action_adventure'
    }
]

consoles = [
    {
        'brand': 'sony',
        'name': 'playstation 4',
        'price': 10000000,
    },
    {
        'brand': 'sony',
        'name': 'playstation 5',
        'price': 30000000,
    },
    {
        'brand': 'microsoft',
        'name': 'xbox series s',
        'price': 12000000,
    },
    {
        'brand': 'microsoft',
        'name': 'xbox series x',
        'price': 23000000,
    },
    {
        'brand': 'microsoft',
        'name': 'xbox one',
        'price': 12500000,
    },
    {
        'brand': 'nintendo',
        'name': 'nintendo switch',
        'price': 14000000,
    },
]


