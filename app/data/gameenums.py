from enum import Enum, IntEnum
from typing import Dict


class SvtType(IntEnum):
    NORMAL = 1
    HEROINE = 2
    COMBINE_MATERIAL = 3
    ENEMY = 4
    ENEMY_COLLECTION = 5
    SERVANT_EQUIP = 6
    STATUS_UP = 7
    SVT_EQUIP_MATERIAL = 8
    ENEMY_COLLECTION_DETAIL = 9
    ALL = 10
    COMMAND_CODE = 11


class NiceSvtType(str, Enum):
    normal = "normal"
    heroine = "heroine"
    combineMaterial = "combineMaterial"
    enemy = "enemy"
    enemyCollection = "enemyCollection"
    servantEquip = "servantEquip"
    statusUp = "statusUp"
    svtEquipMaterial = "svtEquipMaterial"
    enemyCollectionDetail = "enemyCollectionDetail"
    all = "all"
    commandCode = "commandCode"


SVT_TYPE_NAME: Dict[int, NiceSvtType] = {
    1: NiceSvtType.normal,
    2: NiceSvtType.heroine,
    3: NiceSvtType.combineMaterial,
    4: NiceSvtType.enemy,
    5: NiceSvtType.enemyCollection,
    6: NiceSvtType.servantEquip,
    7: NiceSvtType.statusUp,
    8: NiceSvtType.svtEquipMaterial,
    9: NiceSvtType.enemyCollectionDetail,
    10: NiceSvtType.all,
    11: NiceSvtType.commandCode,
}


class FuncType(IntEnum):
    NONE = 0
    ADD_STATE = 1
    SUB_STATE = 2
    DAMAGE = 3
    DAMAGE_NP = 4
    GAIN_STAR = 5
    GAIN_HP = 6
    GAIN_NP = 7
    LOSS_NP = 8
    SHORTEN_SKILL = 9
    EXTEND_SKILL = 10
    RELEASE_STATE = 11
    LOSS_HP = 12
    INSTANT_DEATH = 13
    DAMAGE_NP_PIERCE = 14
    DAMAGE_NP_INDIVIDUAL = 15
    ADD_STATE_SHORT = 16
    GAIN_HP_PER = 17
    DAMAGE_NP_STATE_INDIVIDUAL = 18
    HASTEN_NPTURN = 19
    DELAY_NPTURN = 20
    DAMAGE_NP_HPRATIO_HIGH = 21
    DAMAGE_NP_HPRATIO_LOW = 22
    CARD_RESET = 23
    REPLACE_MEMBER = 24
    LOSS_HP_SAFE = 25
    DAMAGE_NP_COUNTER = 26
    DAMAGE_NP_STATE_INDIVIDUAL_FIX = 27
    DAMAGE_NP_SAFE = 28
    CALL_SERVANT = 29
    PT_SHUFFLE = 30
    LOSS_STAR = 31
    CHANGE_SERVANT = 32
    CHANGE_BG = 33
    DAMAGE_VALUE = 34
    WITHDRAW = 35
    FIX_COMMANDCARD = 36
    SHORTEN_BUFFTURN = 37
    EXTEND_BUFFTURN = 38
    SHORTEN_BUFFCOUNT = 39
    EXTEND_BUFFCOUNT = 40
    CHANGE_BGM = 41
    DISPLAY_BUFFSTRING = 42
    RESURRECTION = 43
    GAIN_NP_BUFF_INDIVIDUAL_SUM = 44
    SET_SYSTEM_ALIVE_FLAG = 45
    FORCE_INSTANT_DEATH = 46
    DAMAGE_NP_RARE = 47
    GAIN_NP_FROM_TARGETS = 48
    GAIN_HP_FROM_TARGETS = 49
    LOSS_HP_PER = 50
    LOSS_HP_PER_SAFE = 51
    SHORTEN_USER_EQUIP_SKILL = 52
    QUICK_CHANGE_BG = 53
    SHIFT_SERVANT = 54
    DAMAGE_NP_AND_CHECK_INDIVIDUALITY = 55
    ABSORB_NPTURN = 56
    OVERWRITE_DEAD_TYPE = 57
    FORCE_ALL_BUFF_NOACT = 58
    BREAK_GAUGE_UP = 59
    BREAK_GAUGE_DOWN = 60
    EXP_UP = 101
    QP_UP = 102
    DROP_UP = 103
    FRIEND_POINT_UP = 104
    EVENT_DROP_UP = 105
    EVENT_DROP_RATE_UP = 106
    EVENT_POINT_UP = 107
    EVENT_POINT_RATE_UP = 108
    TRANSFORM_SERVANT = 109
    QP_DROP_UP = 110
    SERVANT_FRIENDSHIP_UP = 111
    USER_EQUIP_EXP_UP = 112
    CLASS_DROP_UP = 113
    ENEMY_ENCOUNT_COPY_RATE_UP = 114
    ENEMY_ENCOUNT_RATE_UP = 115
    ENEMY_PROB_DOWN = 116
    GET_REWARD_GIFT = 117
    SEND_SUPPORT_FRIEND_POINT = 118
    MOVE_POSITION = 119
    REVIVAL = 120
    DAMAGE_NP_INDIVIDUAL_SUM = 121
    DAMAGE_VALUE_SAFE = 122
    FRIEND_POINT_UP_DUPLICATE = 123


class NiceFuncType(str, Enum):
    none = "none"
    addState = "addState"
    subState = "subState"
    damage = "damage"
    damageNp = "damageNp"
    gainStar = "gainStar"
    gainHp = "gainHp"
    gainNp = "gainNp"
    lossNp = "lossNp"
    shortenSkill = "shortenSkill"
    extendSkill = "extendSkill"
    releaseState = "releaseState"
    lossHp = "lossHp"
    instantDeath = "instantDeath"
    damageNpPierce = "damageNpPierce"
    damageNpIndividual = "damageNpIndividual"
    addStateShort = "addStateShort"
    gainHpPer = "gainHpPer"
    damageNpStateIndividual = "damageNpStateIndividual"
    hastenNpturn = "hastenNpturn"
    delayNpturn = "delayNpturn"
    damageNpHpratioHigh = "damageNpHpratioHigh"
    damageNpHpratioLow = "damageNpHpratioLow"
    cardReset = "cardReset"
    replaceMember = "replaceMember"
    lossHpSafe = "lossHpSafe"
    damageNpCounter = "damageNpCounter"
    damageNpStateIndividualFix = "damageNpStateIndividualFix"
    damageNpSafe = "damageNpSafe"
    callServant = "callServant"
    ptShuffle = "ptShuffle"
    lossStar = "lossStar"
    changeServant = "changeServant"
    changeBg = "changeBg"
    damageValue = "damageValue"
    withdraw = "withdraw"
    fixCommandcard = "fixCommandcard"
    shortenBuffturn = "shortenBuffturn"
    extendBuffturn = "extendBuffturn"
    shortenBuffcount = "shortenBuffcount"
    extendBuffcount = "extendBuffcount"
    changeBgm = "changeBgm"
    displayBuffstring = "displayBuffstring"
    resurrection = "resurrection"
    gainNpBuffIndividualSum = "gainNpBuffIndividualSum"
    setSystemAliveFlag = "setSystemAliveFlag"
    forceInstantDeath = "forceInstantDeath"
    damageNpRare = "damageNpRare"
    gainNpFromTargets = "gainNpFromTargets"
    gainHpFromTargets = "gainHpFromTargets"
    lossHpPer = "lossHpPer"
    lossHpPerSafe = "lossHpPerSafe"
    shortenUserEquipSkill = "shortenUserEquipSkill"
    quickChangeBg = "quickChangeBg"
    shiftServant = "shiftServant"
    damageNpAndCheckIndividuality = "damageNpAndCheckIndividuality"
    absorbNpturn = "absorbNpturn"
    overwriteDeadType = "overwriteDeadType"
    forceAllBuffNoact = "forceAllBuffNoact"
    breakGaugeUp = "breakGaugeUp"
    breakGaugeDown = "breakGaugeDown"
    expUp = "expUp"
    qpUp = "qpUp"
    dropUp = "dropUp"
    friendPointUp = "friendPointUp"
    eventDropUp = "eventDropUp"
    eventDropRateUp = "eventDropRateUp"
    eventPointUp = "eventPointUp"
    eventPointRateUp = "eventPointRateUp"
    transformServant = "transformServant"
    qpDropUp = "qpDropUp"
    servantFriendshipUp = "servantFriendshipUp"
    userEquipExpUp = "userEquipExpUp"
    classDropUp = "classDropUp"
    enemyEncountCopyRateUp = "enemyEncountCopyRateUp"
    enemyEncountRateUp = "enemyEncountRateUp"
    enemyProbDown = "enemyProbDown"
    getRewardGift = "getRewardGift"
    sendSupportFriendPoint = "sendSupportFriendPoint"
    movePosition = "movePosition"
    revival = "revival"
    damageNpIndividualSum = "damageNpIndividualSum"
    damageValueSafe = "damageValueSafe"
    friendPointUpDuplicate = "friendPointUpDuplicate"


FUNC_TYPE_NAME: Dict[int, NiceFuncType] = {
    0: NiceFuncType.none,
    1: NiceFuncType.addState,
    2: NiceFuncType.subState,
    3: NiceFuncType.damage,
    4: NiceFuncType.damageNp,
    5: NiceFuncType.gainStar,
    6: NiceFuncType.gainHp,
    7: NiceFuncType.gainNp,
    8: NiceFuncType.lossNp,
    9: NiceFuncType.shortenSkill,
    10: NiceFuncType.extendSkill,
    11: NiceFuncType.releaseState,
    12: NiceFuncType.lossHp,
    13: NiceFuncType.instantDeath,
    14: NiceFuncType.damageNpPierce,
    15: NiceFuncType.damageNpIndividual,
    16: NiceFuncType.addStateShort,
    17: NiceFuncType.gainHpPer,
    18: NiceFuncType.damageNpStateIndividual,
    19: NiceFuncType.hastenNpturn,
    20: NiceFuncType.delayNpturn,
    21: NiceFuncType.damageNpHpratioHigh,
    22: NiceFuncType.damageNpHpratioLow,
    23: NiceFuncType.cardReset,
    24: NiceFuncType.replaceMember,
    25: NiceFuncType.lossHpSafe,
    26: NiceFuncType.damageNpCounter,
    27: NiceFuncType.damageNpStateIndividualFix,
    28: NiceFuncType.damageNpSafe,
    29: NiceFuncType.callServant,
    30: NiceFuncType.ptShuffle,
    31: NiceFuncType.lossStar,
    32: NiceFuncType.changeServant,
    33: NiceFuncType.changeBg,
    34: NiceFuncType.damageValue,
    35: NiceFuncType.withdraw,
    36: NiceFuncType.fixCommandcard,
    37: NiceFuncType.shortenBuffturn,
    38: NiceFuncType.extendBuffturn,
    39: NiceFuncType.shortenBuffcount,
    40: NiceFuncType.extendBuffcount,
    41: NiceFuncType.changeBgm,
    42: NiceFuncType.displayBuffstring,
    43: NiceFuncType.resurrection,
    44: NiceFuncType.gainNpBuffIndividualSum,
    45: NiceFuncType.setSystemAliveFlag,
    46: NiceFuncType.forceInstantDeath,
    47: NiceFuncType.damageNpRare,
    48: NiceFuncType.gainNpFromTargets,
    49: NiceFuncType.gainHpFromTargets,
    50: NiceFuncType.lossHpPer,
    51: NiceFuncType.lossHpPerSafe,
    52: NiceFuncType.shortenUserEquipSkill,
    53: NiceFuncType.quickChangeBg,
    54: NiceFuncType.shiftServant,
    55: NiceFuncType.damageNpAndCheckIndividuality,
    56: NiceFuncType.absorbNpturn,
    57: NiceFuncType.overwriteDeadType,
    58: NiceFuncType.forceAllBuffNoact,
    59: NiceFuncType.breakGaugeUp,
    60: NiceFuncType.breakGaugeDown,
    101: NiceFuncType.expUp,
    102: NiceFuncType.qpUp,
    103: NiceFuncType.dropUp,
    104: NiceFuncType.friendPointUp,
    105: NiceFuncType.eventDropUp,
    106: NiceFuncType.eventDropRateUp,
    107: NiceFuncType.eventPointUp,
    108: NiceFuncType.eventPointRateUp,
    109: NiceFuncType.transformServant,
    110: NiceFuncType.qpDropUp,
    111: NiceFuncType.servantFriendshipUp,
    112: NiceFuncType.userEquipExpUp,
    113: NiceFuncType.classDropUp,
    114: NiceFuncType.enemyEncountCopyRateUp,
    115: NiceFuncType.enemyEncountRateUp,
    116: NiceFuncType.enemyProbDown,
    117: NiceFuncType.getRewardGift,
    118: NiceFuncType.sendSupportFriendPoint,
    119: NiceFuncType.movePosition,
    120: NiceFuncType.revival,
    121: NiceFuncType.damageNpIndividualSum,
    122: NiceFuncType.damageValueSafe,
    123: NiceFuncType.friendPointUpDuplicate,
}


class FuncTargetType(IntEnum):
    SELF = 0
    PT_ONE = 1
    PT_ANOTHER = 2
    PT_ALL = 3
    ENEMY = 4
    ENEMY_ANOTHER = 5
    ENEMY_ALL = 6
    PT_FULL = 7
    ENEMY_FULL = 8
    PT_OTHER = 9
    PT_ONE_OTHER = 10
    PT_RANDOM = 11
    ENEMY_OTHER = 12
    ENEMY_RANDOM = 13
    PT_OTHER_FULL = 14
    ENEMY_OTHER_FULL = 15
    PTSELECT_ONE_SUB = 16
    PTSELECT_SUB = 17
    PT_ONE_ANOTHER_RANDOM = 18
    PT_SELF_ANOTHER_RANDOM = 19
    ENEMY_ONE_ANOTHER_RANDOM = 20
    PT_SELF_ANOTHER_FIRST = 21
    PT_SELF_BEFORE = 22
    PT_SELF_AFTER = 23
    PT_SELF_ANOTHER_LAST = 24
    COMMAND_TYPE_SELF_TREASURE_DEVICE = 25


class NiceFuncTargetType(str, Enum):
    self = "self"
    ptOne = "ptOne"
    ptAnother = "ptAnother"
    ptAll = "ptAll"
    enemy = "enemy"
    enemyAnother = "enemyAnother"
    enemyAll = "enemyAll"
    ptFull = "ptFull"
    enemyFull = "enemyFull"
    ptOther = "ptOther"
    ptOneOther = "ptOneOther"
    ptRandom = "ptRandom"
    enemyOther = "enemyOther"
    enemyRandom = "enemyRandom"
    ptOtherFull = "ptOtherFull"
    enemyOtherFull = "enemyOtherFull"
    ptselectOneSub = "ptselectOneSub"
    ptselectSub = "ptselectSub"
    ptOneAnotherRandom = "ptOneAnotherRandom"
    ptSelfAnotherRandom = "ptSelfAnotherRandom"
    enemyOneAnotherRandom = "enemyOneAnotherRandom"
    ptSelfAnotherFirst = "ptSelfAnotherFirst"
    ptSelfBefore = "ptSelfBefore"
    ptSelfAfter = "ptSelfAfter"
    ptSelfAnotherLast = "ptSelfAnotherLast"
    commandTypeSelfTreasureDevice = "commandTypeSelfTreasureDevice"


FUNC_TARGETTYPE_NAME: Dict[int, NiceFuncTargetType] = {
    0: NiceFuncTargetType.self,
    1: NiceFuncTargetType.ptOne,
    2: NiceFuncTargetType.ptAnother,
    3: NiceFuncTargetType.ptAll,
    4: NiceFuncTargetType.enemy,
    5: NiceFuncTargetType.enemyAnother,
    6: NiceFuncTargetType.enemyAll,
    7: NiceFuncTargetType.ptFull,
    8: NiceFuncTargetType.enemyFull,
    9: NiceFuncTargetType.ptOther,
    10: NiceFuncTargetType.ptOneOther,
    11: NiceFuncTargetType.ptRandom,
    12: NiceFuncTargetType.enemyOther,
    13: NiceFuncTargetType.enemyRandom,
    14: NiceFuncTargetType.ptOtherFull,
    15: NiceFuncTargetType.enemyOtherFull,
    16: NiceFuncTargetType.ptselectOneSub,
    17: NiceFuncTargetType.ptselectSub,
    18: NiceFuncTargetType.ptOneAnotherRandom,
    19: NiceFuncTargetType.ptSelfAnotherRandom,
    20: NiceFuncTargetType.enemyOneAnotherRandom,
    21: NiceFuncTargetType.ptSelfAnotherFirst,
    22: NiceFuncTargetType.ptSelfBefore,
    23: NiceFuncTargetType.ptSelfAfter,
    24: NiceFuncTargetType.ptSelfAnotherLast,
    25: NiceFuncTargetType.commandTypeSelfTreasureDevice,
}


class BuffType(IntEnum):
    NONE = 0
    UP_COMMANDATK = 1
    UP_STARWEIGHT = 2
    UP_CRITICALPOINT = 3
    DOWN_CRITICALPOINT = 4
    REGAIN_NP = 5
    REGAIN_STAR = 6
    REGAIN_HP = 7
    REDUCE_HP = 8
    UP_ATK = 9
    DOWN_ATK = 10
    UP_DAMAGE = 11
    DOWN_DAMAGE = 12
    ADD_DAMAGE = 13
    SUB_DAMAGE = 14
    UP_NPDAMAGE = 15
    DOWN_NPDAMAGE = 16
    UP_DROPNP = 17
    UP_CRITICALDAMAGE = 18
    DOWN_CRITICALDAMAGE = 19
    UP_SELFDAMAGE = 20
    DOWN_SELFDAMAGE = 21
    ADD_SELFDAMAGE = 22
    SUB_SELFDAMAGE = 23
    AVOIDANCE = 24
    BREAK_AVOIDANCE = 25
    INVINCIBLE = 26
    UP_GRANTSTATE = 27
    DOWN_GRANTSTATE = 28
    UP_TOLERANCE = 29
    DOWN_TOLERANCE = 30
    AVOID_STATE = 31
    DONOT_ACT = 32
    DONOT_SKILL = 33
    DONOT_NOBLE = 34
    DONOT_RECOVERY = 35
    DISABLE_GENDER = 36
    GUTS = 37
    UP_HATE = 38
    ADD_INDIVIDUALITY = 40
    SUB_INDIVIDUALITY = 41
    UP_DEFENCE = 42
    DOWN_DEFENCE = 43
    UP_COMMANDSTAR = 50
    UP_COMMANDNP = 51
    UP_COMMANDALL = 52
    DOWN_COMMANDALL = 60
    DOWN_STARWEIGHT = 61
    REDUCE_NP = 62
    DOWN_DROPNP = 63
    UP_GAIN_HP = 64
    DOWN_GAIN_HP = 65
    DOWN_COMMANDATK = 66
    DOWN_COMMANSTAR = 67
    DOWN_COMMANDNP = 68
    UP_CRITICALRATE = 70
    DOWN_CRITICALRATE = 71
    PIERCE_INVINCIBLE = 72
    AVOID_INSTANTDEATH = 73
    UP_RESIST_INSTANTDEATH = 74
    UP_NONRESIST_INSTANTDEATH = 75
    DELAY_FUNCTION = 76
    REGAIN_NP_USED_NOBLE = 77
    DEAD_FUNCTION = 78
    UP_MAXHP = 79
    DOWN_MAXHP = 80
    ADD_MAXHP = 81
    SUB_MAXHP = 82
    BATTLESTART_FUNCTION = 83
    WAVESTART_FUNCTION = 84
    SELFTURNEND_FUNCTION = 85
    UP_GIVEGAIN_HP = 87
    DOWN_GIVEGAIN_HP = 88
    COMMANDATTACK_FUNCTION = 89
    DEADATTACK_FUNCTION = 90
    UP_SPECIALDEFENCE = 91
    DOWN_SPECIALDEFENCE = 92
    UP_DAMAGEDROPNP = 93
    DOWN_DAMAGEDROPNP = 94
    ENTRY_FUNCTION = 95
    UP_CHAGETD = 96
    REFLECTION_FUNCTION = 97
    UP_GRANT_SUBSTATE = 98
    DOWN_GRANT_SUBSTATE = 99
    UP_TOLERANCE_SUBSTATE = 100
    DOWN_TOLERANCE_SUBSTATE = 101
    UP_GRANT_INSTANTDEATH = 102
    DOWN_GRANT_INSTANTDEATH = 103
    GUTS_RATIO = 104
    DAMAGE_FUNCTION = 86
    UP_DEFENCECOMMANDALL = 105
    DOWN_DEFENCECOMMANDALL = 106
    OVERWRITE_BATTLECLASS = 107
    OVERWRITE_CLASSRELATIO_ATK = 108
    OVERWRITE_CLASSRELATIO_DEF = 109
    UP_DAMAGE_INDIVIDUALITY = 110
    DOWN_DAMAGE_INDIVIDUALITY = 111
    UP_DAMAGE_INDIVIDUALITY_ACTIVEONLY = 112
    DOWN_DAMAGE_INDIVIDUALITY_ACTIVEONLY = 113
    UP_NPTURNVAL = 114
    DOWN_NPTURNVAL = 115
    MULTIATTACK = 116
    UP_GIVE_NP = 117
    DOWN_GIVE_NP = 118
    UP_RESISTANCE_DELAY_NPTURN = 119
    DOWN_RESISTANCE_DELAY_NPTURN = 120
    PIERCE_DEFENCE = 121
    UP_GUTS_HP = 122
    DOWN_GUTS_HP = 123
    UP_FUNCGAIN_NP = 124
    DOWN_FUNCGAIN_NP = 125
    UP_FUNC_HP_REDUCE = 126
    DOWN_FUNC_HP_REDUCE = 127
    UP_DEFENCECOMMAN_DAMAGE = 128
    DOWN_DEFENCECOMMAN_DAMAGE = 129
    NPATTACK_PREV_BUFF = 130
    FIX_COMMANDCARD = 131
    DONOT_GAINNP = 132
    FIELD_INDIVIDUALITY = 133
    DONOT_ACT_COMMANDTYPE = 134
    UP_DAMAGE_EVENT_POINT = 135
    UP_DAMAGE_SPECIAL = 136
    ATTACK_FUNCTION = 137
    COMMANDCODEATTACK_FUNCTION = 138
    DONOT_NOBLE_COND_MISMATCH = 139
    DONOT_SELECT_COMMANDCARD = 140
    DONOT_REPLACE = 141
    SHORTEN_USER_EQUIP_SKILL = 142
    TD_TYPE_CHANGE = 143
    OVERWRITE_CLASS_RELATION = 144
    TD_TYPE_CHANGE_ARTS = 145
    TD_TYPE_CHANGE_BUSTER = 146
    TD_TYPE_CHANGE_QUICK = 147
    COMMANDATTACK_BEFORE_FUNCTION = 148
    GUTS_FUNCTION = 149
    UP_CRITICAL_RATE_DAMAGE_TAKEN = 150
    DOWN_CRITICAL_RATE_DAMAGE_TAKEN = 151
    UP_CRITICAL_STAR_DAMAGE_TAKEN = 152
    DOWN_CRITICAL_STAR_DAMAGE_TAKEN = 153
    SKILL_RANK_UP = 154
    AVOIDANCE_INDIVIDUALITY = 155
    CHANGE_COMMAND_CARD_TYPE = 156
    SPECIAL_INVINCIBLE = 157


class NiceBuffType(str, Enum):
    none = "none"
    upCommandatk = "upCommandatk"
    upStarweight = "upStarweight"
    upCriticalpoint = "upCriticalpoint"
    downCriticalpoint = "downCriticalpoint"
    regainNp = "regainNp"
    regainStar = "regainStar"
    regainHp = "regainHp"
    reduceHp = "reduceHp"
    upAtk = "upAtk"
    downAtk = "downAtk"
    upDamage = "upDamage"
    downDamage = "downDamage"
    addDamage = "addDamage"
    subDamage = "subDamage"
    upNpdamage = "upNpdamage"
    downNpdamage = "downNpdamage"
    upDropnp = "upDropnp"
    upCriticaldamage = "upCriticaldamage"
    downCriticaldamage = "downCriticaldamage"
    upSelfdamage = "upSelfdamage"
    downSelfdamage = "downSelfdamage"
    addSelfdamage = "addSelfdamage"
    subSelfdamage = "subSelfdamage"
    avoidance = "avoidance"
    breakAvoidance = "breakAvoidance"
    invincible = "invincible"
    upGrantstate = "upGrantstate"
    downGrantstate = "downGrantstate"
    upTolerance = "upTolerance"
    downTolerance = "downTolerance"
    avoidState = "avoidState"
    donotAct = "donotAct"
    donotSkill = "donotSkill"
    donotNoble = "donotNoble"
    donotRecovery = "donotRecovery"
    disableGender = "disableGender"
    guts = "guts"
    upHate = "upHate"
    addIndividuality = "addIndividuality"
    subIndividuality = "subIndividuality"
    upDefence = "upDefence"
    downDefence = "downDefence"
    upCommandstar = "upCommandstar"
    upCommandnp = "upCommandnp"
    upCommandall = "upCommandall"
    downCommandall = "downCommandall"
    downStarweight = "downStarweight"
    reduceNp = "reduceNp"
    downDropnp = "downDropnp"
    upGainHp = "upGainHp"
    downGainHp = "downGainHp"
    downCommandatk = "downCommandatk"
    downCommanstar = "downCommanstar"
    downCommandnp = "downCommandnp"
    upCriticalrate = "upCriticalrate"
    downCriticalrate = "downCriticalrate"
    pierceInvincible = "pierceInvincible"
    avoidInstantdeath = "avoidInstantdeath"
    upResistInstantdeath = "upResistInstantdeath"
    upNonresistInstantdeath = "upNonresistInstantdeath"
    delayFunction = "delayFunction"
    regainNpUsedNoble = "regainNpUsedNoble"
    deadFunction = "deadFunction"
    upMaxhp = "upMaxhp"
    downMaxhp = "downMaxhp"
    addMaxhp = "addMaxhp"
    subMaxhp = "subMaxhp"
    battlestartFunction = "battlestartFunction"
    wavestartFunction = "wavestartFunction"
    selfturnendFunction = "selfturnendFunction"
    upGivegainHp = "upGivegainHp"
    downGivegainHp = "downGivegainHp"
    commandattackFunction = "commandattackFunction"
    deadattackFunction = "deadattackFunction"
    upSpecialdefence = "upSpecialdefence"
    downSpecialdefence = "downSpecialdefence"
    upDamagedropnp = "upDamagedropnp"
    downDamagedropnp = "downDamagedropnp"
    entryFunction = "entryFunction"
    upChagetd = "upChagetd"
    reflectionFunction = "reflectionFunction"
    upGrantSubstate = "upGrantSubstate"
    downGrantSubstate = "downGrantSubstate"
    upToleranceSubstate = "upToleranceSubstate"
    downToleranceSubstate = "downToleranceSubstate"
    upGrantInstantdeath = "upGrantInstantdeath"
    downGrantInstantdeath = "downGrantInstantdeath"
    gutsRatio = "gutsRatio"
    damageFunction = "damageFunction"
    upDefencecommandall = "upDefencecommandall"
    downDefencecommandall = "downDefencecommandall"
    overwriteBattleclass = "overwriteBattleclass"
    overwriteClassrelatioAtk = "overwriteClassrelatioAtk"
    overwriteClassrelatioDef = "overwriteClassrelatioDef"
    upDamageIndividuality = "upDamageIndividuality"
    downDamageIndividuality = "downDamageIndividuality"
    upDamageIndividualityActiveonly = "upDamageIndividualityActiveonly"
    downDamageIndividualityActiveonly = "downDamageIndividualityActiveonly"
    upNpturnval = "upNpturnval"
    downNpturnval = "downNpturnval"
    multiattack = "multiattack"
    upGiveNp = "upGiveNp"
    downGiveNp = "downGiveNp"
    upResistanceDelayNpturn = "upResistanceDelayNpturn"
    downResistanceDelayNpturn = "downResistanceDelayNpturn"
    pierceDefence = "pierceDefence"
    upGutsHp = "upGutsHp"
    downGutsHp = "downGutsHp"
    upFuncgainNp = "upFuncgainNp"
    downFuncgainNp = "downFuncgainNp"
    upFuncHpReduce = "upFuncHpReduce"
    downFuncHpReduce = "downFuncHpReduce"
    upDefencecommanDamage = "upDefencecommanDamage"
    downDefencecommanDamage = "downDefencecommanDamage"
    npattackPrevBuff = "npattackPrevBuff"
    fixCommandcard = "fixCommandcard"
    donotGainnp = "donotGainnp"
    fieldIndividuality = "fieldIndividuality"
    donotActCommandtype = "donotActCommandtype"
    upDamageEventPoint = "upDamageEventPoint"
    upDamageSpecial = "upDamageSpecial"
    attackFunction = "attackFunction"
    commandcodeattackFunction = "commandcodeattackFunction"
    donotNobleCondMismatch = "donotNobleCondMismatch"
    donotSelectCommandcard = "donotSelectCommandcard"
    donotReplace = "donotReplace"
    shortenUserEquipSkill = "shortenUserEquipSkill"
    tdTypeChange = "tdTypeChange"
    overwriteClassRelation = "overwriteClassRelation"
    tdTypeChangeArts = "tdTypeChangeArts"
    tdTypeChangeBuster = "tdTypeChangeBuster"
    tdTypeChangeQuick = "tdTypeChangeQuick"
    commandattackBeforeFunction = "commandattackBeforeFunction"
    gutsFunction = "gutsFunction"
    upCriticalRateDamageTaken = "upCriticalRateDamageTaken"
    downCriticalRateDamageTaken = "downCriticalRateDamageTaken"
    upCriticalStarDamageTaken = "upCriticalStarDamageTaken"
    downCriticalStarDamageTaken = "downCriticalStarDamageTaken"
    skillRankUp = "skillRankUp"
    avoidanceIndividuality = "avoidanceIndividuality"
    changeCommandCardType = "changeCommandCardType"
    specialInvincible = "specialInvincible"


BUFF_TYPE_NAME: Dict[int, NiceBuffType] = {
    0: NiceBuffType.none,
    1: NiceBuffType.upCommandatk,
    2: NiceBuffType.upStarweight,
    3: NiceBuffType.upCriticalpoint,
    4: NiceBuffType.downCriticalpoint,
    5: NiceBuffType.regainNp,
    6: NiceBuffType.regainStar,
    7: NiceBuffType.regainHp,
    8: NiceBuffType.reduceHp,
    9: NiceBuffType.upAtk,
    10: NiceBuffType.downAtk,
    11: NiceBuffType.upDamage,
    12: NiceBuffType.downDamage,
    13: NiceBuffType.addDamage,
    14: NiceBuffType.subDamage,
    15: NiceBuffType.upNpdamage,
    16: NiceBuffType.downNpdamage,
    17: NiceBuffType.upDropnp,
    18: NiceBuffType.upCriticaldamage,
    19: NiceBuffType.downCriticaldamage,
    20: NiceBuffType.upSelfdamage,
    21: NiceBuffType.downSelfdamage,
    22: NiceBuffType.addSelfdamage,
    23: NiceBuffType.subSelfdamage,
    24: NiceBuffType.avoidance,
    25: NiceBuffType.breakAvoidance,
    26: NiceBuffType.invincible,
    27: NiceBuffType.upGrantstate,
    28: NiceBuffType.downGrantstate,
    29: NiceBuffType.upTolerance,
    30: NiceBuffType.downTolerance,
    31: NiceBuffType.avoidState,
    32: NiceBuffType.donotAct,
    33: NiceBuffType.donotSkill,
    34: NiceBuffType.donotNoble,
    35: NiceBuffType.donotRecovery,
    36: NiceBuffType.disableGender,
    37: NiceBuffType.guts,
    38: NiceBuffType.upHate,
    40: NiceBuffType.addIndividuality,
    41: NiceBuffType.subIndividuality,
    42: NiceBuffType.upDefence,
    43: NiceBuffType.downDefence,
    50: NiceBuffType.upCommandstar,
    51: NiceBuffType.upCommandnp,
    52: NiceBuffType.upCommandall,
    60: NiceBuffType.downCommandall,
    61: NiceBuffType.downStarweight,
    62: NiceBuffType.reduceNp,
    63: NiceBuffType.downDropnp,
    64: NiceBuffType.upGainHp,
    65: NiceBuffType.downGainHp,
    66: NiceBuffType.downCommandatk,
    67: NiceBuffType.downCommanstar,
    68: NiceBuffType.downCommandnp,
    70: NiceBuffType.upCriticalrate,
    71: NiceBuffType.downCriticalrate,
    72: NiceBuffType.pierceInvincible,
    73: NiceBuffType.avoidInstantdeath,
    74: NiceBuffType.upResistInstantdeath,
    75: NiceBuffType.upNonresistInstantdeath,
    76: NiceBuffType.delayFunction,
    77: NiceBuffType.regainNpUsedNoble,
    78: NiceBuffType.deadFunction,
    79: NiceBuffType.upMaxhp,
    80: NiceBuffType.downMaxhp,
    81: NiceBuffType.addMaxhp,
    82: NiceBuffType.subMaxhp,
    83: NiceBuffType.battlestartFunction,
    84: NiceBuffType.wavestartFunction,
    85: NiceBuffType.selfturnendFunction,
    87: NiceBuffType.upGivegainHp,
    88: NiceBuffType.downGivegainHp,
    89: NiceBuffType.commandattackFunction,
    90: NiceBuffType.deadattackFunction,
    91: NiceBuffType.upSpecialdefence,
    92: NiceBuffType.downSpecialdefence,
    93: NiceBuffType.upDamagedropnp,
    94: NiceBuffType.downDamagedropnp,
    95: NiceBuffType.entryFunction,
    96: NiceBuffType.upChagetd,
    97: NiceBuffType.reflectionFunction,
    98: NiceBuffType.upGrantSubstate,
    99: NiceBuffType.downGrantSubstate,
    100: NiceBuffType.upToleranceSubstate,
    101: NiceBuffType.downToleranceSubstate,
    102: NiceBuffType.upGrantInstantdeath,
    103: NiceBuffType.downGrantInstantdeath,
    104: NiceBuffType.gutsRatio,
    86: NiceBuffType.damageFunction,
    105: NiceBuffType.upDefencecommandall,
    106: NiceBuffType.downDefencecommandall,
    107: NiceBuffType.overwriteBattleclass,
    108: NiceBuffType.overwriteClassrelatioAtk,
    109: NiceBuffType.overwriteClassrelatioDef,
    110: NiceBuffType.upDamageIndividuality,
    111: NiceBuffType.downDamageIndividuality,
    112: NiceBuffType.upDamageIndividualityActiveonly,
    113: NiceBuffType.downDamageIndividualityActiveonly,
    114: NiceBuffType.upNpturnval,
    115: NiceBuffType.downNpturnval,
    116: NiceBuffType.multiattack,
    117: NiceBuffType.upGiveNp,
    118: NiceBuffType.downGiveNp,
    119: NiceBuffType.upResistanceDelayNpturn,
    120: NiceBuffType.downResistanceDelayNpturn,
    121: NiceBuffType.pierceDefence,
    122: NiceBuffType.upGutsHp,
    123: NiceBuffType.downGutsHp,
    124: NiceBuffType.upFuncgainNp,
    125: NiceBuffType.downFuncgainNp,
    126: NiceBuffType.upFuncHpReduce,
    127: NiceBuffType.downFuncHpReduce,
    128: NiceBuffType.upDefencecommanDamage,
    129: NiceBuffType.downDefencecommanDamage,
    130: NiceBuffType.npattackPrevBuff,
    131: NiceBuffType.fixCommandcard,
    132: NiceBuffType.donotGainnp,
    133: NiceBuffType.fieldIndividuality,
    134: NiceBuffType.donotActCommandtype,
    135: NiceBuffType.upDamageEventPoint,
    136: NiceBuffType.upDamageSpecial,
    137: NiceBuffType.attackFunction,
    138: NiceBuffType.commandcodeattackFunction,
    139: NiceBuffType.donotNobleCondMismatch,
    140: NiceBuffType.donotSelectCommandcard,
    141: NiceBuffType.donotReplace,
    142: NiceBuffType.shortenUserEquipSkill,
    143: NiceBuffType.tdTypeChange,
    144: NiceBuffType.overwriteClassRelation,
    145: NiceBuffType.tdTypeChangeArts,
    146: NiceBuffType.tdTypeChangeBuster,
    147: NiceBuffType.tdTypeChangeQuick,
    148: NiceBuffType.commandattackBeforeFunction,
    149: NiceBuffType.gutsFunction,
    150: NiceBuffType.upCriticalRateDamageTaken,
    151: NiceBuffType.downCriticalRateDamageTaken,
    152: NiceBuffType.upCriticalStarDamageTaken,
    153: NiceBuffType.downCriticalStarDamageTaken,
    154: NiceBuffType.skillRankUp,
    155: NiceBuffType.avoidanceIndividuality,
    156: NiceBuffType.changeCommandCardType,
    157: NiceBuffType.specialInvincible,
}


class BuffAction(IntEnum):
    NONE = 0
    COMMAND_ATK = 1
    COMMAND_DEF = 2
    ATK = 3
    DEFENCE = 4
    DEFENCE_PIERCE = 5
    SPECIALDEFENCE = 6
    DAMAGE = 7
    DAMAGE_INDIVIDUALITY = 8
    DAMAGE_INDIVIDUALITY_ACTIVEONLY = 9
    SELFDAMAGE = 10
    CRITICAL_DAMAGE = 11
    NPDAMAGE = 12
    GIVEN_DAMAGE = 13
    RECEIVE_DAMAGE = 14
    PIERCE_INVINCIBLE = 15
    INVINCIBLE = 16
    BREAK_AVOIDANCE = 17
    AVOIDANCE = 18
    OVERWRITE_BATTLECLASS = 19
    OVERWRITE_CLASSRELATIO_ATK = 20
    OVERWRITE_CLASSRELATIO_DEF = 21
    COMMAND_NP_ATK = 22
    COMMAND_NP_DEF = 23
    DROP_NP = 24
    DROP_NP_DAMAGE = 25
    COMMAND_STAR_ATK = 26
    COMMAND_STAR_DEF = 27
    CRITICAL_POINT = 28
    STARWEIGHT = 29
    TURNEND_NP = 30
    TURNEND_STAR = 31
    TURNEND_HP_REGAIN = 32
    TURNEND_HP_REDUCE = 33
    GAIN_HP = 34
    TURNVAL_NP = 35
    GRANT_STATE = 36
    RESISTANCE_STATE = 37
    AVOID_STATE = 38
    DONOT_ACT = 39
    DONOT_SKILL = 40
    DONOT_NOBLE = 41
    DONOT_RECOVERY = 42
    INDIVIDUALITY_ADD = 43
    INDIVIDUALITY_SUB = 44
    HATE = 45
    CRITICAL_RATE = 46
    AVOID_INSTANTDEATH = 47
    RESIST_INSTANTDEATH = 48
    NONRESIST_INSTANTDEATH = 49
    REGAIN_NP_USED_NOBLE = 50
    FUNCTION_DEAD = 51
    MAXHP_RATE = 52
    MAXHP_VALUE = 53
    FUNCTION_WAVESTART = 54
    FUNCTION_SELFTURNEND = 55
    GIVE_GAIN_HP = 56
    FUNCTION_COMMANDATTACK = 57
    FUNCTION_DEADATTACK = 58
    FUNCTION_ENTRY = 59
    CHAGETD = 60
    GRANT_SUBSTATE = 61
    TOLERANCE_SUBSTATE = 62
    GRANT_INSTANTDEATH = 63
    FUNCTION_DAMAGE = 64
    FUNCTION_REFLECTION = 65
    MULTIATTACK = 66
    GIVE_NP = 67
    RESISTANCE_DELAY_NPTURN = 68
    PIERCE_DEFENCE = 69
    GUTS_HP = 70
    FUNCGAIN_NP = 71
    FUNC_HP_REDUCE = 72
    FUNCTION_NPATTACK = 73
    FIX_COMMANDCARD = 74
    DONOT_GAINNP = 75
    FIELD_INDIVIDUALITY = 76
    DONOT_ACT_COMMANDTYPE = 77
    DAMAGE_EVENT_POINT = 78
    DAMAGE_SPECIAL = 79
    FUNCTION_ATTACK = 80
    FUNCTION_COMMANDCODEATTACK = 81
    DONOT_NOBLE_COND_MISMATCH = 82
    DONOT_SELECT_COMMANDCARD = 83
    DONOT_REPLACE = 84
    SHORTEN_USER_EQUIP_SKILL = 85
    TD_TYPE_CHANGE = 86
    OVERWRITE_CLASS_RELATION = 87
    FUNCTION_COMMANDATTACK_BEFORE = 88
    FUNCTION_GUTS = 89
    CRITICAL_RATE_DAMAGE_TAKEN = 90
    CRITICAL_STAR_DAMAGE_TAKEN = 91
    SKILL_RANK_CHANGE = 92
    AVOIDANCE_INDIVIDUALITY = 93
    CHANGE_COMMAND_CARD_TYPE = 94
    SPECIAL_INVINCIBLE = 95


class NiceBuffAction(str, Enum):
    none = "none"
    commandAtk = "commandAtk"
    commandDef = "commandDef"
    atk = "atk"
    defence = "defence"
    defencePierce = "defencePierce"
    specialdefence = "specialdefence"
    damage = "damage"
    damageIndividuality = "damageIndividuality"
    damageIndividualityActiveonly = "damageIndividualityActiveonly"
    selfdamage = "selfdamage"
    criticalDamage = "criticalDamage"
    npdamage = "npdamage"
    givenDamage = "givenDamage"
    receiveDamage = "receiveDamage"
    pierceInvincible = "pierceInvincible"
    invincible = "invincible"
    breakAvoidance = "breakAvoidance"
    avoidance = "avoidance"
    overwriteBattleclass = "overwriteBattleclass"
    overwriteClassrelatioAtk = "overwriteClassrelatioAtk"
    overwriteClassrelatioDef = "overwriteClassrelatioDef"
    commandNpAtk = "commandNpAtk"
    commandNpDef = "commandNpDef"
    dropNp = "dropNp"
    dropNpDamage = "dropNpDamage"
    commandStarAtk = "commandStarAtk"
    commandStarDef = "commandStarDef"
    criticalPoint = "criticalPoint"
    starweight = "starweight"
    turnendNp = "turnendNp"
    turnendStar = "turnendStar"
    turnendHpRegain = "turnendHpRegain"
    turnendHpReduce = "turnendHpReduce"
    gainHp = "gainHp"
    turnvalNp = "turnvalNp"
    grantState = "grantState"
    resistanceState = "resistanceState"
    avoidState = "avoidState"
    donotAct = "donotAct"
    donotSkill = "donotSkill"
    donotNoble = "donotNoble"
    donotRecovery = "donotRecovery"
    individualityAdd = "individualityAdd"
    individualitySub = "individualitySub"
    hate = "hate"
    criticalRate = "criticalRate"
    avoidInstantdeath = "avoidInstantdeath"
    resistInstantdeath = "resistInstantdeath"
    nonresistInstantdeath = "nonresistInstantdeath"
    regainNpUsedNoble = "regainNpUsedNoble"
    functionDead = "functionDead"
    maxhpRate = "maxhpRate"
    maxhpValue = "maxhpValue"
    functionWavestart = "functionWavestart"
    functionSelfturnend = "functionSelfturnend"
    giveGainHp = "giveGainHp"
    functionCommandattack = "functionCommandattack"
    functionDeadattack = "functionDeadattack"
    functionEntry = "functionEntry"
    chagetd = "chagetd"
    grantSubstate = "grantSubstate"
    toleranceSubstate = "toleranceSubstate"
    grantInstantdeath = "grantInstantdeath"
    functionDamage = "functionDamage"
    functionReflection = "functionReflection"
    multiattack = "multiattack"
    giveNp = "giveNp"
    resistanceDelayNpturn = "resistanceDelayNpturn"
    pierceDefence = "pierceDefence"
    gutsHp = "gutsHp"
    funcgainNp = "funcgainNp"
    funcHpReduce = "funcHpReduce"
    functionNpattack = "functionNpattack"
    fixCommandcard = "fixCommandcard"
    donotGainnp = "donotGainnp"
    fieldIndividuality = "fieldIndividuality"
    donotActCommandtype = "donotActCommandtype"
    damageEventPoint = "damageEventPoint"
    damageSpecial = "damageSpecial"
    functionAttack = "functionAttack"
    functionCommandcodeattack = "functionCommandcodeattack"
    donotNobleCondMismatch = "donotNobleCondMismatch"
    donotSelectCommandcard = "donotSelectCommandcard"
    donotReplace = "donotReplace"
    shortenUserEquipSkill = "shortenUserEquipSkill"
    tdTypeChange = "tdTypeChange"
    overwriteClassRelation = "overwriteClassRelation"
    functionCommandattackBefore = "functionCommandattackBefore"
    functionGuts = "functionGuts"
    criticalRateDamageTaken = "criticalRateDamageTaken"
    criticalStarDamageTaken = "criticalStarDamageTaken"
    skillRankChange = "skillRankChange"
    avoidanceIndividuality = "avoidanceIndividuality"
    changeCommandCardType = "changeCommandCardType"
    specialInvincible = "specialInvincible"


BUFF_ACTION_NAME: Dict[int, NiceBuffAction] = {
    0: NiceBuffAction.none,
    1: NiceBuffAction.commandAtk,
    2: NiceBuffAction.commandDef,
    3: NiceBuffAction.atk,
    4: NiceBuffAction.defence,
    5: NiceBuffAction.defencePierce,
    6: NiceBuffAction.specialdefence,
    7: NiceBuffAction.damage,
    8: NiceBuffAction.damageIndividuality,
    9: NiceBuffAction.damageIndividualityActiveonly,
    10: NiceBuffAction.selfdamage,
    11: NiceBuffAction.criticalDamage,
    12: NiceBuffAction.npdamage,
    13: NiceBuffAction.givenDamage,
    14: NiceBuffAction.receiveDamage,
    15: NiceBuffAction.pierceInvincible,
    16: NiceBuffAction.invincible,
    17: NiceBuffAction.breakAvoidance,
    18: NiceBuffAction.avoidance,
    19: NiceBuffAction.overwriteBattleclass,
    20: NiceBuffAction.overwriteClassrelatioAtk,
    21: NiceBuffAction.overwriteClassrelatioDef,
    22: NiceBuffAction.commandNpAtk,
    23: NiceBuffAction.commandNpDef,
    24: NiceBuffAction.dropNp,
    25: NiceBuffAction.dropNpDamage,
    26: NiceBuffAction.commandStarAtk,
    27: NiceBuffAction.commandStarDef,
    28: NiceBuffAction.criticalPoint,
    29: NiceBuffAction.starweight,
    30: NiceBuffAction.turnendNp,
    31: NiceBuffAction.turnendStar,
    32: NiceBuffAction.turnendHpRegain,
    33: NiceBuffAction.turnendHpReduce,
    34: NiceBuffAction.gainHp,
    35: NiceBuffAction.turnvalNp,
    36: NiceBuffAction.grantState,
    37: NiceBuffAction.resistanceState,
    38: NiceBuffAction.avoidState,
    39: NiceBuffAction.donotAct,
    40: NiceBuffAction.donotSkill,
    41: NiceBuffAction.donotNoble,
    42: NiceBuffAction.donotRecovery,
    43: NiceBuffAction.individualityAdd,
    44: NiceBuffAction.individualitySub,
    45: NiceBuffAction.hate,
    46: NiceBuffAction.criticalRate,
    47: NiceBuffAction.avoidInstantdeath,
    48: NiceBuffAction.resistInstantdeath,
    49: NiceBuffAction.nonresistInstantdeath,
    50: NiceBuffAction.regainNpUsedNoble,
    51: NiceBuffAction.functionDead,
    52: NiceBuffAction.maxhpRate,
    53: NiceBuffAction.maxhpValue,
    54: NiceBuffAction.functionWavestart,
    55: NiceBuffAction.functionSelfturnend,
    56: NiceBuffAction.giveGainHp,
    57: NiceBuffAction.functionCommandattack,
    58: NiceBuffAction.functionDeadattack,
    59: NiceBuffAction.functionEntry,
    60: NiceBuffAction.chagetd,
    61: NiceBuffAction.grantSubstate,
    62: NiceBuffAction.toleranceSubstate,
    63: NiceBuffAction.grantInstantdeath,
    64: NiceBuffAction.functionDamage,
    65: NiceBuffAction.functionReflection,
    66: NiceBuffAction.multiattack,
    67: NiceBuffAction.giveNp,
    68: NiceBuffAction.resistanceDelayNpturn,
    69: NiceBuffAction.pierceDefence,
    70: NiceBuffAction.gutsHp,
    71: NiceBuffAction.funcgainNp,
    72: NiceBuffAction.funcHpReduce,
    73: NiceBuffAction.functionNpattack,
    74: NiceBuffAction.fixCommandcard,
    75: NiceBuffAction.donotGainnp,
    76: NiceBuffAction.fieldIndividuality,
    77: NiceBuffAction.donotActCommandtype,
    78: NiceBuffAction.damageEventPoint,
    79: NiceBuffAction.damageSpecial,
    80: NiceBuffAction.functionAttack,
    81: NiceBuffAction.functionCommandcodeattack,
    82: NiceBuffAction.donotNobleCondMismatch,
    83: NiceBuffAction.donotSelectCommandcard,
    84: NiceBuffAction.donotReplace,
    85: NiceBuffAction.shortenUserEquipSkill,
    86: NiceBuffAction.tdTypeChange,
    87: NiceBuffAction.overwriteClassRelation,
    88: NiceBuffAction.functionCommandattackBefore,
    89: NiceBuffAction.functionGuts,
    90: NiceBuffAction.criticalRateDamageTaken,
    91: NiceBuffAction.criticalStarDamageTaken,
    92: NiceBuffAction.skillRankChange,
    93: NiceBuffAction.avoidanceIndividuality,
    94: NiceBuffAction.changeCommandCardType,
    95: NiceBuffAction.specialInvincible,
}


class DataValsType(IntEnum):
    Rate = 0
    Turn = 1
    Count = 2
    Value = 3
    Value2 = 4
    UseRate = 5
    Target = 6
    Correction = 7
    ParamAdd = 8
    ParamMax = 9
    HideMiss = 10
    OnField = 11
    HideNoEffect = 12
    Unaffected = 13
    ShowState = 14
    AuraEffectId = 15
    ActSet = 16
    ActSetWeight = 17
    ShowQuestNoEffect = 18
    CheckDead = 19
    RatioHPHigh = 20
    RatioHPLow = 21
    SetPassiveFrame = 22
    ProcPassive = 23
    ProcActive = 24
    HideParam = 25
    SkillID = 26
    SkillLV = 27
    ShowCardOnly = 28
    EffectSummon = 29
    RatioHPRangeHigh = 30
    RatioHPRangeLow = 31
    TargetList = 32
    OpponentOnly = 33
    StatusEffectId = 34
    EndBattle = 35
    LoseBattle = 36
    AddIndividualty = 37
    AddLinkageTargetIndividualty = 38
    SameBuffLimitTargetIndividuality = 39
    SameBuffLimitNum = 40
    CheckDuplicate = 41
    OnFieldCount = 42
    TargetRarityList = 43
    DependFuncId = 44
    DependFuncVals = 45
    InvalidHide = 46
    OutEnemyNpcId = 47
    InEnemyNpcId = 48
    OutEnemyPosition = 49
    IgnoreIndividuality = 50
    StarHigher = 51
    ChangeTDCommandType = 52
    ShiftNpcId = 53
    DisplayLastFuncInvalidType = 54
    AndCheckIndividualityList = 55
    WinBattleNotRelatedSurvivalStatus = 56
    ForceSelfInstantDeath = 57
    ChangeMaxBreakGauge = 58
    ParamAddMaxValue = 59
    ParamAddMaxCount = 60
    LossHpChangeDamage = 61
    IncludePassiveIndividuality = 62
    MotionChange = 63
    PopLabelDelay = 64


class ClassRelationOverwriteType(IntEnum):
    OVERWRITE_FORCE = 0
    OVERWRITE_MORE_THAN_TARGET = 1
    OVERWRITE_LESS_THAN_TARGET = 2


class NiceClassRelationOverwriteType(str, Enum):
    overwriteForce = "overwriteForce"
    overwriteMoreThanTarget = "overwriteMoreThanTarget"
    overwriteLessThanTarget = "overwriteLessThanTarget"


CLASS_OVERWRITE_NAME: Dict[int, NiceClassRelationOverwriteType] = {
    0: NiceClassRelationOverwriteType.overwriteForce,
    1: NiceClassRelationOverwriteType.overwriteMoreThanTarget,
    2: NiceClassRelationOverwriteType.overwriteLessThanTarget,
}


class ItemType(IntEnum):
    QP = 1
    STONE = 2
    AP_RECOVER = 3
    AP_ADD = 4
    MANA = 5
    KEY = 6
    GACHA_CLASS = 7
    GACHA_RELIC = 8
    GACHA_TICKET = 9
    LIMIT = 10
    SKILL_LV_UP = 11
    TD_LV_UP = 12
    FRIEND_POINT = 13
    EVENT_POINT = 14
    EVENT_ITEM = 15
    QUEST_REWARD_QP = 16
    CHARGE_STONE = 17
    RP_ADD = 18
    BOOST_ITEM = 19
    STONE_FRAGMENTS = 20
    ANONYMOUS = 21
    RARE_PRI = 22
    COSTUME_RELEASE = 23
    ITEM_SELECT = 24
    COMMAND_CARD_PRM_UP = 25
    DICE = 26


class NiceItemType(str, Enum):
    qp = "qp"
    stone = "stone"
    apRecover = "apRecover"
    apAdd = "apAdd"
    mana = "mana"
    key = "key"
    gachaClass = "gachaClass"
    gachaRelic = "gachaRelic"
    gachaTicket = "gachaTicket"
    limit = "limit"
    skillLvUp = "skillLvUp"
    tdLvUp = "tdLvUp"
    friendPoint = "friendPoint"
    eventPoint = "eventPoint"
    eventItem = "eventItem"
    questRewardQp = "questRewardQp"
    chargeStone = "chargeStone"
    rpAdd = "rpAdd"
    boostItem = "boostItem"
    stoneFragments = "stoneFragments"
    anonymous = "anonymous"
    rarePri = "rarePri"
    costumeRelease = "costumeRelease"
    itemSelect = "itemSelect"
    commandCardPrmUp = "commandCardPrmUp"
    dice = "dice"


ITEM_TYPE_NAME: Dict[int, NiceItemType] = {
    1: NiceItemType.qp,
    2: NiceItemType.stone,
    3: NiceItemType.apRecover,
    4: NiceItemType.apAdd,
    5: NiceItemType.mana,
    6: NiceItemType.key,
    7: NiceItemType.gachaClass,
    8: NiceItemType.gachaRelic,
    9: NiceItemType.gachaTicket,
    10: NiceItemType.limit,
    11: NiceItemType.skillLvUp,
    12: NiceItemType.tdLvUp,
    13: NiceItemType.friendPoint,
    14: NiceItemType.eventPoint,
    15: NiceItemType.eventItem,
    16: NiceItemType.questRewardQp,
    17: NiceItemType.chargeStone,
    18: NiceItemType.rpAdd,
    19: NiceItemType.boostItem,
    20: NiceItemType.stoneFragments,
    21: NiceItemType.anonymous,
    22: NiceItemType.rarePri,
    23: NiceItemType.costumeRelease,
    24: NiceItemType.itemSelect,
    25: NiceItemType.commandCardPrmUp,
    26: NiceItemType.dice,
}


class CardType(IntEnum):
    NONE = 0
    ARTS = 1
    BUSTER = 2
    QUICK = 3
    ADDATTACK = 4
    BLANK = 5
    WEAK = 10
    STRENGTH = 11


class NiceCardType(str, Enum):
    none = "none"
    arts = "arts"
    buster = "buster"
    quick = "quick"
    addattack = "extra"
    blank = "blank"
    weak = "weak"
    strength = "strength"


CARD_TYPE_NAME: Dict[int, NiceCardType] = {
    0: NiceCardType.none,
    1: NiceCardType.arts,
    2: NiceCardType.buster,
    3: NiceCardType.quick,
    4: NiceCardType.addattack,
    5: NiceCardType.blank,
    10: NiceCardType.weak,
    11: NiceCardType.strength,
}


class CondType(IntEnum):
    NONE = 0
    QUEST_CLEAR = 1
    ITEM_GET = 2
    USE_ITEM_ETERNITY = 3
    USE_ITEM_TIME = 4
    USE_ITEM_COUNT = 5
    SVT_LEVEL = 6
    SVT_LIMIT = 7
    SVT_GET = 8
    SVT_FRIENDSHIP = 9
    SVT_GROUP = 10
    EVENT = 11
    DATE = 12
    WEEKDAY = 13
    PURCHASE_QP_SHOP = 14
    PURCHASE_STONE_SHOP = 15
    WAR_CLEAR = 16
    FLAG = 17
    SVT_COUNT_STOP = 18
    BIRTH_DAY = 19
    EVENT_END = 20
    SVT_EVENT_JOIN = 21
    MISSION_CONDITION_DETAIL = 22
    EVENT_MISSION_CLEAR = 23
    EVENT_MISSION_ACHIEVE = 24
    QUEST_CLEAR_NUM = 25
    NOT_QUEST_GROUP_CLEAR = 26
    RAID_ALIVE = 27
    RAID_DEAD = 28
    RAID_DAMAGE = 29
    QUEST_CHALLENGE_NUM = 30
    MASTER_MISSION = 31
    QUEST_GROUP_CLEAR = 32
    SUPER_BOSS_DAMAGE = 33
    SUPER_BOSS_DAMAGE_ALL = 34
    PURCHASE_SHOP = 35
    QUEST_NOT_CLEAR = 36
    NOT_SHOP_PURCHASE = 37
    NOT_SVT_GET = 38
    NOT_EVENT_SHOP_PURCHASE = 39
    SVT_HAVING = 40
    NOT_SVT_HAVING = 41
    QUEST_CHALLENGE_NUM_EQUAL = 42
    QUEST_CHALLENGE_NUM_BELOW = 43
    QUEST_CLEAR_NUM_EQUAL = 44
    QUEST_CLEAR_NUM_BELOW = 45
    QUEST_CLEAR_PHASE = 46
    NOT_QUEST_CLEAR_PHASE = 47
    EVENT_POINT_GROUP_WIN = 48
    EVENT_NORMA_POINT_CLEAR = 49
    QUEST_AVAILABLE = 50
    QUEST_GROUP_AVAILABLE_NUM = 51
    EVENT_NORMA_POINT_NOT_CLEAR = 52
    NOT_ITEM_GET = 53
    COSTUME_GET = 54
    QUEST_RESET_AVAILABLE = 55
    SVT_GET_BEFORE_EVENT_END = 56
    QUEST_CLEAR_RAW = 57
    QUEST_GROUP_CLEAR_RAW = 58
    EVENT_GROUP_POINT_RATIO_IN_TERM = 59
    EVENT_GROUP_RANK_IN_TERM = 60
    NOT_EVENT_RACE_QUEST_OR_NOT_ALL_GROUP_GOAL = 61
    EVENT_GROUP_TOTAL_WIN_EACH_PLAYER = 62
    EVENT_SCRIPT_PLAY = 63
    SVT_COSTUME_RELEASED = 64
    QUEST_NOT_CLEAR_AND = 65
    SVT_RECOVERD = 66
    SHOP_RELEASED = 67
    EVENT_POINT = 68
    EVENT_REWARD_DISP_COUNT = 69
    EQUIP_WITH_TARGET_COSTUME = 70
    RAID_GROUP_DEAD = 71
    NOT_SVT_GROUP = 72
    NOT_QUEST_RESET_AVAILABLE = 73
    NOT_QUEST_CLEAR_RAW = 74
    NOT_QUEST_GROUP_CLEAR_RAW = 75
    NOT_EVENT_MISSION_CLEAR = 76
    NOT_EVENT_MISSION_ACHIEVE = 77
    NOT_COSTUME_GET = 78
    NOT_SVT_COSTUME_RELEASED = 79
    NOT_EVENT_RACE_QUEST_OR_NOT_TARGET_RANK_GOAL = 80
    PLAYER_GENDER_TYPE = 81
    SHOP_GROUP_LIMIT_NUM = 82
    EVENT_GROUP_POINT = 83
    EVENT_GROUP_POINT_BELOW = 84
    EVENT_TOTAL_POINT = 85
    EVENT_TOTAL_POINT_BELOW = 86
    EVENT_VALUE = 87
    EVENT_VALUE_BELOW = 88
    EVENT_FLAG = 89
    EVENT_STATUS = 90
    NOT_EVENT_STATUS = 91
    FORCE_FALSE = 92
    SVT_HAVING_LIMIT_MAX = 93
    EVENT_POINT_BELOW = 94
    SVT_EQUIP_FRIENDSHIP_HAVING = 95
    MOVIE_NOT_DOWNLOAD = 96
    MULTIPLE_DATE = 97
    SVT_FRIENDSHIP_ABOVE = 98
    SVT_FRIENDSHIP_BELOW = 99
    MOVIE_DOWNLOADED = 100
    ROUTE_SELECT = 101
    NOT_ROUTE_SELECT = 102
    LIMIT_COUNT = 103
    LIMIT_COUNT_ABOVE = 104
    LIMIT_COUNT_BELOW = 105
    BAD_END_PLAY = 106
    COMMAND_CODE_GET = 107
    NOT_COMMAND_CODE_GET = 108
    ALL_USERS_BOX_GACHA_COUNT = 109
    TOTAL_TD_LEVEL = 110
    TOTAL_TD_LEVEL_ABOVE = 111
    TOTAL_TD_LEVEL_BELOW = 112
    COMMON_RELEASE = 113
    BATTLE_RESULT_WIN = 114
    BATTLE_RESULT_LOSE = 115
    EVENT_VALUE_EQUAL = 116
    BOARD_GAME_TOKEN_HAVING = 117
    BOARD_GAME_TOKEN_GROUP_HAVING = 118
    EVENT_FLAG_ON = 119
    EVENT_FLAG_OFF = 120
    QUEST_STATUS_FLAG_ON = 121
    QUEST_STATUS_FLAG_OFF = 122
    EVENT_VALUE_NOT_EQUAL = 123
    LIMIT_COUNT_MAX_EQUAL = 124
    LIMIT_COUNT_MAX_ABOVE = 125
    LIMIT_COUNT_MAX_BELOW = 126
    BOARD_GAME_TOKEN_GET_NUM = 127
    BATTLE_LINE_WIN_ABOVE = 128
    BATTLE_LINE_LOSE_ABOVE = 129
    BATTLE_LINE_CONTINUE_WIN = 130
    BATTLE_LINE_CONTINUE_LOSE = 131
    BATTLE_LINE_CONTINUE_WIN_BELOW = 132
    BATTLE_LINE_CONTINUE_LOSE_BELOW = 133
    BATTLE_GROUP_WIN_AVOVE = 134
    BATTLE_GROUP_LOSE_AVOVE = 135


class NiceCondType(str, Enum):
    none = "none"
    questClear = "questClear"
    itemGet = "itemGet"
    useItemEternity = "useItemEternity"
    useItemTime = "useItemTime"
    useItemCount = "useItemCount"
    svtLevel = "svtLevel"
    svtLimit = "svtLimit"
    svtGet = "svtGet"
    svtFriendship = "svtFriendship"
    svtGroup = "svtGroup"
    event = "event"
    date = "date"
    weekday = "weekday"
    purchaseQpShop = "purchaseQpShop"
    purchaseStoneShop = "purchaseStoneShop"
    warClear = "warClear"
    flag = "flag"
    svtCountStop = "svtCountStop"
    birthDay = "birthDay"
    eventEnd = "eventEnd"
    svtEventJoin = "svtEventJoin"
    missionConditionDetail = "missionConditionDetail"
    eventMissionClear = "eventMissionClear"
    eventMissionAchieve = "eventMissionAchieve"
    questClearNum = "questClearNum"
    notQuestGroupClear = "notQuestGroupClear"
    raidAlive = "raidAlive"
    raidDead = "raidDead"
    raidDamage = "raidDamage"
    questChallengeNum = "questChallengeNum"
    masterMission = "masterMission"
    questGroupClear = "questGroupClear"
    superBossDamage = "superBossDamage"
    superBossDamageAll = "superBossDamageAll"
    purchaseShop = "purchaseShop"
    questNotClear = "questNotClear"
    notShopPurchase = "notShopPurchase"
    notSvtGet = "notSvtGet"
    notEventShopPurchase = "notEventShopPurchase"
    svtHaving = "svtHaving"
    notSvtHaving = "notSvtHaving"
    questChallengeNumEqual = "questChallengeNumEqual"
    questChallengeNumBelow = "questChallengeNumBelow"
    questClearNumEqual = "questClearNumEqual"
    questClearNumBelow = "questClearNumBelow"
    questClearPhase = "questClearPhase"
    notQuestClearPhase = "notQuestClearPhase"
    eventPointGroupWin = "eventPointGroupWin"
    eventNormaPointClear = "eventNormaPointClear"
    questAvailable = "questAvailable"
    questGroupAvailableNum = "questGroupAvailableNum"
    eventNormaPointNotClear = "eventNormaPointNotClear"
    notItemGet = "notItemGet"
    costumeGet = "costumeGet"
    questResetAvailable = "questResetAvailable"
    svtGetBeforeEventEnd = "svtGetBeforeEventEnd"
    questClearRaw = "questClearRaw"
    questGroupClearRaw = "questGroupClearRaw"
    eventGroupPointRatioInTerm = "eventGroupPointRatioInTerm"
    eventGroupRankInTerm = "eventGroupRankInTerm"
    notEventRaceQuestOrNotAllGroupGoal = "notEventRaceQuestOrNotAllGroupGoal"
    eventGroupTotalWinEachPlayer = "eventGroupTotalWinEachPlayer"
    eventScriptPlay = "eventScriptPlay"
    svtCostumeReleased = "svtCostumeReleased"
    questNotClearAnd = "questNotClearAnd"
    svtRecoverd = "svtRecoverd"
    shopReleased = "shopReleased"
    eventPoint = "eventPoint"
    eventRewardDispCount = "eventRewardDispCount"
    equipWithTargetCostume = "equipWithTargetCostume"
    raidGroupDead = "raidGroupDead"
    notSvtGroup = "notSvtGroup"
    notQuestResetAvailable = "notQuestResetAvailable"
    notQuestClearRaw = "notQuestClearRaw"
    notQuestGroupClearRaw = "notQuestGroupClearRaw"
    notEventMissionClear = "notEventMissionClear"
    notEventMissionAchieve = "notEventMissionAchieve"
    notCostumeGet = "notCostumeGet"
    notSvtCostumeReleased = "notSvtCostumeReleased"
    notEventRaceQuestOrNotTargetRankGoal = "notEventRaceQuestOrNotTargetRankGoal"
    playerGenderType = "playerGenderType"
    shopGroupLimitNum = "shopGroupLimitNum"
    eventGroupPoint = "eventGroupPoint"
    eventGroupPointBelow = "eventGroupPointBelow"
    eventTotalPoint = "eventTotalPoint"
    eventTotalPointBelow = "eventTotalPointBelow"
    eventValue = "eventValue"
    eventValueBelow = "eventValueBelow"
    eventFlag = "eventFlag"
    eventStatus = "eventStatus"
    notEventStatus = "notEventStatus"
    forceFalse = "forceFalse"
    svtHavingLimitMax = "svtHavingLimitMax"
    eventPointBelow = "eventPointBelow"
    svtEquipFriendshipHaving = "svtEquipFriendshipHaving"
    movieNotDownload = "movieNotDownload"
    multipleDate = "multipleDate"
    svtFriendshipAbove = "svtFriendshipAbove"
    svtFriendshipBelow = "svtFriendshipBelow"
    movieDownloaded = "movieDownloaded"
    routeSelect = "routeSelect"
    notRouteSelect = "notRouteSelect"
    limitCount = "limitCount"
    limitCountAbove = "limitCountAbove"
    limitCountBelow = "limitCountBelow"
    badEndPlay = "badEndPlay"
    commandCodeGet = "commandCodeGet"
    notCommandCodeGet = "notCommandCodeGet"
    allUsersBoxGachaCount = "allUsersBoxGachaCount"
    totalTdLevel = "totalTdLevel"
    totalTdLevelAbove = "totalTdLevelAbove"
    totalTdLevelBelow = "totalTdLevelBelow"
    commonRelease = "commonRelease"
    battleResultWin = "battleResultWin"
    battleResultLose = "battleResultLose"
    eventValueEqual = "eventValueEqual"
    boardGameTokenHaving = "boardGameTokenHaving"
    boardGameTokenGroupHaving = "boardGameTokenGroupHaving"
    eventFlagOn = "eventFlagOn"
    eventFlagOff = "eventFlagOff"
    questStatusFlagOn = "questStatusFlagOn"
    questStatusFlagOff = "questStatusFlagOff"
    eventValueNotEqual = "eventValueNotEqual"
    limitCountMaxEqual = "limitCountMaxEqual"
    limitCountMaxAbove = "limitCountMaxAbove"
    limitCountMaxBelow = "limitCountMaxBelow"
    boardGameTokenGetNum = "boardGameTokenGetNum"
    battleLineWinAbove = "battleLineWinAbove"
    battleLineLoseAbove = "battleLineLoseAbove"
    battleLineContinueWin = "battleLineContinueWin"
    battleLineContinueLose = "battleLineContinueLose"
    battleLineContinueWinBelow = "battleLineContinueWinBelow"
    battleLineContinueLoseBelow = "battleLineContinueLoseBelow"
    battleGroupWinAvove = "battleGroupWinAvove"
    battleGroupLoseAvove = "battleGroupLoseAvove"


COND_TYPE_NAME: Dict[int, NiceCondType] = {
    0: NiceCondType.none,
    1: NiceCondType.questClear,
    2: NiceCondType.itemGet,
    3: NiceCondType.useItemEternity,
    4: NiceCondType.useItemTime,
    5: NiceCondType.useItemCount,
    6: NiceCondType.svtLevel,
    7: NiceCondType.svtLimit,
    8: NiceCondType.svtGet,
    9: NiceCondType.svtFriendship,
    10: NiceCondType.svtGroup,
    11: NiceCondType.event,
    12: NiceCondType.date,
    13: NiceCondType.weekday,
    14: NiceCondType.purchaseQpShop,
    15: NiceCondType.purchaseStoneShop,
    16: NiceCondType.warClear,
    17: NiceCondType.flag,
    18: NiceCondType.svtCountStop,
    19: NiceCondType.birthDay,
    20: NiceCondType.eventEnd,
    21: NiceCondType.svtEventJoin,
    22: NiceCondType.missionConditionDetail,
    23: NiceCondType.eventMissionClear,
    24: NiceCondType.eventMissionAchieve,
    25: NiceCondType.questClearNum,
    26: NiceCondType.notQuestGroupClear,
    27: NiceCondType.raidAlive,
    28: NiceCondType.raidDead,
    29: NiceCondType.raidDamage,
    30: NiceCondType.questChallengeNum,
    31: NiceCondType.masterMission,
    32: NiceCondType.questGroupClear,
    33: NiceCondType.superBossDamage,
    34: NiceCondType.superBossDamageAll,
    35: NiceCondType.purchaseShop,
    36: NiceCondType.questNotClear,
    37: NiceCondType.notShopPurchase,
    38: NiceCondType.notSvtGet,
    39: NiceCondType.notEventShopPurchase,
    40: NiceCondType.svtHaving,
    41: NiceCondType.notSvtHaving,
    42: NiceCondType.questChallengeNumEqual,
    43: NiceCondType.questChallengeNumBelow,
    44: NiceCondType.questClearNumEqual,
    45: NiceCondType.questClearNumBelow,
    46: NiceCondType.questClearPhase,
    47: NiceCondType.notQuestClearPhase,
    48: NiceCondType.eventPointGroupWin,
    49: NiceCondType.eventNormaPointClear,
    50: NiceCondType.questAvailable,
    51: NiceCondType.questGroupAvailableNum,
    52: NiceCondType.eventNormaPointNotClear,
    53: NiceCondType.notItemGet,
    54: NiceCondType.costumeGet,
    55: NiceCondType.questResetAvailable,
    56: NiceCondType.svtGetBeforeEventEnd,
    57: NiceCondType.questClearRaw,
    58: NiceCondType.questGroupClearRaw,
    59: NiceCondType.eventGroupPointRatioInTerm,
    60: NiceCondType.eventGroupRankInTerm,
    61: NiceCondType.notEventRaceQuestOrNotAllGroupGoal,
    62: NiceCondType.eventGroupTotalWinEachPlayer,
    63: NiceCondType.eventScriptPlay,
    64: NiceCondType.svtCostumeReleased,
    65: NiceCondType.questNotClearAnd,
    66: NiceCondType.svtRecoverd,
    67: NiceCondType.shopReleased,
    68: NiceCondType.eventPoint,
    69: NiceCondType.eventRewardDispCount,
    70: NiceCondType.equipWithTargetCostume,
    71: NiceCondType.raidGroupDead,
    72: NiceCondType.notSvtGroup,
    73: NiceCondType.notQuestResetAvailable,
    74: NiceCondType.notQuestClearRaw,
    75: NiceCondType.notQuestGroupClearRaw,
    76: NiceCondType.notEventMissionClear,
    77: NiceCondType.notEventMissionAchieve,
    78: NiceCondType.notCostumeGet,
    79: NiceCondType.notSvtCostumeReleased,
    80: NiceCondType.notEventRaceQuestOrNotTargetRankGoal,
    81: NiceCondType.playerGenderType,
    82: NiceCondType.shopGroupLimitNum,
    83: NiceCondType.eventGroupPoint,
    84: NiceCondType.eventGroupPointBelow,
    85: NiceCondType.eventTotalPoint,
    86: NiceCondType.eventTotalPointBelow,
    87: NiceCondType.eventValue,
    88: NiceCondType.eventValueBelow,
    89: NiceCondType.eventFlag,
    90: NiceCondType.eventStatus,
    91: NiceCondType.notEventStatus,
    92: NiceCondType.forceFalse,
    93: NiceCondType.svtHavingLimitMax,
    94: NiceCondType.eventPointBelow,
    95: NiceCondType.svtEquipFriendshipHaving,
    96: NiceCondType.movieNotDownload,
    97: NiceCondType.multipleDate,
    98: NiceCondType.svtFriendshipAbove,
    99: NiceCondType.svtFriendshipBelow,
    100: NiceCondType.movieDownloaded,
    101: NiceCondType.routeSelect,
    102: NiceCondType.notRouteSelect,
    103: NiceCondType.limitCount,
    104: NiceCondType.limitCountAbove,
    105: NiceCondType.limitCountBelow,
    106: NiceCondType.badEndPlay,
    107: NiceCondType.commandCodeGet,
    108: NiceCondType.notCommandCodeGet,
    109: NiceCondType.allUsersBoxGachaCount,
    110: NiceCondType.totalTdLevel,
    111: NiceCondType.totalTdLevelAbove,
    112: NiceCondType.totalTdLevelBelow,
    113: NiceCondType.commonRelease,
    114: NiceCondType.battleResultWin,
    115: NiceCondType.battleResultLose,
    116: NiceCondType.eventValueEqual,
    117: NiceCondType.boardGameTokenHaving,
    118: NiceCondType.boardGameTokenGroupHaving,
    119: NiceCondType.eventFlagOn,
    120: NiceCondType.eventFlagOff,
    121: NiceCondType.questStatusFlagOn,
    122: NiceCondType.questStatusFlagOff,
    123: NiceCondType.eventValueNotEqual,
    124: NiceCondType.limitCountMaxEqual,
    125: NiceCondType.limitCountMaxAbove,
    126: NiceCondType.limitCountMaxBelow,
    127: NiceCondType.boardGameTokenGetNum,
    128: NiceCondType.battleLineWinAbove,
    129: NiceCondType.battleLineLoseAbove,
    130: NiceCondType.battleLineContinueWin,
    131: NiceCondType.battleLineContinueLose,
    132: NiceCondType.battleLineContinueWinBelow,
    133: NiceCondType.battleLineContinueLoseBelow,
    134: NiceCondType.battleGroupWinAvove,
    135: NiceCondType.battleGroupLoseAvove,
}


class VoiceCondType(IntEnum):
    BIRTH_DAY = 1
    EVENT = 2
    FRIENDSHIP = 3
    SVT_GET = 4
    SVT_GROUP = 5
    QUEST_CLEAR = 6
    NOT_QUEST_CLEAR = 7
    LEVEL_UP = 8
    LIMIT_COUNT = 9
    LIMIT_COUNT_COMMON = 10
    COUNT_STOP = 11
    ISNEW_WAR = 12
    EVENT_END = 13
    EVENT_NOEND = 14
    EVENT_MISSION_ACTION = 15
    MASTER_MISSION = 16
    LIMIT_COUNT_ABOVE = 17
    EVENT_SHOP_PURCHASE = 18
    EVENT_PERIOD = 19
    FRIENDSHIP_ABOVE = 20
    SPACIFIC_SHOP_PURCHASE = 21
    FRIENDSHIP_BELOW = 22
    COSTUME = 23
    LEVEL_UP_LIMIT_COUNT = 24
    LEVEL_UP_LIMIT_COUNT_ABOVE = 25
    LEVEL_UP_LIMIT_COUNT_BELOW = 26


class NiceVoiceCondType(str, Enum):
    birthDay = "birthDay"
    event = "event"
    friendship = "friendship"
    svtGet = "svtGet"
    svtGroup = "svtGroup"
    questClear = "questClear"
    notQuestClear = "notQuestClear"
    levelUp = "levelUp"
    limitCount = "limitCount"
    limitCountCommon = "limitCountCommon"
    countStop = "countStop"
    isnewWar = "isnewWar"
    eventEnd = "eventEnd"
    eventNoend = "eventNoend"
    eventMissionAction = "eventMissionAction"
    masterMission = "masterMission"
    limitCountAbove = "limitCountAbove"
    eventShopPurchase = "eventShopPurchase"
    eventPeriod = "eventPeriod"
    friendshipAbove = "friendshipAbove"
    spacificShopPurchase = "spacificShopPurchase"
    friendshipBelow = "friendshipBelow"
    costume = "costume"
    levelUpLimitCount = "levelUpLimitCount"
    levelUpLimitCountAbove = "levelUpLimitCountAbove"
    levelUpLimitCountBelow = "levelUpLimitCountBelow"


VOICE_COND_NAME: Dict[int, NiceVoiceCondType] = {
    1: NiceVoiceCondType.birthDay,
    2: NiceVoiceCondType.event,
    3: NiceVoiceCondType.friendship,
    4: NiceVoiceCondType.svtGet,
    5: NiceVoiceCondType.svtGroup,
    6: NiceVoiceCondType.questClear,
    7: NiceVoiceCondType.notQuestClear,
    8: NiceVoiceCondType.levelUp,
    9: NiceVoiceCondType.limitCount,
    10: NiceVoiceCondType.limitCountCommon,
    11: NiceVoiceCondType.countStop,
    12: NiceVoiceCondType.isnewWar,
    13: NiceVoiceCondType.eventEnd,
    14: NiceVoiceCondType.eventNoend,
    15: NiceVoiceCondType.eventMissionAction,
    16: NiceVoiceCondType.masterMission,
    17: NiceVoiceCondType.limitCountAbove,
    18: NiceVoiceCondType.eventShopPurchase,
    19: NiceVoiceCondType.eventPeriod,
    20: NiceVoiceCondType.friendshipAbove,
    21: NiceVoiceCondType.spacificShopPurchase,
    22: NiceVoiceCondType.friendshipBelow,
    23: NiceVoiceCondType.costume,
    24: NiceVoiceCondType.levelUpLimitCount,
    25: NiceVoiceCondType.levelUpLimitCountAbove,
    26: NiceVoiceCondType.levelUpLimitCountBelow,
}


class SvtVoiceType(IntEnum):
    HOME = 1
    GROETH = 2
    FIRST_GET = 3
    EVENT_JOIN = 4
    EVENT_REWARD = 5
    BATTLE = 6
    TREASURE_DEVICE = 7
    MASTER_MISSION = 8
    EVENT_SHOP = 9
    HOME_COSTUME = 10
    BOX_GACHA_TALK = 11
    BATTLE_ENTRY = 12
    BATTLE_WIN = 13
    EVENT_TOWER_REWARD = 14
    GUIDE = 15
    EVENT_DAILY_POINT = 16
    TDDAMAGE = 17
    SUM = 18


class NiceSvtVoiceType(str, Enum):
    home = "home"
    groeth = "groeth"
    firstGet = "firstGet"
    eventJoin = "eventJoin"
    eventReward = "eventReward"
    battle = "battle"
    treasureDevice = "treasureDevice"
    masterMission = "masterMission"
    eventShop = "eventShop"
    homeCostume = "homeCostume"
    boxGachaTalk = "boxGachaTalk"
    battleEntry = "battleEntry"
    battleWin = "battleWin"
    eventTowerReward = "eventTowerReward"
    guide = "guide"
    eventDailyPoint = "eventDailyPoint"
    tddamage = "tddamage"
    sum = "sum"


VOICE_TYPE_NAME: Dict[int, NiceSvtVoiceType] = {
    1: NiceSvtVoiceType.home,
    2: NiceSvtVoiceType.groeth,
    3: NiceSvtVoiceType.firstGet,
    4: NiceSvtVoiceType.eventJoin,
    5: NiceSvtVoiceType.eventReward,
    6: NiceSvtVoiceType.battle,
    7: NiceSvtVoiceType.treasureDevice,
    8: NiceSvtVoiceType.masterMission,
    9: NiceSvtVoiceType.eventShop,
    10: NiceSvtVoiceType.homeCostume,
    11: NiceSvtVoiceType.boxGachaTalk,
    12: NiceSvtVoiceType.battleEntry,
    13: NiceSvtVoiceType.battleWin,
    14: NiceSvtVoiceType.eventTowerReward,
    15: NiceSvtVoiceType.guide,
    16: NiceSvtVoiceType.eventDailyPoint,
    17: NiceSvtVoiceType.tddamage,
    18: NiceSvtVoiceType.sum,
}


class QuestType(IntEnum):
    MAIN = 1
    FREE = 2
    FRIENDSHIP = 3
    EVENT = 5
    HEROBALLAD = 6


class NiceQuestType(str, Enum):
    main = "main"
    free = "free"
    friendship = "friendship"
    event = "event"
    heroballad = "heroballad"


QUEST_TYPE_NAME: Dict[int, NiceQuestType] = {
    1: NiceQuestType.main,
    2: NiceQuestType.free,
    3: NiceQuestType.friendship,
    5: NiceQuestType.event,
    6: NiceQuestType.heroballad,
}


class QuestConsumeType(IntEnum):
    NONE = 0
    AP = 1
    RP = 2
    ITEM = 3
    AP_ADD_ITEM = 4


class NiceConsumeType(str, Enum):
    none = "none"
    ap = "ap"
    rp = "rp"
    item = "item"
    apAddItem = "apAddItem"


QUEST_CONSUME_TYPE_NAME: Dict[int, NiceConsumeType] = {
    0: NiceConsumeType.none,
    1: NiceConsumeType.ap,
    2: NiceConsumeType.rp,
    3: NiceConsumeType.item,
    4: NiceConsumeType.apAddItem,
}
