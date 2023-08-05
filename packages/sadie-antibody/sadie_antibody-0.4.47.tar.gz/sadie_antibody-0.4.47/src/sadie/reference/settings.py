RECEPTORS = ["IG", "TR"]
IMGT_DEF_nt = {
    "FW1": {"start": 1, "end": 78},
    "CDR1": {"start": 79, "end": 114},
    "FW2": {"start": 115, "end": 165},
    "CDR2": {"start": 166, "end": 195},
    "FW3": {"start": 196, "end": 312},
    "CDR3": {"start": 312, "end": ""},
    "V-REGION": {"start": 0, "end": ""},
}

IMGT_GB_LOOKUP = {
    "Canis_lupus_familiaris_boxer": "dog",
    "Felis_catus_Abyssinian": "cat",
    "Canis_lupus_familiaris_Canis_lupus_familiaris_boxer": "dog",
    "Rattus_norvegicus_BN;_Sprague-Dawley": "rat",
    "Rattus_norvegicus_BN/SsNHsdMCW": "rat",
    "Rattus_norvegicus": "rat",
    "Mus_musculus_C57BL/6": "mouse",
    "Mus_musculus_BALB/c": "mouse",
    "Mus_musculus_C57BL/6J": "mouse",
    "Mus_musculus_MRL/lpr": "mouse",
    "Mus_musculus": "mouse",
    "Mus_musculus_A/J": "mouse",
    "Mus_musculus_C57BL/10": "mouse",
    "Mus_musculus_129/Sv": "mouse",
    "Mus_musculus_NZB": "mouse",
    "Mus_musculus_I/St": "mouse",
    "Mus_musculus_NFS": "mouse",
    "Mus_musculus_BALB.K": "mouse",
    "Mus_musculus_C3H": "mouse",
    "Mus_musculus_NZB/BINJ": "mouse",
    "Mus_musculus_CE/J": "mouse",
    "Mus_musculus_PERU": "mouse",
    "Mus_musculus_AKR": "mouse",
    "Mus_musculus_domesticus": "mouse",
    "Mus_musculus_O20/A": "mouse",
    "Mus_musculus_castaneus": "mouse",
    "Mus_musculus_molossinus_MOLF/Ei": "mouse",
    "Mus_musculus_musculus": "mouse",
    "Mus_musculus_castaneus_CAST/Ei": "mouse",
    "Mus_musculus_C58": "mouse",
    "Mus_musculus_SK": "mouse",
    "Mus_musculus_PERA": "mouse",
    "Mus_musculus_MRL": "mouse",
    "Mus_musculus_MBK": "mouse",
    "Mus_musculus_PWK": "mouse",
    "Mus_musculus_MAI": "mouse",
    "Homo_sapiens": "human",
    "Vicugna_pacos": "alpaca",
}


IMGT_LOOKUP = {
    "human": "Homo_sapiens",
    "cow": "Bos_taurus",
    "camel": "Camelus_dromedarius",
    "dog": "Canis_lupus_familiaris",
    "cat": "Felis_catus",
    "junglefowl": "Gallus_gallus",
    "night_monkey": "Aotus_nancymaae",
    "goat": "Capra_hircus",
    "sharks": "Chondrichthyes",
    "zebrafish": "Danio_rerio",
    "horse": "Equus_caballus",
    "cod": "Gadus_morhua",
    "catfish": "Ictalurus_punctatus",
    "crabmacaque": "Macaca_fascicularis",
    "macaque": "Macaca_mulatta",
    "mouse": "Mus_musculus",
    "ferret": "Mustela_putorius_furo",
    "nhp": "Nonhuman_primates",
    "trout": "Oncorhynchus_mykiss",
    "platypus": "Ornithorhynchus_anatinus",
    "rabbit": "Oryctolagus_cuniculus",
    "sheep": "Ovis_aries",
    "rat": "Rattus_norvegicus",
    "salmon": "Salmo_salar",
    "boar": "Sus_scrofa",
    "teleosts": "Teleostei",
    "dolphin": "Tursiops_truncatus",
    "alpaca": "Vicugna_pacos",
}

REVERSE_IMGT_LOOKUP = {v: k for k, v in IMGT_LOOKUP.items()}

BLAST_CONVENTION = {"IG": "Ig", "TR": "TCR"}


SEGMENTS_INTERNAL_DATA = {
    "TR": ["TRAV", "TRBV", "TRDV", "TRGV"],
    "IG": ["IGHV", "IGKV", "IGLV"],
}
SEGMENTS = {
    "TR": ["TRAV", "TRBD", "TRBJ", "TRBV", "TRDD", "TRDJ", "TRDV", "TRGV", "TRGJ"],
    "IG": ["IGHD", "IGHJ", "IGHV", "IGKJ", "IGKV", "IGLJ", "IGLV"],
}


MOTIF_LOOKUP = {
    "mouse": {
        "IGHJ": r"WG.G",
        "IGKJ": r"F[SG].G",
        "IGLJ": r"FG.G",
        "TRAJ": r"[FLWC][GSVA].[GEWE]",
        "TRBJ": r"[FH][GA].G",
        "TRGJ": r"FA[EK]G",
        "ignore": ["IGLJ3P", "TRAJ41", "TRAJ60", "TRAJ61", "TRBJ2-6"],
    },
    "rat": {"IGHJ": r"WG.G", "IGKJ": r"FG.G", "IGLJ": r"[FL]G.G", "ignore": ["IGKJ3"]},
    "human": {
        "IGHJ": r"WG.G",
        "IGKJ": r"FG",
        "IGLJ": r"FG.G",
        "TRAJ": r"[FWC][GA].[GEN]",
        "TRBJ": r"[FVG][GR].[G]",
        "TRGJ": r"F[GA].G",
        "TRDJ": r"FG.G",
        "ignore": "",
    },
    "macaque": {
        "IGHJ": r"WG.G",
        "IGKJ": r"FG.G",
        "IGLJ": r"F[GC].GT",
        "TRAJ": r"[FWS][GV].[GSRE][TMVS]",
        "TRBJ": r"[F][G].[G]",
        "TRDJ": r"FG.G",
        "TRGJ": r"F[GA].[G*]",
        "ignore": "",
    },
    "nhp": {
        "TRAJ": r"[F][G].[G][T]",
        "TRBJ": r"[F][G].[G][TS]",
        "TRDJ": r"F[GDA].[GT]T",
        "TRGJ": r"F[GDA].[GT]T",
        "ignore": ["TRAJ34", "TRBJ1-1", "TRBJ1-4", "TRBJ1-5", "TRBJ2-5"],
    },
    "platypus": {"IGHJ": r"WGQG", "ignore": []},
    "rabbit": {
        "IGHJ": r"WG.GT",
        "IGKJ": r"[FLR]G.[GE]T",
        "IGLJ": r"F[GS].[RG]T",
        "TRAJ": r"[FLW][GE].[CGRK][TMS]",
        "TRBJ": r"[F]G.G[TS]",
        "TRDJ": r"[F]G.G[TS]",
        "TRGJ": r"[F]G.GT",
        "ignore": [],
    },
    "night_monkey": {
        "TRAJ": r"[F][G].[G][T]",
        "TRBJ": r"[F][G].[G][TS]",
        "TRDJ": r"F[GA].[G]T",
        "TRGJ": r"F[GA].[G]T",
        "ignore": ["TRAJ34", "TRBJ1-1", "TRBJ1-4", "TRBJ1-5", "TRBJ2-5", "TRDJ2"],
    },
    "boar": {
        "ignore": "",
        "IGHJ": r"WG.G",
        "IGKJ": r"FG.GT",
        "IGLJ": r"FG.GT",
        "TRBJ": r"FG.G",
    },
    "cow": {
        "ignore": "",
        "IGHJ": r"[WC][SG][QPSR].",
        "IGKJ": r"[FL]G.[GR]T..E",
        "IGLJ": r"[FL][GI][SG][GR]T",
        "TRAJ": r"[FWL][GAS].[GK][TS]",
        "TRDJ": r"FG.[GE]",
        "TRGJ": r"[FLY][GN][VEK][GA]",
    },
    "crabmacaque": {"ignore": "", "IGHJ": r"WG.G"},
    "dolphin": {
        "ignore": "",
        "TRAJ": r"[FCLWSY][GS].[GRLK]",
        "TRGJ": r"[FCLWSY]G.[GRL]",
        "TRDJ": r"[FCLWSY][RG].[GRL]",
    },
    "ferret": {"ignore": "", "TRBJ": r"[F][GA].G", "TRAJ": r"[F][GA].G"},
    "camel": {
        "ignore": ["TRBJ3-4"],
        "IGHJ": r"WG.G",
        "IGKJ": r"[FL]G.GT",
        "IGLJ": r"FG.GT",
        "TRBJ": r"FG.G",
        "TRGJ": r"FG.G",
    },
    "goat": {"ignore": [""], "IGKJ": r"[FL]G.GT", "IGLJ": r"[FL]G.GT"},
    "horse": {"ignore": [""], "IGKJ": r"[F]G.GT", "IGHJ": r"[W][GD].G"},
    "dog": {
        "IGHJ": r"WG.G",
        "IGKJ": r"F[GS].G",
        "IGLJ": r"FG.G",
        "TRAJ": r"[FSW][GW].[GRLER]",
        "TRBJ": r"[F][GA].[G]",
        "TRGJ": r"[LFM][GTA].[GDV]",
        "TRDJ": r"FG.[GL]",
        "ignore": "",
    },
    "cat": {
        "IGHJ": r"WG.G",
        "IGKJ": r"F[G].G",
        "IGLJ": r"F[GNS].G",
        "TRAJ": r"[FWL][ERGW].[GRCKEQ]",
        "TRBJ": r"[F][TG].[G]",
        "TRGJ": r"[SF][TGAD].[G]",
        "TRDJ": r"FG.[G]",
        "ignore": "",
    },
    "alpaca": {"IGHJ": r"[WL]G[TQK][VG]", "ignore": [""]},
    "salmon": {"IGHJ": r"[W*][EG][KQ]GT", "ignore": [""]},
    "sharks": {
        "ignore": [
            "PEKGVGTVLTVR",
            "SYEYGGGTVVTVNP",
            "RHGLLGTRDHGDGDC",
            "RHGLLGTRDHGDGDC",
            "ACGDGTFVTVNP",
            "YGADTVVTVNP",
            "YAACGAGTAVTVNP",
            "LSRLLGTRDHGDGDC",
            "YGSGTVLTVNP",
            "YGGGTVVTVNP",
            "HHGLLGTRDHGDGDF",
            "GLLGTRDHGDGDC",
            "YGGGTVVTVNP",
            "SFDEYGGGTVVT",
            "SPNYWGGGSMVTVTC",
            "YAAVGDGTAVTVNP",
            "YGGGTVVTVNP",
            "YAACGDATAVTVNP",
            "DYKGGDTLLTVK",
            "SYEYGGGTVVT",
            "CGDNTAVTVNP",
            "ERPGTALTVK",
            "QLCCMRRRHCRD",
            "HHGLLGTRDHGDGDC",
            "YGGGTVVTVNP",
            "MLHAEMALRDCES",
            "YEKGAGTVLTVK",
            "HHGLLGTRDHGDGDC",
            "NEKGAGTVLTVK",
            "DEEGAGTVLTVK",
            "GGAGTVLTVK",
            "YGGGTGVTVNP",
            "YGGGTVVTVNP",
            "LPRLLGTRDHGDGDC",
        ],
        "IGHJ": r"[WCH][G].[RGS][TK]",
    },
    "sheep": {
        "IGLJ": r"[LF]G[GS]GT",
        "IGHJ": r"W[GD].[GR]",
        "IGKJ": r"FG[PGQ]GT",
        "TRAJ": r"[LFWE][GAKW].[GQ][TDRA]",
        "TRBJ": r"[F][G].[G][TS]",
        "TRDJ": r"FG.[EG]T",
        "ignore": ["FGDFYFLRGEGRRLAVV", "RPGAALTYGAGSGLAAG"],
    },
    "trout": {
        "ignore": ["SGAYAAYFGEXTKLTVL", "SYSEAYXXAGXKLTVL"],
        "IGHJ": r"WG.G",
        "TRBJ": r"FG.G[ATS]",
    },
    "zebrafish": {
        "ignore": ["IGIJ1", "IGIJ2", "IGIJ3", "IGIJ5", "IGIJ6S1", "IGIJ7S1", "IGIJ8S1"],
        "IGHJ": r"WG.GT",
        "TRAJ": r"[FM][GAST].G[TVSM]",
        "TRDJ": r"FG.P",
    },
}

J_SEGMENTS = {"IG": ["IGHJ", "IGKJ", "IGKJ"], "TR": ["TRAJ", "TRBJ", "TRGJ", "TRDJ"]}
RENAME_DICT = {
    "CDR1-IMGT": "cdr1_nt",
    "FR1-IMGT": "fwr1_nt",
    "FR2-IMGT": "fwr2_nt",
    "FR3-IMGT": "fwr3_nt",
    "CDR2-IMGT": "cdr2_nt",
    "CDR3-IMGT": "cdr3_nt",
    "FW1": "fwr1_nt",
    "FW2": "fwr2_nt",
    "FW3": "fwr3_nt",
    "CDR1": "cdr1_nt",
    "CDR2": "cdr2_nt",
    "CDR3": "cdr3_nt",
    "V-REGION": "v_gene_nt",
    "D-REGION": "d_gene_nt",
    "J-REGION": "j_gene_nt",
}
RENAME_DICT_TRANSLATE = {
    "cdr1_nt": "cdr1_aa",
    "fwr1_nt": "fwr1_aa",
    "fwr2_nt": "fwr2_aa",
    "fwr3_nt": "fwr3_aa",
    "cdr2_nt": "cdr2_aa",
    "cdr3_nt": "cdr3_aa",
}
