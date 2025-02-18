class JSeriesMessage:
    jseries_message_parts = [
        "time_slot_type",                   "relayed_transmission_indicator",
        "type_modifier",                    "source_track_number",
        "secure_data_unit_serial_number",
    ]

    def __init__(self, **kwargs):
        """
        Initialize a jseries message, it requires that you send one of each of the jseries message parts
        """
        self.message_parts = {}

        # self.time_slot_type = None
        # self.relayed_transmission_indicator = None
        # self.type_modifier = None
        # self.source_track_number = None
        # self.secure_data_unit_serial_number = None

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

        # if "time_slot_type" in keys:
        #     self.time_slot_type                 = kwargs["time_slot_type"]
        # if "relayed_transmission_indicator" in keys:
        #     self.relayed_transmission_indicator = kwargs["relayed_transmission_indicator"]
        # if "type_modifier" in keys:
        #     self.type_modifier                  = kwargs["type_modifier"]
        # if "source_track_number" in keys:
        #     self.source_track_number            = kwargs["source_track_number"]
        # if "secure_data_unit_serial_number" in keys:
        #     self.secure_data_unit_serial_number = kwargs["secure_data_unit_serial_number"]
                
    def __setitem__(self, key, value):
        """I'm lazy and I don't want to have to specify every property, so instead I'm just gonna just use the set item like it's a dictionary"""
        self.message_parts[key] = value
    def __getitem__(self, key):
        """I'm lazy and and just want to get my properties at if it's a dictionary"""
        return self.message_parts[key]
    def __str__(self):
        """Pretty print of our object"""
        ## TO-DO: update me to include the message body of our message
        return f"JSeries Message: header {self.message_parts} and message (N/A)"


    def ParseJSeriesFromByteArray(byteArray):
        """
        Parses a byte array and extracts specific bit fields into variables.

        Args:
            byte_array: The input byte array.

        Returns:
            A JSeriesMessage.
        """
        # try:
        # Convert byte array to bit string
        bit_string = "".join(bin(byte)[2:].zfill(8) for byte in byte_array)

        # Check if the bit string has enough bits for all fields
        if len(bit_string) < 35:  # Need at least 35 bits (up to position 34)
            # return None
            raise ValueError("Minimum number of bits not passed, JSeriesHeader has to be of length 34")

        # Extract bit fields
        time_slot_type = int(bit_string[0:3], 2)
        relayed_transmission_indicator = int(bit_string[3], 2)
        type_modifier = int(bit_string[3], 2)  # Same bit as relayed_transmission_indicator
        source_track_number = int(bit_string[4:19], 2)
        secure_data_unit_serial_number = int(bit_string[19:35], 2)

        return JSeriesMessage(
            time_slot_type=time_slot_type,      relayed_transmission_indicator=relayed_transmission_indicator,
            type_modifier=type_modifier,        source_track_number=source_track_number,
            secure_data_unit_serial_number=secure_data_unit_serial_number,
        )

        # return {
        #     "time_slot_type": time_slot_type,
        #     "relayed_transmission_indicator": relayed_transmission_indicator,
        #     "type_modifier": type_modifier,
        #     "source_track_number": source_track_number,
        #     "secure_data_unit_serial_number": secure_data_unit_serial_number,
        # }

        # except (ValueError, IndexError):  # Handle potential errors during conversion or indexing.
        #     return None  # Or raise an exception if desired


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

