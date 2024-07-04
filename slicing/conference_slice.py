
from .net_structure import mac 

def get_conference_mac_mapping():
    return {
        1: {
            # Direct connections
            mac("h1"): 3, mac("h2"): 4, mac("vc1"): 5,

            # Fast connection
            mac("h3"): 1, mac("h4"): 1, mac("h5"): 1,

            # Fast connection for conference
            mac("ds"): 1, mac("vc2"): 1
        },

        2: {
            # Direct connections
            mac("h5"): 4,

            # Fast connection
            mac("h1"): 1, mac("h2"): 1, mac("h3"): 3, mac("h4"): 3,

            # Fast connection for conference
            mac("vc1"): 1, mac("vc2"): 3,
            mac("ds"): 2,

            # Production server missing: no hosts should contact that host
        },

        3: {
            # Direct connections
            mac("h3"): 3, mac("h4"): 4, mac("vc2"): 5,

            # Fast connection
            mac("h1"): 1, mac("h2"): 1, mac("h5"): 1,

            # Fast connection for conference
            mac("ds"): 1, mac("vc1"): 1,
        },

        4: {
            # Direct connections
            mac("ds"): 4,

            # Fast conference connections
            mac("vc1"): 1, mac("vc2"): 2,

            mac("h1"): 2, mac("h2"): 2, mac("h3"): 2, mac("h4"): 2, mac("h5"): 2,
        },

        5: {
            # fast connection
            mac("h1"): 1, mac("h2"): 1, mac("h3"): 1, mac("h4"): 1, mac("h5"): 1,
            mac("vc2"): 1, mac("vc1"): 1,

            mac("ds"): 2
        },
    }



def get_conference_forbidden():
    # Basically every host can communicate with the others, with the exeption of the production
    # server, that is isolated
    return {
        
        mac("vc1"): set([ mac("ps")]),
        mac("vc2"): set([ mac("ps")]),

        mac("h1"): set([ mac("ps")]),
        mac("h2"): set([ mac("ps")]),
        mac("h3"): set([ mac("ps")]),
        mac("h4"): set([ mac("ps")]),
        mac("h5"): set([ mac("ps")]),
        # TODO: h5

        mac("ps"): set([ mac("h1"), mac("h2"), mac("h3"), mac("h4"), mac("h5"), mac("vc1"), mac("vc2"), mac("ds") ]),
        mac("ds"): set([ mac("ps")])

    }
