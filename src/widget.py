from src import masks
def mask_account_card(finding_numbers:str)-> str:
    string_numbers = ""
    string_letters = ""
    for finding in finding_numbers:
        if finding.isdigit():
            string_numbers += finding
        else:
            string_letters += finding

    return string_numbers, string_letters




