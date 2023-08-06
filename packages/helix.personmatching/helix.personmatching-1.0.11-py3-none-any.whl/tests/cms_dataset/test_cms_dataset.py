from datetime import datetime, timedelta
from pathlib import Path
import csv
from typing import Dict, Optional, List

# noinspection PyPackageRequirements
from fhir.resources.address import Address
from fhir.resources.bundle import Bundle, BundleEntry

# noinspection PyPackageRequirements
# noinspection PyPackageRequirements
from fhir.resources.contactpoint import ContactPoint

# noinspection PyPackageRequirements
from fhir.resources.humanname import HumanName

# noinspection PyPackageRequirements
from fhir.resources.identifier import Identifier

# noinspection PyPackageRequirements
from fhir.resources.patient import Patient

from helix_personmatching.logics.match_score import MatchScore
from helix_personmatching.matchers.matcher import Matcher


def create_patient_resource(row: Dict[str, str]) -> Patient:
    patient: Patient = Patient()
    patient.id = row["EnterpriseID"]
    patient.name = [
        HumanName(
            family=row["LAST"],
        )
    ]
    if row["FIRST"] or row["MIDDLE"]:
        patient.name[0].given = []

    if row["FIRST"]:
        first_: str = row["FIRST"]
        patient.name[0].given.append(first_)

    if row["MIDDLE"]:
        middle: str = row["MIDDLE"]
        patient.name[0].given.append(middle)

    if row["SUFFIX"]:
        patient.name[0].suffix = [row["SUFFIX"]]

    if row["GENDER"]:
        if row["GENDER"] == "FEMALE" or row["GENDER"] == "F":
            patient.gender = "female"
        elif row["GENDER"] == "MALE" or row["GENDER"] == "M":
            patient.gender = "male"
        elif row["GENDER"] == "U":
            patient.gender = "unknown"
        else:
            raise NotImplementedError(f"Unknown gender: {row['GENDER']}")

    if row["DOB"]:
        # DOB is in number of days from 1/1/1900
        initial_date = datetime.strptime("1-1-1900", "%m-%d-%Y")
        dob_ = initial_date + timedelta(days=int(row["DOB"]) - 2)
        patient.birthDate = dob_
    if row["SSN"]:
        patient.identifier = [
            Identifier(system="http://hl7.org/fhir/sid/us-ssn", value=row["SSN"])
        ]
    if row["ADDRESS1"] or row["ADDRESS2"] or row["ZIP"] or row["CITY"] or row["STATE"]:
        patient.address = [Address(use="home")]

    if row["ADDRESS1"]:
        patient.address[0].line = [row["ADDRESS1"]]
    if row["ADDRESS2"]:
        address_2 = row["ADDRESS2"]
        if not patient.address[0].line:
            patient.address[0].line = []
        patient.address[0].line.append(address_2)

    if row["CITY"]:
        patient.address[0].city = row["CITY"]

    if row["STATE"]:
        patient.address[0].state = row["STATE"]

    if row["ZIP"]:
        # noinspection PyPep8Naming
        patient.address[0].postalCode = row["ZIP"]

    if row["PHONE"] or row["EMAIL"]:
        patient.telecom = []
    if row["PHONE"]:
        patient.telecom.append(ContactPoint(system="phone", value=row["PHONE"]))
    if row["EMAIL"]:
        patient.telecom.append(ContactPoint(system="email", value=row["EMAIL"]))
    return patient


def test_cms_dataset() -> None:
    print("")
    data_dir: Path = Path(__file__).parent.joinpath("./")

    limit: Optional[int] = 100

    file_name = "ONC Patient Matching Algorithm Challenge Test Dataset.A-C.csv"
    with open(data_dir.joinpath("files/onc").joinpath(file_name)) as file:
        csv_reader = csv.DictReader(file)
        patients = list()
        i: int = 0
        for row in csv_reader:
            i = i + 1
            if limit and i > limit:
                break
            patients.append(create_patient_resource(row=row))
        print(f"Count of rows={len(patients)}")

        bundle = Bundle(
            type="searchset",
            total=len(patients),
            entry=[BundleEntry(resource=resource) for resource in patients],
        )
        with open(
            data_dir.joinpath("files/bundles").joinpath(
                file_name.replace(".csv", ".json")
            ),
            "w",
        ) as json_file:
            json_file.write(bundle.json())

        matcher: Matcher = Matcher()
        match_scores: List[MatchScore] = matcher.match_resources(
            source=bundle.entry[0].resource, target=bundle
        )
        for match_score in match_scores:
            print(f"{match_score!r}")
