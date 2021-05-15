from enum import Enum, IntEnum

from .gameenums import (
    AI_ACT_NUM_NAME,
    AI_ACT_TARGET_NAME,
    AI_ACT_TYPE_NAME,
    AI_COND_NAME,
    BUFF_ACTION_NAME,
    BUFF_LIMIT_NAME,
    BUFF_TYPE_NAME,
    CARD_TYPE_NAME,
    CLASS_OVERWRITE_NAME,
    COND_TYPE_NAME,
    EVENT_LOTTERY_FLAG_NAME,
    EVENT_TYPE_NAME,
    FUNC_TARGETTYPE_NAME,
    FUNC_TYPE_NAME,
    GENDER_TYPE_NAME,
    GIFT_TYPE_NAME,
    ITEM_TYPE_NAME,
    MISSION_PROGRESS_TYPE_NAME,
    MISSION_REWARD_TYPE_NAME,
    MISSION_TYPE_NAME,
    PAY_TYPE_NAME,
    PURCHASE_TYPE_NAME,
    QUEST_CONSUME_TYPE_NAME,
    QUEST_TYPE_NAME,
    SHOP_TYPE_NAME,
    STATUS_RANK_NAME,
    SVT_FLAG_NAME,
    SVT_TYPE_NAME,
    VOICE_COND_NAME,
    VOICE_TYPE_NAME,
    WAR_OVERWRITE_TYPE_NAME,
    WAR_START_TYPE_NAME,
    FuncType,
    NiceBuffType,
    NiceCardType,
    NiceFuncTargetType,
    NiceFuncType,
    NiceGender,
    NiceSvtFlag,
    NiceSvtType,
)


### Servant Type ###


SVT_TYPE_NAME_REVERSE: dict[NiceSvtType, int] = {v: k for k, v in SVT_TYPE_NAME.items()}


### Servant Flag ###


SVT_FLAG_NAME_REVERSE: dict[NiceSvtFlag, int] = {v: k for k, v in SVT_FLAG_NAME.items()}


### Item Use Type ###


class NiceItemUse(str, Enum):
    """Item Use Enum"""

    skill = "skill"
    ascension = "ascension"
    costume = "costume"


### Skill Type ###


class NiceSkillType(str, Enum):
    """Skill Type Enum"""

    active = "active"
    passive = "passive"


SKILL_TYPE_NAME: dict[int, NiceSkillType] = {
    1: NiceSkillType.active,
    2: NiceSkillType.passive,
}


SKILL_TYPE_NAME_REVERSE: dict[NiceSkillType, int] = {
    v: k for k, v in SKILL_TYPE_NAME.items()
}


### Function Type ###

# The vals attribute of these func types are not buff IDs.
FUNC_VALS_NOT_BUFF = {
    FuncType.SUB_STATE,
    FuncType.EVENT_DROP_UP,
    FuncType.GAIN_NP_BUFF_INDIVIDUAL_SUM,
}


FUNC_TYPE_NAME_REVERSE: dict[NiceFuncType, int] = {
    v: k for k, v in FUNC_TYPE_NAME.items()
}


### Func Apply Target ###


class FuncApplyTarget(str, Enum):
    """Function Target Team Enum"""

    player = "player"
    enemy = "enemy"
    playerAndEnemy = "playerAndEnemy"


FUNC_APPLYTARGET_NAME: dict[int, FuncApplyTarget] = {
    1: FuncApplyTarget.player,
    2: FuncApplyTarget.enemy,
    3: FuncApplyTarget.playerAndEnemy,
}


FUNC_APPLYTARGET_NAME_REVERSE: dict[FuncApplyTarget, int] = {
    v: k for k, v in FUNC_APPLYTARGET_NAME.items()
}


### Func Target Type ###


FUNC_TARGETTYPE_NAME_REVERSE: dict[NiceFuncTargetType, int] = {
    v: k for k, v in FUNC_TARGETTYPE_NAME.items()
}


### Building enemy func signature ###

TARGETTYPE_WITH_ENEMY_APPLYTARGET = (
    NiceFuncTargetType.self_,
    NiceFuncTargetType.ptOne,
    NiceFuncTargetType.ptAnother,
    NiceFuncTargetType.ptAll,
    NiceFuncTargetType.ptFull,
    NiceFuncTargetType.ptOther,
    NiceFuncTargetType.ptOneOther,
    NiceFuncTargetType.ptRandom,
    NiceFuncTargetType.ptOtherFull,
    NiceFuncTargetType.ptselectOneSub,
    NiceFuncTargetType.ptselectSub,
    NiceFuncTargetType.ptOneAnotherRandom,
    NiceFuncTargetType.ptSelfAnotherRandom,
    NiceFuncTargetType.ptSelfAnotherFirst,
    NiceFuncTargetType.ptSelfBefore,
    NiceFuncTargetType.ptSelfAfter,
    NiceFuncTargetType.ptSelfAnotherLast,
    NiceFuncTargetType.commandTypeSelfTreasureDevice,
)


TARGETTYPE_WITH_PLAYER_APPLYTARGET = (
    NiceFuncTargetType.enemy,
    NiceFuncTargetType.enemyAnother,
    NiceFuncTargetType.enemyAll,
    NiceFuncTargetType.enemyFull,
    NiceFuncTargetType.enemyOther,
    NiceFuncTargetType.enemyRandom,
    NiceFuncTargetType.enemyOtherFull,
    NiceFuncTargetType.enemyOneAnotherRandom,
)


ENEMY_FUNC_TARGETING_PLAYER_TEAM = {
    (target_type, FuncApplyTarget.player)
    for target_type in TARGETTYPE_WITH_PLAYER_APPLYTARGET
}
ENEMY_FUNC_TARGETING_ENEMY_TEAM = {
    (target_type, FuncApplyTarget.enemy)
    for target_type in TARGETTYPE_WITH_ENEMY_APPLYTARGET
}
ENEMY_FUNC_SIGNATURE = (
    ENEMY_FUNC_TARGETING_PLAYER_TEAM | ENEMY_FUNC_TARGETING_ENEMY_TEAM
)


### Buff Type ###


BUFF_TYPE_NAME_REVERSE: dict[NiceBuffType, int] = {
    v: k for k, v in BUFF_TYPE_NAME.items()
}


### Item BG Type ###


class NiceItemBGType(str, Enum):
    """Item Background Type Enum"""

    zero = "zero"  # qp, friendpoint
    bronze = "bronze"
    silver = "silver"
    gold = "gold"
    questClearQPReward = "questClearQPReward"


ITEM_BG_TYPE_NAME: dict[int, NiceItemBGType] = {
    0: NiceItemBGType.zero,
    1: NiceItemBGType.bronze,
    2: NiceItemBGType.silver,
    3: NiceItemBGType.gold,
    4: NiceItemBGType.questClearQPReward,
}


ITEM_BG_TYPE_REVERSE = {v: k for k, v in ITEM_BG_TYPE_NAME.items()}


### Item Type ###


ITEM_TYPE_REVERSE = {v: k for k, v in ITEM_TYPE_NAME.items()}


### Card Type ###


CARD_TYPE_NAME_REVERSE: dict[NiceCardType, int] = {
    v: k for k, v in CARD_TYPE_NAME.items()
}


### Gender ###


GENDER_TYPE_NAME_REVERSE: dict[NiceGender, int] = {
    v: k for k, v in GENDER_TYPE_NAME.items()
}


### Attribute ###


class Attribute(str, Enum):
    """Servant Attribute Enum"""

    human = "human"
    sky = "sky"
    earth = "earth"
    star = "star"
    beast = "beast"
    void = "void"


ATTRIBUTE_NAME: dict[int, Attribute] = {
    1: Attribute.human,
    2: Attribute.sky,
    3: Attribute.earth,
    4: Attribute.star,
    5: Attribute.beast,
    10: Attribute.void,
}


ATTRIBUTE_NAME_REVERSE: dict[Attribute, int] = {v: k for k, v in ATTRIBUTE_NAME.items()}


### Servant Class ###


class SvtClass(str, Enum):
    """Servant Class"""

    saber = "saber"
    archer = "archer"
    lancer = "lancer"
    rider = "rider"
    caster = "caster"
    assassin = "assassin"
    berserker = "berserker"
    shielder = "shielder"
    ruler = "ruler"
    alterEgo = "alterEgo"
    avenger = "avenger"
    demonGodPillar = "demonGodPillar"
    moonCancer = "moonCancer"
    foreigner = "foreigner"
    grandCaster = "grandCaster"
    beastII = "beastII"
    ushiChaosTide = "ushiChaosTide"
    beastI = "beastI"
    beastIIIR = "beastIIIR"
    beastIIIL = "beastIIIL"
    beastUnknown = "beastUnknown"
    unknown = "unknown"
    cccFinaleEmiyaAlter = "cccFinaleEmiyaAlter"
    # OTHER = "OTHER"
    ALL = "ALL"
    # EXTRA = "EXTRA"
    # ALLCLASS = "ALLCLASS"


CLASS_NAME: dict[int, SvtClass] = {
    1: SvtClass.saber,
    2: SvtClass.archer,
    3: SvtClass.lancer,
    4: SvtClass.rider,
    5: SvtClass.caster,
    6: SvtClass.assassin,
    7: SvtClass.berserker,
    8: SvtClass.shielder,
    9: SvtClass.ruler,
    10: SvtClass.alterEgo,
    11: SvtClass.avenger,
    12: SvtClass.demonGodPillar,
    # 13
    # 14
    # 15
    # 16
    17: SvtClass.grandCaster,
    # 18
    # 19
    20: SvtClass.beastII,
    21: SvtClass.ushiChaosTide,
    22: SvtClass.beastI,
    23: SvtClass.moonCancer,
    24: SvtClass.beastIIIR,
    25: SvtClass.foreigner,
    26: SvtClass.beastIIIL,
    27: SvtClass.beastUnknown,  # LB 5.2 beast
    97: SvtClass.unknown,
    # 98
    # 99
    # 100
    # 107
    124: SvtClass.cccFinaleEmiyaAlter,
    # 125
    # 1000: SvtClass.OTHER,
    1001: SvtClass.ALL,
    # 1002: SvtClass.EXTRA,
    # 1003: SvtClass.ALLCLASS,
}


CLASS_NAME_REVERSE: dict[SvtClass, int] = {v: k for k, v in CLASS_NAME.items()}


PLAYABLE_CLASS_LIST = [
    SvtClass.saber,
    SvtClass.archer,
    SvtClass.lancer,
    SvtClass.rider,
    SvtClass.caster,
    SvtClass.assassin,
    SvtClass.berserker,
    SvtClass.shielder,
    SvtClass.ruler,
    SvtClass.alterEgo,
    SvtClass.avenger,
    SvtClass.moonCancer,
    SvtClass.foreigner,
]


### AI Type ###


class AiType(str, Enum):
    """AI Type: where the AI is used"""

    svt = "svt"
    field = "field"


### AI Timing ###


class AiTiming(str, Enum):
    """Field AI timing Enum"""

    dead = "dead"
    turnEnemyStart = "turnEnemyStart"
    turnEnemyEnd = "turnEnemyEnd"
    turnPlayerStart = "turnPlayerStart"
    turnPlayerEnd = "turnPlayerEnd"
    waveStart = "waveStart"
    turnStart = "turnStart"
    unknown = "unknown"


AI_TIMING_NAME: dict[int, AiTiming] = {
    -6: AiTiming.dead,
    -1: AiTiming.unknown,
    1: AiTiming.waveStart,
    2: AiTiming.turnStart,
    3: AiTiming.turnPlayerStart,
    4: AiTiming.turnPlayerEnd,
    5: AiTiming.turnEnemyStart,
    6: AiTiming.turnEnemyEnd,
}


### Enemy death type ###


class EnemyDeathType(str, Enum):
    ESCAPE = "escape"
    STAND = "stand"
    EFFECT = "effect"
    WAIT = "wait"


ENEMY_DEATH_TYPE_NAME: dict[int, EnemyDeathType] = {
    1: EnemyDeathType.ESCAPE,
    2: EnemyDeathType.STAND,
    3: EnemyDeathType.EFFECT,
    4: EnemyDeathType.WAIT,
}


### Mission Cond Detail Type ###


class DetailMissionCondType(IntEnum):
    ENEMY_KILL_NUM = 1
    ENEMY_INDIVIDUALITY_KILL_NUM = 2
    ITEM_GET_TOTAL = 3
    BATTLE_SVT_IN_DECK = 4  # Unused
    BATTLE_SVT_EQUIP_IN_DECK = 5  # Unused
    TARGET_QUEST_ENEMY_KILL_NUM = 6
    TARGET_QUEST_ENEMY_INDIVIDUALITY_KILL_NUM = 7
    TARGET_QUEST_ITEM_GET_TOTAL = 8
    QUEST_CLEAR_ONCE = 9
    QUEST_CLEAR_NUM_1 = 10
    ITEM_GET_BATTLE = 12
    DEFEAT_ENEMY_INDIVIDUALITY = 13
    DEFEAT_ENEMY_CLASS = 14
    DEFEAT_SERVANT_CLASS = 15
    DEFEAT_ENEMY_NOT_SERVANT_CLASS = 16
    BATTLE_SVT_CLASS_IN_DECK = 18  # Filter by svt class
    SVT_GET_BATTLE = 19  # Embers are svt instead of items
    FRIEND_POINT_SUMMON = 21
    BATTLE_SVT_ID_IN_DECK_1 = 22  # Filter by svt ID
    BATTLE_SVT_ID_IN_DECK_2 = 23
    QUEST_CLEAR_NUM_2 = 24  # Not sure what's the difference QUEST_CLEAR_NUM_1
    DICE_USE = 25  # Probably Fate/Requiem event
    SQUARE_ADVANCED = 26
    MORE_FRIEND_FOLLOWER = 27  # 5th Anniversary missions
    MAIN_QUEST_DONE = 28  # 22M Download Campaign


class NiceDetailMissionCondType(str, Enum):
    """Mission Condition Detail Condition Type Enum"""

    enemyKillNum = "enemyKillNum"
    enemyIndividualityKillNum = "enemyIndividualityKillNum"
    itemGetTotal = "itemGetTotal"
    battleSvtInDeck = "battleSvtInDeck"
    battleSvtEquipInDeck = "battleSvtEquipInDeck"
    targetQuestEnemyKillNum = "targetQuestEnemyKillNum"
    targetQuestEnemyIndividualityKillNum = "targetQuestEnemyIndividualityKillNum"
    targetQuestItemGetTotal = "targetQuestItemGetTotal"


DETAIL_MISSION_COND_TYPE: dict[int, NiceDetailMissionCondType] = {
    1: NiceDetailMissionCondType.enemyKillNum,
    2: NiceDetailMissionCondType.enemyIndividualityKillNum,
    3: NiceDetailMissionCondType.itemGetTotal,
    4: NiceDetailMissionCondType.battleSvtInDeck,
    5: NiceDetailMissionCondType.battleSvtEquipInDeck,
    6: NiceDetailMissionCondType.targetQuestEnemyKillNum,
    7: NiceDetailMissionCondType.targetQuestEnemyIndividualityKillNum,
    8: NiceDetailMissionCondType.targetQuestItemGetTotal,
}


class DetailMissionCondLinkType(IntEnum):
    EVENT_START = 1
    MISSION_START = 2
    MASTER＿MISSION_START = 3


class NiceDetailMissionCondLinkType(str, Enum):
    """Mission Condition Detail Condition Link Type Enum"""

    eventStart = "eventStart"
    missionStart = "missionStart"
    master＿missionStart = "master＿missionStart"


DETAIL_MISSION_LINK_TYPE: dict[int, NiceDetailMissionCondLinkType] = {
    1: NiceDetailMissionCondLinkType.eventStart,
    2: NiceDetailMissionCondLinkType.missionStart,
    3: NiceDetailMissionCondLinkType.master＿missionStart,
}


### Trait ###


class Trait(str, Enum):
    """Trait/Individuality Enum"""

    unknown = "unknown"
    genderMale = "genderMale"
    genderFemale = "genderFemale"
    genderUnknown = "genderUnknown"
    classSaber = "classSaber"
    classLancer = "classLancer"
    classArcher = "classArcher"
    classRider = "classRider"
    classCaster = "classCaster"
    classAssassin = "classAssassin"
    classBerserker = "classBerserker"
    classShielder = "classShielder"
    classRuler = "classRuler"
    classAlterEgo = "classAlterEgo"
    classAvenger = "classAvenger"
    classDemonGodPillar = "classDemonGodPillar"
    classGrandCaster = "classGrandCaster"
    classBeastI = "classBeastI"
    classBeastII = "classBeastII"
    classMoonCancer = "classMoonCancer"
    classBeastIIIR = "classBeastIIIR"
    classForeigner = "classForeigner"
    classBeastIIIL = "classBeastIIIL"
    classBeastUnknown = "classBeastUnknown"
    attributeSky = "attributeSky"
    attributeEarth = "attributeEarth"
    attributeHuman = "attributeHuman"
    attributeStar = "attributeStar"
    attributeBeast = "attributeBeast"
    alignmentLawful = "alignmentLawful"
    alignmentChaotic = "alignmentChaotic"
    alignmentNeutral = "alignmentNeutral"
    alignmentGood = "alignmentGood"
    alignmentEvil = "alignmentEvil"
    alignmentBalanced = "alignmentBalanced"
    alignmentMadness = "alignmentMadness"
    alignmentSummer = "alignmentSummer"
    basedOnServant = "basedOnServant"
    human = "human"
    undead = "undead"
    artificialDemon = "artificialDemon"
    demonBeast = "demonBeast"
    daemon = "daemon"
    soldier = "soldier"
    amazoness = "amazoness"
    skeleton = "skeleton"
    zombie = "zombie"
    ghost = "ghost"
    automata = "automata"
    golem = "golem"
    spellBook = "spellBook"
    homunculus = "homunculus"
    lamia = "lamia"
    centaur = "centaur"
    werebeast = "werebeast"
    chimera = "chimera"
    wyvern = "wyvern"
    dragonType = "dragonType"
    gazer = "gazer"
    handOrDoor = "handOrDoor"
    demonGodPillar = "demonGodPillar"
    oni = "oni"
    hand = "hand"
    door = "door"
    threatToHumanity = "threatToHumanity"
    divine = "divine"
    humanoid = "humanoid"
    dragon = "dragon"
    dragonSlayer = "dragonSlayer"
    roman = "roman"
    wildbeast = "wildbeast"
    atalante = "atalante"
    saberface = "saberface"
    weakToEnumaElish = "weakToEnumaElish"
    riding = "riding"
    arthur = "arthur"
    skyOrEarth = "skyOrEarth"
    brynhildsBeloved = "brynhildsBeloved"
    undeadOrDaemon = "undeadOrDaemon"
    demonic = "demonic"
    skyOrEarthExceptPseudoAndDemi = "skyOrEarthExceptPseudoAndDemi"
    divineOrDaemonOrUndead = "divineOrDaemonOrUndead"
    saberClassServant = "saberClassServant"
    superGiant = "superGiant"
    king = "king"
    greekMythologyMales = "greekMythologyMales"
    illya = "illya"
    feminineLookingServant = "feminineLookingServant"
    argonaut = "argonaut"
    genderCaenisServant = "genderCaenisServant"
    hominidaeServant = "hominidaeServant"
    blessedByKur = "blessedByKur"
    demonicBeastServant = "demonicBeastServant"
    canBeInBattle = "canBeInBattle"
    notBasedOnServant = "notBasedOnServant"
    livingHuman = "livingHuman"
    cardArts = "cardArts"
    cardBuster = "cardBuster"
    cardQuick = "cardQuick"
    cardExtra = "cardExtra"
    buffPositiveEffect = "buffPositiveEffect"
    buffNegativeEffect = "buffNegativeEffect"
    buffIncreaseDamage = "buffIncreaseDamage"
    buffIncreaseDefence = "buffIncreaseDefence"
    buffDecreaseDamage = "buffDecreaseDamage"
    buffDecreaseDefence = "buffDecreaseDefence"
    buffMentalEffect = "buffMentalEffect"
    buffPoison = "buffPoison"
    buffCharm = "buffCharm"
    buffPetrify = "buffPetrify"
    buffStun = "buffStun"
    buffBurn = "buffBurn"
    buffSpecialResistUp = "buffSpecialResistUp"
    buffSpecialResistDown = "buffSpecialResistDown"
    buffEvadeAndInvincible = "buffEvadeAndInvincible"
    buffSureHit = "buffSureHit"
    buffNpSeal = "buffNpSeal"
    buffEvade = "buffEvade"
    buffInvincible = "buffInvincible"
    buffTargetFocus = "buffTargetFocus"
    buffGuts = "buffGuts"
    skillSeal = "skillSeal"
    buffCurse = "buffCurse"
    buffAtkUp = "buffAtkUp"
    buffPowerModStrUp = "buffPowerModStrUp"
    buffDamagePlus = "buffDamagePlus"
    buffNpDamageUp = "buffNpDamageUp"
    buffCritDamageUp = "buffCritDamageUp"
    buffCritRateUp = "buffCritRateUp"
    buffAtkDown = "buffAtkDown"
    buffPowerModStrDown = "buffPowerModStrDown"
    buffDamageMinus = "buffDamageMinus"
    buffNpDamageDown = "buffNpDamageDown"
    buffCritDamageDown = "buffCritDamageDown"
    buffCritRateDown = "buffCritRateDown"
    buffDeathResistDown = "buffDeathResistDown"
    buffDefenceUp = "buffDefenceUp"
    buffMaxHpUpPercent = "buffMaxHpUpPercent"
    buffMaxHpDownPercent = "buffMaxHpDownPercent"
    buffMaxHpUp = "buffMaxHpUp"
    buffMaxHpDown = "buffMaxHpDown"
    buffImmobilize = "buffImmobilize"
    buffIncreasePoisonEffectiveness = "buffIncreasePoisonEffectiveness"
    buffPigify = "buffPigify"
    buffCurseEffectUp = "buffCurseEffectUp"
    buffTerrorStunChanceAfterTurn = "buffTerrorStunChanceAfterTurn"
    buffConfusion = "buffConfusion"
    buffOffensiveMode = "buffOffensiveMode"
    buffDefensiveMode = "buffDefensiveMode"
    buffLockCardsDeck = "buffLockCardsDeck"
    buffDisableColorCard = "buffDisableColorCard"
    buffChangeField = "buffChangeField"
    buffIncreaseDefenceAgainstIndividuality = "buffIncreaseDefenceAgainstIndividuality"
    buffInvinciblePierce = "buffInvinciblePierce"
    buffHpRecoveryPerTurn = "buffHpRecoveryPerTurn"
    buffNegativeEffectImmunity = "buffNegativeEffectImmunity"
    buffNegativeEffectAtTurnEnd = "buffNegativeEffectAtTurnEnd"
    normalAttack0 = "normalAttack0"
    normalAttack1 = "normalAttack1"
    normalAttack2 = "normalAttack2"
    criticalHit = "criticalHit"
    playerCards = "playerCards"
    cardNP = "cardNP"
    kingproteaGrowth = "kingproteaGrowth"
    kingproteaProliferation = "kingproteaProliferation"
    kingproteaProliferationNPDefense = "kingproteaProliferationNPDefense"
    fieldSunlight = "fieldSunlight"
    fieldShore = "fieldShore"
    fieldForest = "fieldForest"
    fieldBurning = "fieldBurning"
    fieldCity = "fieldCity"
    shadowServant = "shadowServant"
    aoeNP = "aoeNP"
    giant = "giant"
    childServant = "childServant"
    buffSpecialInvincible = "buffSpecialInvincible"
    buffSkillRankUp = "buffSkillRankUp"
    buffSleep = "buffSleep"
    nobunaga = "nobunaga"
    fieldImaginarySpace = "fieldImaginarySpace"
    existenceOutsideTheDomain = "existenceOutsideTheDomain"
    curse = "curse"
    fieldShoreOrImaginarySpace = "fieldShoreOrImaginarySpace"
    shutenOnField = "shutenOnField"
    shuten = "shuten"
    genji = "genji"
    vengeance = "vengeance"
    enemyGardenOfSinnersLivingCorpse = "enemyGardenOfSinnersLivingCorpse"
    enemyGardenOfSinnersApartmentGhostAndSkeleton = (
        "enemyGardenOfSinnersApartmentGhostAndSkeleton"
    )
    enemyGardenOfSinnersBaseModel = "enemyGardenOfSinnersBaseModel"
    enemyGardenOfSinnersVengefulSpiritOfSevenPeople = (
        "enemyGardenOfSinnersVengefulSpiritOfSevenPeople"
    )
    enemySaberEliWerebeastAndHomunculusAndKnight = (
        "enemySaberEliWerebeastAndHomunculusAndKnight"
    )
    enemySaberEliSkeletonAndGhostAndLamia = "enemySaberEliSkeletonAndGhostAndLamia"
    enemySaberEliBugAndGolem = "enemySaberEliBugAndGolem"
    enemySeraphEater = "enemySeraphEater"
    enemySeraphShapeshifter = "enemySeraphShapeshifter"
    enemySeraphTypeI = "enemySeraphTypeI"
    enemySeraphTypeSakura = "enemySeraphTypeSakura"
    enemyHimejiCastleKnightAndGazerAndMassProduction = (
        "enemyHimejiCastleKnightAndGazerAndMassProduction"
    )
    enemyHimejiCastleDronesAndHomunculusAndAutomata = (
        "enemyHimejiCastleDronesAndHomunculusAndAutomata"
    )
    enemyHimejiCastleSkeletonAndScarecrow = "enemyHimejiCastleSkeletonAndScarecrow"
    enemyGuda3MiniNobu = "enemyGuda3MiniNobu"
    enemyDavinciTrueEnemy = "enemyDavinciTrueEnemy"
    enemyDavinciFalseEnemy = "enemyDavinciFalseEnemy"
    enemyCaseFilesRareEnemy = "enemyCaseFilesRareEnemy"
    enemyLasVegasBonusEnemy = "enemyLasVegasBonusEnemy"
    enemySummerCampRareEnemy = "enemySummerCampRareEnemy"
    enemyLittleBigTenguTsuwamonoEnemy = "enemyLittleBigTenguTsuwamonoEnemy"
    eventSaberWars = "eventSaberWars"
    eventRashomon = "eventRashomon"
    eventOnigashima = "eventOnigashima"
    eventOnigashimaRaid = "eventOnigashimaRaid"
    eventPrisma = "eventPrisma"
    eventPrismaWorldEndMatch = "eventPrismaWorldEndMatch"
    eventNeroFest2 = "eventNeroFest2"
    eventGuda2 = "eventGuda2"
    eventNeroFest3 = "eventNeroFest3"
    eventSetsubun = "eventSetsubun"
    eventApocrypha = "eventApocrypha"
    eventBattleInNewYork1 = "eventBattleInNewYork1"
    eventOniland = "eventOniland"
    eventOoku = "eventOoku"
    eventGuda4 = "eventGuda4"
    eventLasVegas = "eventLasVegas"
    eventBattleInNewYork2 = "eventBattleInNewYork2"
    eventSaberWarsII = "eventSaberWarsII"
    eventSummerCamp = "eventSummerCamp"
    eventGuda5 = "eventGuda5"
    cursedBook = "cursedBook"
    buffCharmFemale = "buffCharmFemale"
    mechanical = "mechanical"
    fae = "fae"
    hasCostume = "hasCostume"


TRAIT_NAME: dict[int, Trait] = {
    1: Trait.genderMale,
    2: Trait.genderFemale,
    3: Trait.genderUnknown,
    100: Trait.classSaber,
    101: Trait.classLancer,
    102: Trait.classArcher,
    103: Trait.classRider,
    104: Trait.classCaster,
    105: Trait.classAssassin,
    106: Trait.classBerserker,
    107: Trait.classShielder,
    108: Trait.classRuler,
    109: Trait.classAlterEgo,
    110: Trait.classAvenger,
    111: Trait.classDemonGodPillar,
    112: Trait.classGrandCaster,
    113: Trait.classBeastI,
    114: Trait.classBeastII,
    115: Trait.classMoonCancer,
    116: Trait.classBeastIIIR,
    117: Trait.classForeigner,
    118: Trait.classBeastIIIL,
    119: Trait.classBeastUnknown,
    200: Trait.attributeSky,
    201: Trait.attributeEarth,
    202: Trait.attributeHuman,
    203: Trait.attributeStar,
    204: Trait.attributeBeast,
    300: Trait.alignmentLawful,
    301: Trait.alignmentChaotic,
    302: Trait.alignmentNeutral,
    303: Trait.alignmentGood,
    304: Trait.alignmentEvil,
    305: Trait.alignmentBalanced,
    306: Trait.alignmentMadness,
    308: Trait.alignmentSummer,
    1000: Trait.basedOnServant,  # can be NPC or enemy but use a servant's data
    1001: Trait.human,  # Sanson's 3rd skill
    1002: Trait.undead,  # Scathach's 3rd skill
    1003: Trait.artificialDemon,
    1004: Trait.demonBeast,
    1005: Trait.daemon,
    1100: Trait.soldier,
    1101: Trait.amazoness,
    1102: Trait.skeleton,
    1103: Trait.zombie,
    1104: Trait.ghost,
    1105: Trait.automata,
    1106: Trait.golem,
    1107: Trait.spellBook,
    1108: Trait.homunculus,
    1110: Trait.lamia,
    1111: Trait.centaur,
    1112: Trait.werebeast,
    1113: Trait.chimera,
    1117: Trait.wyvern,
    1118: Trait.dragonType,
    1119: Trait.gazer,
    1120: Trait.handOrDoor,
    1121: Trait.demonGodPillar,
    1122: Trait.shadowServant,
    1128: Trait.enemyGardenOfSinnersLivingCorpse,
    1129: Trait.enemyGardenOfSinnersApartmentGhostAndSkeleton,
    1130: Trait.enemyGardenOfSinnersBaseModel,
    1131: Trait.enemyGardenOfSinnersVengefulSpiritOfSevenPeople,
    1132: Trait.oni,
    1133: Trait.hand,
    1134: Trait.door,
    1135: Trait.enemySaberEliWerebeastAndHomunculusAndKnight,
    1136: Trait.enemySaberEliSkeletonAndGhostAndLamia,
    1137: Trait.enemySaberEliBugAndGolem,
    1138: Trait.enemySeraphEater,
    1139: Trait.enemySeraphShapeshifter,
    1140: Trait.enemySeraphTypeI,
    1141: Trait.enemySeraphTypeSakura,
    1155: Trait.enemyHimejiCastleKnightAndGazerAndMassProduction,
    1156: Trait.enemyHimejiCastleDronesAndHomunculusAndAutomata,
    1157: Trait.enemyHimejiCastleSkeletonAndScarecrow,
    1171: Trait.enemyGuda3MiniNobu,
    1172: Trait.threatToHumanity,
    1177: Trait.fae,
    2000: Trait.divine,
    2001: Trait.humanoid,
    2002: Trait.dragon,
    2003: Trait.dragonSlayer,
    2004: Trait.roman,
    2005: Trait.wildbeast,
    2006: Trait.atalante,
    2007: Trait.saberface,
    2008: Trait.weakToEnumaElish,
    2009: Trait.riding,
    2010: Trait.arthur,
    2011: Trait.skyOrEarth,  # Tesla's NP
    2012: Trait.brynhildsBeloved,
    2018: Trait.undeadOrDaemon,  # Amakusa bond CE
    2019: Trait.demonic,
    2023: Trait.enemyDavinciTrueEnemy,
    2024: Trait.enemyDavinciFalseEnemy,
    2037: Trait.skyOrEarthExceptPseudoAndDemi,  # Raikou's 3rd skill
    2038: Trait.fieldSunlight,
    2039: Trait.fieldShore,
    2040: Trait.divineOrDaemonOrUndead,  # Ruler Martha's 3rd skill
    2073: Trait.fieldForest,
    2074: Trait.blessedByKur,  # Eresh's 3rd skill add this individuality
    2075: Trait.saberClassServant,  # MHXA NP
    2076: Trait.superGiant,
    2113: Trait.king,
    2114: Trait.greekMythologyMales,
    2121: Trait.fieldBurning,
    2191: Trait.buffCharmFemale,  # Charm buffs that come from females; Fion 2nd skill
    2355: Trait.illya,
    2356: Trait.feminineLookingServant,  # Teach's 3rd skill
    2385: Trait.cursedBook,  # Murasaki Valentine
    2386: Trait.kingproteaProliferation,
    2387: Trait.kingproteaGrowth,
    2392: Trait.fieldCity,
    2403: Trait.enemyCaseFilesRareEnemy,
    2469: Trait.enemyLasVegasBonusEnemy,
    2466: Trait.argonaut,
    2615: Trait.genderCaenisServant,  # Phantom's 2nd skill
    2631: Trait.hominidaeServant,  # used in TamaVitch's fight
    2632: Trait.demonicBeastServant,  # used in TamaVitch's fight
    2654: Trait.livingHuman,  # Voyager's NP
    2663: Trait.enemySummerCampRareEnemy,
    2664: Trait.kingproteaProliferationNPDefense,
    2666: Trait.giant,
    2667: Trait.childServant,  # Summer Illya's 2nd skill
    2721: Trait.nobunaga,  # Nobukatsu's skill
    2729: Trait.curse,  # Van Gogh passive
    2730: Trait.fieldImaginarySpace,
    2731: Trait.existenceOutsideTheDomain,
    2732: Trait.fieldShoreOrImaginarySpace,  # Nemo's 3rd skill and bond CE
    2733: Trait.shutenOnField,  # Ibaraki strengthened 2nd skill
    2734: Trait.shuten,  # Ibaraki strengthened 2nd skill
    2735: Trait.genji,
    2749: Trait.enemyLittleBigTenguTsuwamonoEnemy,
    2759: Trait.vengeance,  # Taira 2nd skill and NP
    2780: Trait.hasCostume,
    2781: Trait.mechanical,
    # 2xxx: CQ or Story quests buff
    3000: Trait.normalAttack0,  # Normal attack, including NP
    3001: Trait.normalAttack1,  # Haven't figured out the difference between the 3
    3002: Trait.normalAttack2,  #
    3004: Trait.buffPositiveEffect,
    3005: Trait.buffNegativeEffect,  # mutually exclusive with 3004
    3006: Trait.buffIncreaseDamage,  # catch all damage: atk, np, powermod, ...
    3007: Trait.buffIncreaseDefence,  # catch all defence, including evade
    3008: Trait.buffDecreaseDamage,
    3009: Trait.buffDecreaseDefence,  # including death resist down and card color resist down
    3010: Trait.buffMentalEffect,  # charm, terror, confusion
    3011: Trait.buffPoison,
    3012: Trait.buffCharm,
    3013: Trait.buffPetrify,
    3014: Trait.buffStun,  # including Pigify
    3015: Trait.buffBurn,
    3016: Trait.buffSpecialResistUp,  # Unused stuffs
    3017: Trait.buffSpecialResistDown,  # Unused stuffs
    3018: Trait.buffEvadeAndInvincible,
    3019: Trait.buffSureHit,
    3020: Trait.buffNpSeal,
    3021: Trait.buffEvade,
    3022: Trait.buffInvincible,
    3023: Trait.buffTargetFocus,
    3024: Trait.buffGuts,
    3025: Trait.skillSeal,
    3026: Trait.buffCurse,
    3027: Trait.buffAtkUp,  # Likely not the best name for this
    3028: Trait.buffPowerModStrUp,
    3029: Trait.buffDamagePlus,
    3030: Trait.buffNpDamageUp,
    3031: Trait.buffCritDamageUp,
    3032: Trait.buffCritRateUp,
    3033: Trait.buffAtkDown,
    3034: Trait.buffPowerModStrDown,
    3035: Trait.buffDamageMinus,
    3036: Trait.buffNpDamageDown,
    3037: Trait.buffCritDamageDown,
    3038: Trait.buffCritRateDown,
    3039: Trait.buffDeathResistDown,
    3040: Trait.buffDefenceUp,
    3041: Trait.buffMaxHpUpPercent,
    3042: Trait.buffMaxHpDownPercent,
    3043: Trait.buffMaxHpUp,
    3044: Trait.buffMaxHpDown,
    3045: Trait.buffImmobilize,  # Including Petrify, Bound, Pigify, Stun
    3046: Trait.buffIncreasePoisonEffectiveness,
    3047: Trait.buffPigify,
    3048: Trait.buffCurseEffectUp,
    3049: Trait.buffTerrorStunChanceAfterTurn,
    3052: Trait.buffConfusion,
    3053: Trait.buffOffensiveMode,  # Unused
    3054: Trait.buffDefensiveMode,  # Unused
    3055: Trait.buffLockCardsDeck,  # Summer BB
    3056: Trait.buffDisableColorCard,
    3057: Trait.buffChangeField,
    3058: Trait.buffIncreaseDefenceAgainstIndividuality,  # Unsure
    3059: Trait.buffInvinciblePierce,
    3060: Trait.buffHpRecoveryPerTurn,
    3061: Trait.buffNegativeEffectImmunity,
    3063: Trait.buffNegativeEffectAtTurnEnd,
    3064: Trait.buffSpecialInvincible,
    3065: Trait.buffSkillRankUp,
    3066: Trait.buffSleep,
    # 6016: No detail
    # 6021: No detail
    # 6022: No detail
    # 10xxx: CCC Kiara buff
    4001: Trait.cardArts,
    4002: Trait.cardBuster,
    4003: Trait.cardQuick,
    4004: Trait.cardExtra,
    4007: Trait.cardNP,
    4008: Trait.playerCards,  # Normal Buster, Arts, Quick, Extra Attack
    4100: Trait.criticalHit,
    4101: Trait.aoeNP,
    5000: Trait.canBeInBattle,  # can be NPC, enemy or playable servant i.e. not CE
    5010: Trait.notBasedOnServant,
    94000015: Trait.eventSaberWars,
    94000037: Trait.eventRashomon,
    94000045: Trait.eventOnigashima,
    94000046: Trait.eventOnigashimaRaid,
    94000047: Trait.eventPrisma,
    94000048: Trait.eventPrismaWorldEndMatch,
    94000049: Trait.eventNeroFest2,
    94000057: Trait.eventGuda2,
    94000066: Trait.eventNeroFest3,
    94000071: Trait.eventSetsubun,
    94000074: Trait.eventApocrypha,
    94000077: Trait.eventBattleInNewYork1,
    94000078: Trait.eventOniland,
    94000086: Trait.eventOoku,
    94000089: Trait.eventGuda4,
    94000091: Trait.eventLasVegas,
    94000092: Trait.eventBattleInNewYork2,
    94000095: Trait.eventSaberWarsII,
    94000107: Trait.eventSummerCamp,
    94000108: Trait.eventGuda5,
}


TRAIT_NAME_REVERSE: dict[Trait, int] = {v: k for k, v in TRAIT_NAME.items()}


ALL_ENUMS = {
    "NiceSvtType": SVT_TYPE_NAME,
    "NiceSvtFlag": SVT_FLAG_NAME,
    "NiceSkillType": SKILL_TYPE_NAME,
    "NiceFuncType": FUNC_TYPE_NAME,
    "FuncApplyTarget": FUNC_APPLYTARGET_NAME,
    "NiceFuncTargetType": FUNC_TARGETTYPE_NAME,
    "NiceBuffType": BUFF_TYPE_NAME,
    "NiceBuffAction": BUFF_ACTION_NAME,
    "NiceBuffLimit": BUFF_LIMIT_NAME,
    "NiceClassRelationOverwriteType": CLASS_OVERWRITE_NAME,
    "NiceItemType": ITEM_TYPE_NAME,
    "NiceItemBGType": ITEM_BG_TYPE_NAME,
    "NiceCardType": CARD_TYPE_NAME,
    "Gender": GENDER_TYPE_NAME,
    "Attribute": ATTRIBUTE_NAME,
    "SvtClass": CLASS_NAME,
    "NiceStatusRank": STATUS_RANK_NAME,
    "NiceCondType": COND_TYPE_NAME,
    "NiceVoiceCondType": VOICE_COND_NAME,
    "NiceSvtVoiceType": VOICE_TYPE_NAME,
    "NiceQuestType": QUEST_TYPE_NAME,
    "NiceConsumeType": QUEST_CONSUME_TYPE_NAME,
    "NiceEventType": EVENT_TYPE_NAME,
    "Trait": TRAIT_NAME,
    "NiceWarStartType": WAR_START_TYPE_NAME,
    "NiceWarOverwriteType": WAR_OVERWRITE_TYPE_NAME,
    "NiceGiftType": GIFT_TYPE_NAME,
    "NicePayType": PAY_TYPE_NAME,
    "NicePurchaseType": PURCHASE_TYPE_NAME,
    "NiceShopType": SHOP_TYPE_NAME,
    "NiceAiActType": AI_ACT_TYPE_NAME,
    "NiceAiActTarget": AI_ACT_TARGET_NAME,
    "NiceAiActNum": AI_ACT_NUM_NAME,
    "NiceAiCond": AI_COND_NAME,
    "AiTiming": AI_TIMING_NAME,
    "NiceMissionType": MISSION_TYPE_NAME,
    "NiceMissionRewardType": MISSION_REWARD_TYPE_NAME,
    "NiceMissionProgressType": MISSION_PROGRESS_TYPE_NAME,
    "NiceDetailMissionCondType": DETAIL_MISSION_COND_TYPE,
    "NiceDetailMissionCondLinkType": DETAIL_MISSION_LINK_TYPE,
    "NiceLotteryFlag": EVENT_LOTTERY_FLAG_NAME,
}
