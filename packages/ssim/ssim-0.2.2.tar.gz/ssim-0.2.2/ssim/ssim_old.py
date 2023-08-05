import re
from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, WEEKLY
import logging

preprocessing_pattern = {"SIR": "(\n/\s*)(\w[A-Z]*.\d+ \w*[A-Z]*.{0,1}\d*)(\s*/\n)", "SIM": "\n4"}
preprocessing_replace = {"SIR": r" /\2/\n", "SIM": r"4"}

# For email parsing see: emailregex.com
header_pattern = {
    "SIR": (
        "^(?P<file_type>\w+)\s*\n"
        "/{0,1}(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+){0,1}\n{0,1}"
        "(?P<season>\w+)\s*\n"
        "(?P<export_date>\w+)\s*\n"
        "(?P<origin>\w+)\n"
        "(REYT/\n){0,1}"
    ),
    "SIM": (
        "^1AIRLINE STANDARD SCHEDULE DATA SET\s{156}\d{9}"
        "[\n0]{805}[A-Z0-9 ]{10}"
        "(?P<season>[A-Z0-9]{3}){0,1}"
        "[A-Za-z0-9 ]+[\n0]{805}"
    ),
}

footer_pattern = {
    "SIR": ("(?P<special_information>SI [A-Za-z0-9 ()\.:=]+)\n" "(?P<general_information>GI [A-Za-z0-9 ()\.:=]+)\n*$"),
    "SIM": "[\n0]{403}(?P<footer>5[A-Z0-9 ]+)[\n0]{2815}$",
}

return_row_pattern = (
    "(?P<action_code>[A-Z])"
    "(?P<arrival_flight_prefix>[A-Z]{2,3})"
    "(?P<arrival_flight_suffix>\d+[A-Z]*)"
    "\s"
    "(?P<departure_flight_prefix>[A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z])"
    "(?P<departure_flight_suffix>\d+[A-Z]*)"
    "\s"
    "(?P<start_date_of_operation>\d{2}[A-Z]{3})"
    "(?P<end_date_of_operation>\d{2}[A-Z]{3})"
    "\s"
    "(?P<days_of_operation>\d{7})"
    "\s"
    "(?P<seat_number>\d{3})"
    "(?P<aircraft_type_3_letter>\w{3})"
    "\s"
    "(?P<origin_of_flight>[A-Z]{3})"
    "(?P<scheduled_time_of_arrival_utc_utc>\d{4})"
    "\s"
    "(?P<scheduled_time_of_departure_utc_utc>\d{4})"
    "(?P<overnight_indicator>[0-6])*"
    "(?P<destination_of_flight>[A-Z]{3})"
    "\s"
    "(?P<arrival_type_of_flight>[A-Z])"
    "(?P<arrival_frequency_rate>\d){0,1}"
    "(?P<departure_type_of_flight>[A-Z])"
    "(?P<departure_frequency_rate>\d){0,1}"
    "\s{0,1}"
    "(?P<additional_information>.+){0,1}"
    "\n*"
)

departure_row_pattern = (
    "(?P<action_code>[A-Z])"
    "\s"
    "(?P<departure_flight_prefix>[A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z])"
    "(?P<departure_flight_suffix>\d+[A-Z]*)"
    "\s"
    "(?P<start_date_of_operation>\d{2}[A-Z]{3})"
    "(?P<end_date_of_operation>\d{2}[A-Z]{3})"
    "\s"
    "(?P<days_of_operation>\d{7})"
    "\s"
    "(?P<seat_number>\d{3})"
    "(?P<aircraft_type_3_letter>\w{3})"
    "\s"
    "(?P<scheduled_time_of_departure_utc_utc>\d{4})"
    "(?P<destination_of_flight>[A-Z]{3})"
    "\s"
    "(?P<type_of_flight>[A-Z])"
    "(?P<frequency_rate>\d){0,1}"
    "\s{0,1}"
    "(?P<additional_information>.+){0,1}"
    "\n*"
)

arrival_row_pattern = (
    "(?P<action_code>[A-Z])"
    "(?P<arrival_flight_prefix>[A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z])"
    "(?P<arrival_flight_suffix>\d+[A-Z]*)"
    "\s"
    "(?P<start_date_of_operation>\d{2}[A-Z]{3})"
    "(?P<end_date_of_operation>\d{2}[A-Z]{3})"
    "\s"
    "(?P<days_of_operation>\d{7})"
    "\s"
    "(?P<seat_number>\d{3})"
    "(?P<aircraft_type_3_letter>\w{3})"
    "\s"
    "(?P<origin_of_flight>[A-Z]{3})"
    "(?P<scheduled_time_of_arrival_utc_utc>\d{4})"
    "\s"
    "(?P<type_of_flight>[A-Z])"
    "(?P<frequency_rate>\d){0,1}"
    "\s{0,1}"
    "(?P<additional_information>.+){0,1}"
    "\n*"
)

arrival_row_pattern_nl = (
    "(?P<action_code>[A-Z])"
    "(?P<arrival_flight_prefix>[A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z]|\w{2}){0,1}"
    "(?P<arrival_flight_suffix>\d+[A-Z]*|\w+){0,1}"
    "\s"
    "(?P<start_date_of_operation>\d{2}[A-Z]{3})"
    "(?P<end_date_of_operation>\d{2}[A-Z]{3}|)"
    "\s"
    "(?P<days_of_operation>\d{7}|)"
    "\s{0,1}"
    "(?P<seat_number>\d{3}){0,1}"
    "(?P<aircraft_type_3_letter>\w{3})"
    "\s"
    "(?P<previous_stop_of_flight>[A-Z0-9]{3})"
    "(?P<origin_of_flight>[A-Z0-9]{3})"
    "(?P<scheduled_time_of_arrival_utc_utc>\d{4}){0,1}"
    "\s"
    "(?P<type_of_flight>[A-Z])"
    "(?P<frequency_rate>\d){0,1}"
    "\s{0,1}"
    "(?P<additional_information>.*[a-zA-Z0-9].*){0,1}"
)

departure_row_pattern_nl = (
    "(?P<action_code>[A-Z])"
    "\s"
    "(?P<departure_flight_prefix>[A-Z]{2,3}|[A-Z][0-9]|[0-9][A-Z]|\w{2}){0,1}"
    "(?P<departure_flight_suffix>\d+[A-Z]*|\w+){0,1}"
    "\s"
    "(?P<start_date_of_operation>\d{2}[A-Z]{3})"
    "(?P<end_date_of_operation>\d{2}[A-Z]{3}|)"
    "\s"
    "(?P<days_of_operation>\d{7}|)"
    "\s{0,1}"
    "(?P<seat_number>\d{3}){0,1}"
    "(?P<aircraft_type_3_letter>\w{3})"
    "\s"
    "(?P<scheduled_time_of_departure_utc_utc>\d{4}){0,1}"
    "(?P<next_stop_of_flight>[A-Z0-9]{3})"
    "(?P<destination_of_flight>[A-Z0-9]{3})"
    "\s"
    "(?P<type_of_flight>[A-Z])"
    "(?P<frequency_rate>\d){0,1}"
    "\s{0,1}"
    "(?P<additional_information>.*[a-zA-Z0-9].*){0,1}"
)

sim_row_pattern = (
    "^3"
    "(?P<action_code>[A-Z ])"
    "(?P<flight_prefix>[A-Z0-9]{2})\s"
    "(?P<flight_suffix>\s{3}[0-9]{1}|\s{2}[0-9]{2}|\s[0-9]{3}|[0-9]{4}|\s{3,4})"
    "(?P<some_code_1>[0-9]{4})"
    "(?P<type_of_flight>[A-Z]{1})"
    "(?P<start_date_of_operation>[0-9]{2}[A-Z]{3}[0-9]{2}|\s{5})"
    "(?P<end_date_of_operation>[0-9]{2}[A-Z]{3}[0-9]{2}|\s{5})"
    "(?P<days_of_operation>[0-9 ]{8})"
    "(?P<origin_of_flight>[A-Z]{3})"
    "(?P<scheduled_time_of_departure_utc_local>\d{4})"
    "(?P<scheduled_time_of_departure_utc_utc>\d{4})[+-]\d{4}"
    "(?P<some_code_3>\w|\s)\s"
    "(?P<destination_of_flight>[A-Z]{3})"
    "(?P<scheduled_time_of_arrival_utc_local>\d{4})"
    "(?P<scheduled_time_of_arrival_utc_utc>\d{4})[+-]\d{4}"
    "(?P<some_code_4>\w|\s)\s"
    "(?P<aircraft_type_3_letter>\w{3})[A-Z ]"
    "\s{52}"
    "(?P<prefix_1>[A-Z0-9 ]{8})\s"
    "(?P<connecting_flight_prefix>[A-Z0-9 ]{2}|\s{2})\s"
    "(?P<connecting_flight_suffix>\s{4}|\s{3}[0-9]{1}|\s{2}[0-9]{2}|\s[0-9]{3}|[0-9]{4})"
    ".{28}"
    "(?P<arrival_seat_number>[0-9A-Z ]{9})"  # foutje bedankt
    "(?P<aircraft_type_4_letter>.{4})"
    "(?P<departure_seat_number>[0-9]{3}|\s{3})"
    "\s{6}"
    "(?P<row_nr>[0-9]{6})"
    "4{0,1}\s{0,1}"
    "(?P<connecting_flight_prefix_2>[A-Z]{2}){0,1}\s{0,1}"
    "(?P<connecting_flight_suffix_2>\s{3}[0-9]{1}|\s{2}[0-9]{2}|\s[0-9]{3}|[0-9]{4}|\s{3,4}){0,1}"
    "(?P<some_code_6>[0-9 ]{4}){0,1}"
    "(?P<flight_type_3>[A-Z]{0,1})"
    "\s{0,14}"
    "(?P<additional_information>.+){0,1}$"
)

sim_row_zero_line_pattern = "0{200}"

row_patterns = [
    re.compile(arrival_row_pattern),
    re.compile(departure_row_pattern),
    re.compile(return_row_pattern),
    re.compile(arrival_row_pattern_nl),
    re.compile(departure_row_pattern_nl),
    re.compile(sim_row_pattern),
    re.compile(sim_row_zero_line_pattern),
]


def _parse_slotfile(text, year_prefix):
    """
    Parses a SIR or SIM message and returns it as a list of dicts describing flight schedules.

    Parameters
    ----------.
    :type text: string
    :type year_prefix: string

    Returns
    -------
    text: list of dicts, describing rows of a slotfile.
    header: dict, describing the header of the slotfile.
    footer: dict, describing the footer of the slotfile.
    """

    if re.search(header_pattern["SIR"], text):
        file_format = "SIR"

    elif re.search(header_pattern["SIM"], text):
        file_format = "SIM"

    # File format not recognized
    else:
        raise ValueError("Could not find required header information in file:\n%s" % text[0:200])

    header_match = re.search(header_pattern[file_format], text)
    footer_match = re.search(footer_pattern[file_format], text)
    header = header_match.groupdict()
    header_lenght = header_match.group(0).count("\n")

    footer_lenght = 0
    try:
        footer = footer_match.groupdict()
        footer_lenght = footer_match.group(0).count("\n")
    except AttributeError:
        footer = {}

    try:
        rows_text = text[header_match.end() : footer_match.start()]
    except AttributeError:
        rows_text = text[header_match.end() :]
        # pass

    rows_text = re.sub(preprocessing_pattern[file_format], preprocessing_replace[file_format], rows_text)
    additional_info = len(re.findall("/ R.* /", text)) + len(re.findall("\n4.+\n", text))

    rows = rows_text.splitlines()
    unparsed_rows = []
    parsed_rows = []
    ambiguous_rows = []
    multi_interpretation = []

    for row in rows:
        parsed_row = {}

        for row_pattern in row_patterns:
            try:
                parsed_row = re.search(row_pattern, row).groupdict()
                if parsed_row:
                    multi_interpretation += [parsed_row]

            except AttributeError:
                pass

        if parsed_row == {} and not re.search(sim_row_zero_line_pattern, row):
            unparsed_rows += [{"raw": row}]

        else:
            parsed_row["raw"] = row
            parsed_rows += [parsed_row]

    processed_rows = []
    unprocessed_rows = []

    if file_format == "SIR":
        parsed_rows = list(map(_fix_bad_midnight, parsed_rows))

        for row in parsed_rows:
            try:
                processed_rows += [_process_dates_sir(row, header, year_prefix=year_prefix)]

            except Exception as err:
                row["error"] = err
                unprocessed_rows += [row]

    if file_format == "SIM":
        parsed_rows = list(map(_fix_bad_midnight, parsed_rows))
        for row in parsed_rows:
            try:
                processed_rows += [_process_dates_sim(row, header, year_prefix=year_prefix)]

            except Exception as err:
                row["error"] = err
                unprocessed_rows += [row]

    if len(ambiguous_rows) > 0:
        logging.warning(
            "Found %i ambiguous slots that can be interpreted in multiple ways:\n%s"
            % (multi_interpretation, ambiguous_rows)
        )

    if len(unparsed_rows) > 0:
        logging.warning("Cold not parse %i row(s):\n%s" % (len(unparsed_rows), "\n".join(map(str, unparsed_rows))))

    logging.info(
        "[%s row counts]: %i header, %i flight data, %i extra information, %i footer. %i valid flight records."
        " %i total rows."
        % (
            file_format,
            header_lenght,
            rows_text.strip("\n").count("\n") + 1,
            additional_info,
            footer_lenght,
            len(processed_rows),
            text.count("\n"),
        )
    )

    return processed_rows, header, footer


def _fix_bad_midnight(row):
    """
    Fixes bad midnight notation - converts time from 2400 to 0000.

    Parameters
    ----------.
    :param row: dict, describing a slot.
    :return row: dict, describing a slot.
    """
    # for SIR
    if "scheduled_time_of_arrival_utc_utc" in row:
        if row["scheduled_time_of_arrival_utc_utc"] == "2400":
            row = _update_dict(row, {"scheduled_time_of_arrival_utc_utc": "0000"})

            logging.warning("Slot with invalid time notation. Adjusting time to 0000.\n(%s)" % row)

    if "scheduled_time_of_departure_utc_utc" in row:
        if row["scheduled_time_of_departure_utc_utc"] == "2400":
            row = _update_dict(row, {"scheduled_time_of_departure_utc_utc": "0000"})

            logging.warning("Slot with invalid time notation. Adjusting time to 0000.\n(%s)" % row)

    # for SSIM
    if "scheduled_time_of_arrival_utc_local" in row:
        if row["scheduled_time_of_arrival_utc_utc"] == "2400":
            row = _update_dict(row, {"scheduled_time_of_arrival_utc_utc": "0000"})

            logging.warning("Slot with invalid time notation. Adjusting time to 0000.\n(%s)" % row)

    if "scheduled_time_of_departure_utc_local" in row:
        if row["scheduled_time_of_departure_utc_utc"] == "2400":
            row = _update_dict(row, {"scheduled_time_of_departure_utc_utc": "0000"})

            logging.warning("Slot with invalid time notation. Adjusting time to 0000.\n(%s)" % row)

    return row


def _process_dates_sir(slot, header, year_prefix):

    year = year_prefix + header["season"][1:]

    if "end_date_of_operation" not in slot:
        slot["end_date_of_operation"] = slot["start_date_of_operation"]
    if slot["end_date_of_operation"] == "":
        slot["end_date_of_operation"] = slot["start_date_of_operation"]

    slot["start_date_of_operation"] = datetime.strptime(slot["start_date_of_operation"] + year, "%d%b%Y")
    slot["end_date_of_operation"] = datetime.strptime(slot["end_date_of_operation"] + year, "%d%b%Y")

    if "W" in header["season"]:
        if slot["end_date_of_operation"].month < 6:
            slot["end_date_of_operation"] = slot["end_date_of_operation"] + relativedelta(years=1)

            if slot["start_date_of_operation"].month < 6:
                slot["start_date_of_operation"] = slot["start_date_of_operation"] + relativedelta(years=1)

    slot["start_date_of_operation"] = slot["start_date_of_operation"].strftime("%Y-%m-%d")
    slot["end_date_of_operation"] = slot["end_date_of_operation"].strftime("%Y-%m-%d")

    return slot


# parse dates for sim format
# sim dates are aware of their year, so maybe header not needed?
def _process_dates_sim(slot, header, year_prefix):
    # attempt at processing seats. Work with predefined class indicators (economy, business). This list may be incomplete
    seat_indicators = ["Y", "C", "F", "C", "M"]
    seats_int = None

    # for every type of indicator, check if we can find seats
    for seat_indicator in seat_indicators:
        res = re.search("" + seat_indicator + "(?P<" + seat_indicator + ">[0-9]{1,3})", slot["arrival_seat_number"])
        if res:
            if not seats_int:
                seats_int = 0
            seats_int += int(res.groupdict()[seat_indicator])

    for k in slot.keys():
        if slot[k]:
            slot[k] = slot[k].strip(" ")

    # after previous operation we can assign non-string values to dict
    slot["seat_int"] = seats_int

    slot["start_date_of_operation"] = datetime.strptime(
        slot["start_date_of_operation"][:-2] + year_prefix + slot["start_date_of_operation"][-2:], "%d%b%Y"
    )
    slot["end_date_of_operation"] = datetime.strptime(
        slot["end_date_of_operation"][:-2] + year_prefix + slot["end_date_of_operation"][-2:], "%d%b%Y"
    )

    slot["start_date_of_operation"] = slot["start_date_of_operation"].strftime("%Y-%m-%d")
    slot["end_date_of_operation"] = slot["end_date_of_operation"].strftime("%Y-%m-%d")

    if "arrival_seat_number" in slot:
        slot["seat_number"] = slot["arrival_seat_number"]
    else:
        slot["seat_number"] = slot["departure_seat_number"]
    slot["frequency_rate"] = "1"

    return slot


def _explode_aircraft_configuration_string(aircraft_configuration_string: str) -> dict:
    """
    Explodes a string containing aircraft information to.

    Parameters
    ----------.
    :param aircraft_configuration_string: str, describing aircraft configuartion.
    :return row: dict, describing aircraft configuration.
    """
    aircraft_configuration_string = aircraft_configuration_string.rstrip()

    seat_class_designators = [
        "P",
        "F",
        "A",
        "J",
        "C",
        "D",
        "I",
        "Z",
        "W",
        "S",
        "Y",
        "B",
        "H",
        "K",
        "L",
        "M",
        "N",
        "Q",
        "T",
        "V",
        "X",
        "G",
        "U",
        "E",
        "O",
        "R",
    ]

    cargo_designators = ["LL", "PP"]  # unit load devices (containers)  # pallets

    integer_designators = {"seats": seat_class_designators, "cargo": cargo_designators}

    acv_info = {}

    # seat designator should be in fixed order according to standard
    for designator_type, designators in integer_designators.items():
        for designator in designators:
            if aircraft_configuration_string.startswith(
                designator
            ) and (  # only continue if string starts with designator and...
                len(designator) > 1
                or not (  # either have a multi length designator
                    (
                        len(aircraft_configuration_string) > 1
                        and aircraft_configuration_string[1] == aircraft_configuration_string[0]
                    )
                    or aircraft_configuration_string.startswith("V V")
                )
            ):  #

                acv_info_key = designator_type + "_" + designator

                # for next iteration, remove designator from beginning of string
                aircraft_configuration_string = aircraft_configuration_string[len(designator) :]

                # standard specifies that there may be an int following. If not return empty string (to later on destinguish from NaN if data gets put in a data frame)
                acv_info_val = ""
                acv_regex = re.search(r"^\d*", aircraft_configuration_string).group()

                # if int found, add it to total and remove it from string to process as well
                if acv_regex:
                    acv_info_val = int(acv_regex)
                    if designator_type == "seats":
                        if designator_type in acv_info.keys():
                            acv_info[designator_type] += acv_info_val
                        else:
                            acv_info[designator_type] = acv_info_val

                    aircraft_configuration_string = aircraft_configuration_string[len(acv_regex) :]

                # store found information
                acv_info[acv_info_key] = acv_info_val

    # remainer are general designators
    if aircraft_configuration_string.startswith("BB"):
        acv_info["BB"] = ""

    # aircraft type
    if aircraft_configuration_string.startswith("VV"):
        acv_info["VV"] = aircraft_configuration_string[2:]
    elif aircraft_configuration_string.startswith(
        "V V"
    ):  # aircraft type alt. Assuming it won't appear together with VV.
        acv_info["V V"] = aircraft_configuration_string[3:]
    elif len(aircraft_configuration_string.strip()):
        logging.warning(
            "After trying to process aircraft configuration string, there should be no remainder. However, the following string remains in this instance: \n(%s)"
            % aircraft_configuration_string
        )

    return acv_info


def _update_dict(d, entry):
    new_d = d.copy()
    new_d.update(entry)
    return new_d


def _expand_slot(slot):
    """
    Expands slot into individual flights.

    Parameters
    ----------.
    slot: dict, description of a slot.

    Returns
    -------
    slot: list of dicts, representing flights described by the slot.
    """

    try:
        weekdays = re.sub("\s|0", "", slot["days_of_operation"])
        weekdays = [int(weekday) - 1 for weekday in weekdays]
    except KeyError:
        pass

    expanded_slot = []

    # Expand ssim legs
    flight_leg_slot_fields = {
        "action_code",
        "flight_prefix",
        "flight_suffix",
        "aircraft_type_3_letter",
        "type_of_flight",
        "origin_of_flight",
        "seat_number",
        "additional_information",
        "raw",
        "scheduled_time_of_departure_utc_local",
        "scheduled_time_of_arrival_utc_local",
        "destination_of_flight",
        "connecting_flight_prefix",
        "connecting_flight_suffix",
        "frequency_rate",
    }

    if flight_leg_slot_fields <= set(slot):
        flight_leg_slot = {
            "action_code": slot["action_code"],
            "prefix": slot["flight_prefix"],
            "suffix": slot["flight_suffix"],
            "aircraft_type_3_letter": slot["aircraft_type_3_letter"],
            "type_of_flight": slot["type_of_flight"],
            "origin": slot["origin_of_flight"],
            "destination": slot["destination_of_flight"],
            "seat_number": slot["seat_number"],
            "seats_int": slot["seat_int"],
            "additional_information": slot["additional_information"],
            "raw": slot["raw"],
            "connecting_flight_prefix": slot["connecting_flight_prefix"],
            "connecting_flight_suffix": slot["connecting_flight_suffix"],
        }

        # determine flight times
        if slot["scheduled_time_of_arrival_utc_utc"] is not None:
            departure_start_date = datetime.strptime(
                slot["start_date_of_operation"] + slot["scheduled_time_of_departure_utc_utc"], "%Y-%m-%d%H%M"
            )
            departure_end_date = datetime.strptime(
                slot["end_date_of_operation"] + slot["scheduled_time_of_departure_utc_utc"], "%Y-%m-%d%H%M"
            )

            # determine flight time
            departure_time = datetime.strptime(slot["scheduled_time_of_departure_utc_utc"], "%H%M")
            arrival_time = datetime.strptime(slot["scheduled_time_of_arrival_utc_utc"], "%H%M")
            flight_leg_slot["flight_time_seconds"] = (
                arrival_time - departure_time
            ).seconds  # if we take seconds, overnight flights will also get correct flight time because the -1 day gets removed

        if slot["frequency_rate"]:
            dates = rrule(
                freq=WEEKLY,
                interval=int(slot["frequency_rate"]),
                dtstart=departure_start_date,
                until=departure_end_date,
                byweekday=weekdays,
            )
        else:
            dates = rrule(freq=WEEKLY, dtstart=departure_start_date, until=departure_end_date, byweekday=weekdays)

        if slot["scheduled_time_of_departure_utc_utc"] is not None:
            flight_leg_slot["flight_datetime"] = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
        else:
            flight_leg_slot["flight_datetime"] = [x.strftime("%Y-%m-%d") for x in dates]

        expanded_slot += [flight_leg_slot]

    else:
        # Expand arriving flights
        arrival_slot_fields = {
            "action_code",
            "arrival_flight_prefix",
            "arrival_flight_suffix",
            "aircraft_type_3_letter",
            "type_of_flight",
            "origin_of_flight",
            "seat_number",
            "additional_information",
            "raw",
            "frequency_rate",
        }

        if arrival_slot_fields <= set(slot):

            arrival_slot = {
                "action_code": slot["action_code"],
                "ad": "A",
                "prefix": slot["arrival_flight_prefix"],
                "suffix": slot["arrival_flight_suffix"],
                "aircraft_type_3_letter": slot["aircraft_type_3_letter"],
                "type_of_flight": slot["type_of_flight"],
                "destination": slot["origin_of_flight"],
                "seats": slot["seat_number"],
                "additional_information": slot["additional_information"],
                "raw": slot["raw"],
            }

            if slot["scheduled_time_of_arrival_utc_utc"] is not None:
                arrival_start_date = datetime.strptime(
                    slot["start_date_of_operation"] + slot["scheduled_time_of_arrival_utc_utc"], "%Y-%m-%d%H%M"
                )
                arrival_end_date = datetime.strptime(
                    slot["end_date_of_operation"] + slot["scheduled_time_of_arrival_utc_utc"], "%Y-%m-%d%H%M"
                )
            else:
                arrival_start_date = datetime.strptime(slot["start_date_of_operation"], "%Y-%m-%d")
                arrival_end_date = datetime.strptime(slot["end_date_of_operation"], "%Y-%m-%d")

            if slot["frequency_rate"]:
                dates = rrule(
                    freq=WEEKLY,
                    interval=int(slot["frequency_rate"]),
                    dtstart=arrival_start_date,
                    until=arrival_end_date,
                    byweekday=weekdays,
                )
            else:
                dates = rrule(freq=WEEKLY, dtstart=arrival_start_date, until=arrival_end_date, byweekday=weekdays)

            if slot["scheduled_time_of_arrival_utc_utc"] is not None:
                arrival_slot["flight_datetime"] = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
            else:
                arrival_slot["flight_datetime"] = [x.strftime("%Y-%m-%d") for x in dates]

            expanded_slot += [arrival_slot]

        # Expand departing flights
        departure_slot_fields = {
            "action_code",
            "departure_flight_prefix",
            "departure_flight_suffix",
            "aircraft_type_3_letter",
            "type_of_flight",
            "destination_of_flight",
            "seat_number",
            "additional_information",
            "raw",
            "frequency_rate",
        }
        if departure_slot_fields <= set(slot):
            departure_slot = {
                "action_code": slot["action_code"],
                "ad": "D",
                "prefix": slot["departure_flight_prefix"],
                "suffix": slot["departure_flight_suffix"],
                "aircraft_type_3_letter": slot["aircraft_type_3_letter"],
                "type_of_flight": slot["type_of_flight"],
                "destination": slot["destination_of_flight"],
                "seats": slot["seat_number"],
                "additional_information": slot["additional_information"],
                "raw": slot["raw"],
            }

            if "overnight_indicator" in slot:
                overnight_time = relativedelta(days=int(slot["overnight_indicator"]))
            else:
                overnight_time = relativedelta(days=0)

            if slot["scheduled_time_of_departure_utc_utc"]:
                departure_start_date = (
                    datetime.strptime(
                        slot["start_date_of_operation"] + slot["scheduled_time_of_departure_utc_utc"], "%Y-%m-%d%H%M"
                    )
                    + overnight_time
                )
                departure_end_date = (
                    datetime.strptime(
                        slot["end_date_of_operation"] + slot["scheduled_time_of_departure_utc_utc"], "%Y-%m-%d%H%M"
                    )
                    + overnight_time
                )

            else:
                departure_start_date = datetime.strptime(slot["start_date_of_operation"], "%Y-%m-%d") + overnight_time
                departure_end_date = datetime.strptime(slot["end_date_of_operation"], "%Y-%m-%d") + overnight_time

            if slot["frequency_rate"]:
                dates = rrule(
                    freq=WEEKLY,
                    interval=int(slot["frequency_rate"]),
                    dtstart=departure_start_date,
                    until=departure_end_date,
                    byweekday=weekdays,
                )
            else:
                dates = rrule(freq=WEEKLY, dtstart=departure_start_date, until=departure_end_date, byweekday=weekdays)

            if slot["scheduled_time_of_departure_utc_utc"] is not None:
                departure_slot["flight_datetime"] = [x.strftime("%Y-%m-%d %H:%M") for x in dates]
            else:
                departure_slot["flight_datetime"] = [x.strftime("%Y-%m-%d") for x in dates]

            expanded_slot += [departure_slot]

    expanded_slot = [_update_dict(x, {"flight_datetime": f_dt}) for x in expanded_slot for f_dt in x["flight_datetime"]]

    return expanded_slot


def read(slotfile, year_prefix="20"):
    """
    Parses and processes a valid ssim file.

    Parameters
    ----------.
    slotfile : path to a slotfile.
    year_prefix: string, defining the century of the flight.

    Returns
    -------
    slots: list of dicts, describing exact slots of a slotfile.
    header: dict, describing the header of the slotfile.
    footer: dict, describing the footer of the slotfile.
    """

    logging.info("Reading and parsing slotfile: %s." % slotfile)
    with open(slotfile) as f:
        text = f.read()

    slots, header, footer = _parse_slotfile(text, year_prefix=year_prefix)

    return slots, header, footer


def expand_slots(slots):
    """
    Expands a list of slots into flights.

    Parameters
    ----------.
    :param slots: list, a list of slot dicts.

    Returns
    -------
    :return: flattened_flights: list, a list of flight dicts.
    """

    flights = list(map(_expand_slot, slots))
    flattened_flights = [f for fs in flights if len(fs) != 0 for f in fs]
    unexpanded_slots = [s for s, fs in zip(slots, flights) if len(fs) == 0]

    if len(unexpanded_slots) > 0:
        logging.warning(
            "Could not expand %i slot(s):\n%s" % (len(unexpanded_slots), "\n".join(map(str, unexpanded_slots)))
        )

    logging.info("Expanded %i slots into %i flights." % (len(slots) - len(unexpanded_slots), len(flattened_flights)))
    return flattened_flights


def read_csv(slotfile):
    """
    Parses and processes a csv ssim file.

    Parameters
    ----------.
    slotfile : path to a csv slotfile.

    Returns
    -------
    slots: flattened_flights: list, a list of flight dicts.
    """

    logging.info("Reading %s." % slotfile)
    with open(slotfile) as f:
        text = f.read()

    logging.info("Parsing and processing slotfile.")
    flightnumber_regex = "([A-Z]{2,3}|\w{2})\s*(\d+[A-Z]*|\w+)"
    arrival_header = (
        "action_code",
        "origin",
        "arrival_flight_prefix",
        "arrival_flight_suffix",
        "ad",
        "scheduled_time_of_arrival_utc_utc",
        "start_date_of_operation",
        "end_date_of_operation",
        "days_of_operation",
        "previous_stop_of_flight",
        "origin_of_flight",
        "aircraft_type_3_letter",
        "type_of_flight",
        "frequency_rate",
        "unknown_2",
        "unknown_3",
        "unknown_4",
        "season",
        "additional_information",
        "seat_number",
        "raw",
    )
    departure_header = (
        "action_code",
        "origin",
        "departure_flight_prefix",
        "departure_flight_suffix",
        "ad",
        "scheduled_time_of_departure_utc_utc",
        "start_date_of_operation",
        "end_date_of_operation",
        "days_of_operation",
        "next_stop_of_flight",
        "destination_of_flight",
        "aircraft_type_3_letter",
        "type_of_flight",
        "frequency_rate",
        "unknown_2",
        "unknown_3",
        "unknown_4",
        "season",
        "additional_information",
        "seat_number",
        "raw",
    )

    rows = [row.split(";") + [row] for row in re.sub("\n\n", "\n", text).splitlines()]

    # Fix the date formatting, parse the flightnumber
    rows = [row[0:5] + [row[5][0:4] + "-" + row[5][4:6] + "-" + row[5][6:]] + row[6:] for row in rows]
    rows = [row[0:6] + [row[6][0:4] + "-" + row[6][4:6] + "-" + row[6][6:]] + row[7:] for row in rows]
    rows = [row[0:2] + list(re.search(flightnumber_regex, row[2]).groups()) + row[3:] for row in rows]

    arrival_rows = [dict(zip(arrival_header, row)) for row in rows if row[4] == "A"]
    departure_rows = [dict(zip(departure_header, row)) for row in rows if row[4] == "D"]
    logging.info("Found %i valid slots in %i rows." % (len(arrival_rows) + len(departure_rows), len(text.splitlines())))

    logging.info("Expanding flights.")
    flights = map(_expand_slot, arrival_rows + departure_rows)
    flattened_flights = [item for sublist in flights for item in sublist]
    logging.info(
        "Expanded %i slots into %i flights." % ((len(arrival_rows) + len(departure_rows)), len(flattened_flights))
    )

    return flattened_flights
