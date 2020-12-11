import sys
# This is an UGLY solution. I was unable to get proper packaging to work, and it may be a Windows-specific directory based problem.
# (Notice the path uses the D:\ drive as opposed to C:\)
sys.path.append('d:/Program Projects/GitHubRepos/RPG/rpg_program/source/')

import monsters as m

def test_exceptionIfBaseMonsterInvoked():
    try:
        baseMonster = m.Monster()
        return False
    except NotImplementedError:
        return True

def test_exceptionIfBaseArchtypeInvoked():
    try:
        baseArchtype = m.Archtype()
        return False
    except NotImplementedError:
        return True
