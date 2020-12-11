import sys
# This is an UGLY solution. I was unable to get proper packaging to work, and it may be a Windows-specific directory based problem.
# (Notice the path uses the D:\ drive as opposed to C:\)
sys.path.append('d:/Program Projects/GitHubRepos/RPG/rpg_program/source/')

import player as p
TEST_PROFILE = {
    'name' : 'Cuatro',
    'health': 150,
    'attack': 25,
    'defense': 10,
    'intellect': 10,
    'role': 'admin',
    'charisma': 100,
    'luck': 100,
    'perception': 100,
}
