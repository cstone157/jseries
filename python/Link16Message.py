class Link16Message:
    link_message_parts = [
        "word_format",                  "link_16_label",
        "link_16_sublabel",             "message_length_indicator",
        "information_fields",           "parity"
    ]

    def __init__(self, **kwargs):
        """
        Initialize a jseries message, it requires that you send one of each of the jseries message parts
        """
        self.message_parts = {}

        ##     I don't want to return a message that only contains one error, I want it to have all
        ## the other messages as well, so I'm gonna create an exception message and raise that instead
        exception_msg = []

        ## Check and see if our kwargs contains any of the parameters that we care about
        keys = kwargs.keys()
        for k in keys:
            if k in JSeriesMessage.jseries_message_parts:
                self[k] = kwargs[k]
            else:
                exception_msg.append(f"Error unrecognized parameter {k}='{kwargs[k]}', please try again")
        ## Check and ensure that all of the parts of the jseries_message_parts were passed in
        for p in JSeriesMessage.jseries_message_parts:
            if p not in keys:
                exception_msg.append(f"Error missing parameter {p}")
                
        if len(exception_msg) > 0:
            raise Exception(exception_msg)


    def __setitem__(self, key, value):
        """I'm lazy and I don't want to have to specify every property, so instead I'm just gonna just use the set item like it's a dictionary"""
        self.message_parts[key] = value
    def __getitem__(self, key):
        """I'm lazy and and just want to get my properties at if it's a dictionary"""
        return self.message_parts[key]
    def __str__(self):
        """Pretty print of our object"""
        ## TO-DO: update me to include the message body of our message
        return f"Link16 Message: {self.message_parts}"






print(" Test case: 01 ======================= ")
try:
    j1 = JSeriesMessage(
        time_slot_type=1, relayed_transmission_indicator=1,
        type_modifier=1, source_track_number=1,
        secure_data_unit_serial_number=1
    )
    print(j1)
except error:
    print(error)


print("\n Test case: 02 ======================= ")
try:
    byte_array = b'\x12\x34\x56\x78\x56\x78\x56\x78\x56\x78'
    j2 = JSeriesMessage.ParseJSeriesFromByteArray(byte_array)
    # if j2:
    print(j2)
    # else:
    #     print("Error: Byte array is too short or invalid.")
except error:
    print(error)


print("\n Test case: 03 ======================= ")
try:
    byte_array = b'\x07\xC0\x00\x00'
    j_error1 = JSeriesMessage.ParseJSeriesFromByteArray(byte_array)
    # if j3:
    print(j_error1)
    # else:
    #     print("Error: Byte array is too short or invalid.")
except error:
    print(error)

