'''various information about each agency.'''


# API keys for each agency's ideascale site
agencies = {
    "usaid": "b9b85bb0-5588-4ac3-8a5c-0271851e2130",
    "comm":"d4d38eba-0c12-4bd4-a4e2-e20494a86b22",
    "dod": "3582db25-510d-48fe-85d2-479d6406535e",
    "ed": "76330bcb-fcf3-421c-bd87-bf593e3ebce3",
    "energy": "2574a2ec-c7f7-4477-9a30-3fb268794682",
    "nasa":"519f0a2f-4ac7-4ae2-ac11-8a11d0d9657e",   
    'dot': "280cb7ec-7ca9-4f01-9bc2-713d12342649",
    "int": "f80b132a-34f8-4ffd-81c3-7e70bf9f594b",
    "va": "f63a2606-99a3-4ce5-a080-68ed5f107ff0",
    "treas": "d3dd6bd1-d7a5-4835-b6ce-4043ce3c1320",
    "gsa": "2adaed68-d4b5-41f1-a9eb-2b7f130dd1db",
    "opm": "40cbf454-b08e-4269-b5e6-c2cb236bea4c",
    "labor": "9ff0f8f6-edb3-403f-8f96-495213c9a4f2",
    "doj": "fe53f6d0-de45-44f9-a4ea-8b96cde8e700",
    "ssa": "d4705ead-06f8-43fa-ae86-b826f541d6b5",
    "state": "f60a95c1-5a31-4c09-9ac0-c8f1dcb0980f",
    "nsf": "940e088e-a98e-4a57-934e-b73902fdb1a1",
    "hud": "1ffcaa2b-3f87-4b39-92b8-05375d728ca6",
    "epa": "91b203d8-69eb-43a5-a8fe-6f52d738ff0c",
    "sba": "722d6090-8246-4d98-9ef7-73531ce1dc31",
    "dhs": "ead2e53e-33f4-446a-98df-ab1d6a06e6f9",
    "nrc": "1fca50af-3b29-4d0d-aad4-023a661db7f4",
    "ostp": "3aa69b00-0fdb-445d-81cc-93097a4b07ae",
}

# category id for each category for each agency (yes the freaking
# categories are DIFFERENT FOR EVERY SINGLE AGENCY. $*%@*!#*$%&).
cat_id = {
    'usaid': {11832: 'transparency' , 11833: 'participation', 11834:'collaboration', 11835: 'innovation', 11836: 'site_feedback'}, 
    'comm': {11860: 'transparency', 11861: 'participation', 11862: 'collaboration', 11863: 'innovation', 11864: 'site_feedback'}, 
    'dod': {11865: 'transparency', 11866: 'participation', 11867: 'collaboration', 11868: 'innovation', 11869: 'site_feedback'}, 
    'ed': {11870: 'transparency', 11871: 'participation', 11872: 'collaboration', 11873: 'innovation', 11874: 'site_feedback'}, 
    'energy': {11808: 'transparency', 11809: 'participation', 11810: 'collaboration', 11811: 'innovation', 11812: 'site_feedback'}, 
    'nasa': {11571: 'transparency', 11572: 'participation', 11573: 'collaboration', 11928: 'innovation', 11929: 'site_feedback'}, 
    'dot': {11908: 'transparency', 11909: 'participation', 11910: 'collaboration', 11911: 'innovation', 11912: 'site_feedback'}, 
    'int': {11883: 'transparency', 11884: 'participation', 11885: 'collaboration', 11886: 'innovation', 11887: 'site_feedback'}, 
    'va': {11918: 'transparency', 11919: 'participation', 11920: 'collaboration', 11921: 'innovation', 11922: 'site_feedback'}, 
    'treas': {11913: 'transparency', 11914: 'participation', 11915: 'collaboration', 11916: 'innovation', 11917: 'site_feedback'}, 
    'gsa': {11827: 'transparency', 11828: 'participation', 11829: 'collaboration', 11830: 'innovation', 11831: 'site_feedback'}, 
    'opm': {11580: 'transparency', 11581: 'participation', 11582: 'collaboration', 11937: 'innovation', 11938: 'site_feedback'}, 
    'labor': {11893: 'transparency', 11894: 'participation', 11895: 'collaboration', 11896: 'innovation', 11897: 'site_feedback'}, 
    'doj': {11888: 'transparency', 11889: 'participation', 11890: 'collaboration', 11891: 'innovation', 11892: 'site_feedback'}, 
    'ssa': {11653: 'transparency', 11654: 'participation', 11655: 'collaboration', 11941: 'innovation', 11942: 'site_feedback'}, 
    'state': {11903: 'transparency', 11904: 'participation', 11905: 'collaboration', 11906: 'innovation', 11907: 'site_feedback'}, 
    'nsf': {11577: 'transparency', 11578: 'participation', 11579: 'collaboration', 11930: 'innovation', 11931: 'site_feedback'}, 
    'hud': {11878: 'transparency', 11879: 'participation', 11880: 'collaboration', 11881: 'innovation', 11882: 'site_feedback'}, 
    'epa': {11813: 'transparency', 11814: 'participation', 11815: 'collaboration', 11816: 'innovation', 11817: 'site_feedback'}, 
    'sba': {11650: 'transparency', 11651: 'participation', 11652: 'collaboration', 11939: 'innovation', 11940: 'site_feedback'}, 
    'dhs': {11923: 'transparency', 11924: 'participation', 11925: 'collaboration', 11926: 'innovation', 11927: 'site_feedback'}, 
    'nrc': {11583: 'transparency', 11584: 'participation', 11585: 'collaboration', 11935: 'innovation', 11936: 'site_feedback'}, 
    'ostp': {12295: 'transparency', 12296: 'participation', 12297: 'collaboration', 12299: 'innovation', 122300: 'site_feedback'}, 
}

def display_name(agency):
    ''' Return a pretty print display name for each agency'''
    _display_names = {
        "usaid": "USAID",
        "comm":"Commerce",
        "dod": "DoD",
        "ed": "Education",
        "energy": "Energy",
        "nasa":"NASA",   
        'dot': "Transportation",
        "int": "Interior",
        "va": "Veterans Affairs",
        "treas": "Treasury",
        "gsa": "GSA",
        "opm": "OPM",
        "labor": "Labor",
        "doj": "Justice",
        "ssa": "SSA",
        "state": "State",
        "nsf": "NSF",
        "hud": "HUD",
        "epa": "EPA",
        "sba": "SBA",
        "dhs": "DHS",
        "nrc": "NRC",
        "ostp": "OSTP",
        }
    return _display_names[agency]

def get_logo(agency):
    ''' retrieve the path to the logo image for each agency'''
    logo = {
        "usaid": "static/images/logo/usaid.jpg",
        "comm":"static/images/logo/doc.gif",
        "dod": "static/images/logo/dod.gif",
        "ed": "static/images/logo/doed.gif",
        "energy": "static/images/logo/doe.jpg",
        "nasa":"static/images/logo/nasa.jpg",   
        'dot': "static/images/logo/dot.png",
        "int": "static/images/logo/doi.jpg",
        "va": "static/images/logo/va.jpg",
        "treas": "static/images/logo/treasury.png",
        "gsa": "static/images/logo/gsa.jpg",
        "opm": "static/images/logo/opm.jpg",
        "labor": "static/images/logo/dol.jpg",
        "doj": "static/images/logo/doj.png",
        "ssa": "static/images/logo/ssa.gif",
        "state": "static/images/logo/state.jpg",
        "nsf": "static/images/logo/nsf.gif",
        "hud": "static/images/logo/hud.jpg",
        "epa": "static/images/logo/epa.png",
        "sba": "static/images/logo/sba.gif",
        "dhs": "static/images/logo/dhs.jpg",
        "nrc": "static/images/logo/nrc.jpg",
        "ostp": "static/images/logo/ostp.png",
        }
    return logo[agency]


open_pages = {
    "usaid": "http://www.usaid.gov/open/",
    "comm":"http://www.commerce.gov/open/",
    "dod": "http://www.defense.gov/open",
    "ed": "http://www.ed.gov/open/",
    "energy": "http://www.energy.gov/open",
    "nasa":"http://www.nasa.gov/open/",   
    'dot': "http://www.dot.gov/open/",
    "int": "http://www.doi.gov/open/",
    "va": "http://www.va.gov/open/",
    "treas": "http://www.treasury.gov/open/",
    "gsa": "http://www.gsa.gov/open/",
    "opm": "http://www.opm.gov/open/",
    "labor": "http://www.dol.gov/open/",
    "doj": "http://www.justice.gov/open/",
    "ssa": "http://www.ssa.gov/open/",
    "state": "http://www.state.gov/open",
    "nsf": "http://www.nsf.gov/open/",
    "hud": "http://www.hud.gov/open/",
    "epa": "http://www.epa.gov/open/",
    "sba": "http://www.sba.gov/open/",
    "dhs": "http://www.dhs.gov/open/",
    "nrc": "http://www.nrc.gov/open/",
    "ostp": "http://www.whitehouse.gov/administration/eop/ostp/open/",
}

gov_shortener = {
    "usaid": "http://bit.ly/9Nq9aw",
    "comm":"http://bit.ly/bdtMSQ",
    "dod": "http://bit.ly/bYZk5k",
    "ed": "http://bit.ly/cy1wKo",
    "energy": "http://bit.ly/cpRf7a",
    "nasa":"http://bit.ly/da3uc6",   
    'dot': "http://bit.ly/bvGA49",
    "int": "http://bit.ly/dgFxh1",
    "va": "http://bit.ly/btDUvm",
    "treas": "http://bit.ly/92qYA5",
    "gsa": "http://bit.ly/93MOcu",
    "opm": "http://bit.ly/9DoYra",
    "labor": "http://bit.ly/9V5Hrb",
    "doj": "http://bit.ly/behSUt",
    "ssa": "http://bit.ly/bxoytd",
    "state": "http://bit.ly/cwD4ht",
    "nsf": "http://bit.ly/cWfOgM",
    "hud": "http://bit.ly/d2axLy",
    "epa": "http://bit.ly/bCxSmJ",
    "sba": "http://bit.ly/dc7J65",
    "dhs": "http://bit.ly/9bX6UO",
    "nrc": "http://bit.ly/aQx2wv",
    "ostp": "http://bit.ly/d4Yv8F",  
    }

ideascale_link = {
    "usaid": "http://openusaid.ideascale.com",
    "comm": "http://opencommerce.ideascale.com",
    "dod": "http://opendefense.ideascale.com",
    "ed": "http://openeducation.ideascale.com",
    "energy": "http://openenergy.ideascale.com",
    "nasa": "http://opennasa.ideascale.com",
    'dot': "http://opendot.ideascale.com",
    "int": "http://openinterior.ideascale.com",
    "va": "http://openva.ideascale.com",
    "treas": "http://opentreasury.ideascale.com",
    "gsa": "http://opengsa.ideascale.com",
    "opm": "http://openopm.ideascale.com",
    "labor": "http://opendol.ideascale.com",
    "doj": "http://opendoj.ideascale.com",
    "ssa": "http://opensocialsecurity.ideascale.com",
    "state": "http://openstate.ideascale.com",
    "nsf": "http://opennsf.ideascale.com",
    "hud": "http://openhud.ideascale.com",
    "epa": "http://openepa.ideascale.com",
    "sba": "http://opensba.ideascale.com",
    "dhs": "http://openhomelandsecurity.ideascale.com",
    "nrc": "http://opennrc.ideascale.com",
    "ostp": "http://openostp.ideascale.com",
    }
