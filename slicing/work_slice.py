from .net_structure import mac 

def get_work_mac_mapping():
    return {
        1: {
            # Direct connections
            mac("h1"): 3, mac("h2"): 4, mac("vc1"): 5,

            # Slow connection
            mac("ds"): 2, 

            mac("vc2"): {
                mac("vc1"): 2
            },

            # Fast connection
            mac("h3"): 1, mac("h4"): 1, 

            mac("h5"): {
                mac("h1"): 1, 
                mac("h2"): 1,

                mac("vc1"): 2
            },

            mac("ps"): 1,
        },

        2: {
            # Direct connections
            mac("h5"): 4,

            # Fast (lateral and server) connection
            mac("h1"): 1, mac("h2"): 1, mac("h3"): 3, mac("h4"): 3,

            mac("ps"): (2, 251),

            # Fast (bottom, slow bottleneck) connection
            mac("vc1"): (2, 252), mac("vc2"): (2, 252),   

            # Gaming server missing: no hosts need to contact that host
        },

        3: {
            # Direct connections
            mac("h3"): 3, mac("h4"): 4, mac("vc2"): 5,

            # Slow connection
            mac("ds"): 2, 

            mac("vc1"): {
                mac("vc2"): 2

            },

            # Fast connection
            mac("h1"): 1, mac("h2"): 1, 

            mac("h5"): {
                mac("h3"): 1, 
                mac("h4"): 1,

                mac("vc2"): 2
            },

            mac("ps"): 1,
        },

        4: {
            # Direct connections
            mac("ds"): 4,

            # Slow gaming connections
            mac("vc1"): 1,
            mac("vc2"): 3,

            # No other connections in work mode
            mac("h5"): (2,45),
        },

        5: {
            # Direct connections
            mac("ps"): 3,

            # fast connection  dst, {src : (output port, output queue)}
            mac("h1"): {mac("ps") : (1,521)}, 
            mac("h2"): {mac("ps"):(1,521)}, 
            mac("h3"): {mac("ps"):(1,521)}, 
            mac("h4"): {mac("ps"):(1,521)}, 
            mac("h5"): {
                mac("ps"):(1,521), 
                mac("vc1") : (1,522),
                mac("vc2") : (1,522)
            },

            #
            mac("vc1"): (2,54), mac("vc2"): (2,54)


        },
    }



def get_work_forbidden():
    # For gaming hosts, forbidden communications to work hosts and production server
    conferencce_host_forbidden = set([ mac("h1"), mac("h2"), mac("h3"), mac("h4"), mac("ps") ])

    # For work hosts, forbidden communications to gaming hosts and gaming server
    work_host_forbidden = set([ mac("vc1"), mac("vc2"), mac("ds") ])
    
    return {
        
        mac("vc1"): conferencce_host_forbidden,
        mac("vc2"): conferencce_host_forbidden,

        mac("h1"): work_host_forbidden,
        mac("h2"): work_host_forbidden,
        mac("h3"): work_host_forbidden,
        mac("h4"): work_host_forbidden,
        mac("h5"): set([ mac("ds") ]),

        mac("ps"): work_host_forbidden,
        mac("ds"): conferencce_host_forbidden,

    }
